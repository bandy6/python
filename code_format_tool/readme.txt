1.拷贝code_format_tool/文件夹到其它项目的根文件夹下，即可完成部署。完成后，双击clang-format_set.bat

2.格式化1个文件夹下的所有文件：
进入代码本地仓库根目录，右键运行git bash，输入 ./code_format.sh +指定文件夹 ，
如./code_format.sh examples/ble_central_and_peripheral/experimental/ble_app_hrs_rscs_relay/src/framework/device_data/

3.不想格式化的文件夹如芯片的SDK源文件，放到pre-commit.gitignore文件里头。

4.参考
https://ydwiki.dding.net/pages/viewpage.action?pageId=30446900#space-menu-link-content
