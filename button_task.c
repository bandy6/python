/*
 * @-: Copyright (C) 2018 Yunding Network Technology(Beijing) Co., Ltd
 * @.: All Rights Reserved.
 * @*: Confidential and Proprietary - Yunding Network Technology.
 * @Description: 按键任务处理
 * @LastEditors: anfengbo
 */
#include "hal_backlight_pubif.h"
#include "hal_sys_reset_pubif.h"
#include "hal_back_board_button_pubif.h"
#include "hal_misc_button_pubif.h"
#include "hal_touchpad_pubif.h"

#include "ble_platform.h"

#include "button_usb.h"
#include "button_unlock.h"
#include "button_childlock.h"
#include "button_reset.h"
#include "button_register.h"
#include "button_intrude.h"
#include "button_touchpad.h"
#include "button_security.h"
#include "button_task.h"
#include "ui_interaction.h"
#include "sys.h"
#include "app_schedule.h"

T_TASK button_task = APP_TASK_INIT(button);

/**
 * @brief : buttons_action_init
 * @param {*}
 * @return {*}
 */
void buttons_action_init(void) {
    //       触摸键盘灯自动关闭初始化
    button_indoor_open_door_init();

    //触摸键盘初始化
    touchpad_register();

    keyboard_action_init(UI_OFF);

    // 混合按键初始化
    misc_button_pub_init(misc_button_reset_logic, front_board_intrude_logic, NULL, false);

    // 重置超时检测定时器初始化
    button_reset_factory_timer_init();

    back_board_button_pub_init(DEV_REGISTER_CB, FACTORY_RESET_CB, CHILD_LOCK_CB,
                               OPEN_DOOR_BUTTON_CB, OPEN_DOOR_TOUCH_CB, OPEN_DOOR_RIGHT_TOUCH_CB);

    deployable_mode_init();
}

/**
 * @brief : send_button_action_task_type
 * @param {U8} msg_type
 * @param {U8} key
 * @return {*}
 */
void send_button_action_task_type(U8 msg_type, U8 key) {
    button_action_msg_context* context = NULL;

    context = (button_action_msg_context*)OS_Malloc(sizeof(button_action_msg_context));
    APP_ERROR_CHECK(context == NULL);

    memset(context, 0, sizeof(button_action_msg_context));
    context->key = key;

    OS_MsgSendDataFast(&button_task, msg_type, (U8*)context, sizeof(button_action_msg_context));
}

/**
 * @brief : button_task消息处理
 * @param {T_MSG*} msg
 * @param {U16} msg_size
 * @return {*}
 */
static void button_task_on_msg(T_MSG* msg, U16 msg_size) {
    if (msg->data != NULL) {
        OS_Free(msg->data);
        msg->data = NULL;
    }
}

/**
 * @brief : button task 初始化
 * @param {*}
 * @return {*}
 */
void button_task_init(void) {
    buttons_action_init();

    OS_TaskOpen(&button_task, LOW, button_task_on_msg);

    LOG(LEVEL_DEBUG, "button_task_init");
}
