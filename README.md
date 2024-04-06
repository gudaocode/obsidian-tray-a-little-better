# obsidian-tray-a-little-better
尝试解决[obsidian-tray插件](https://github.com/dragonwocky/obsidian-tray)启用后，从Obsidian外点击url链接时，无法唤醒Obsidian窗口的问题。
限Windows系统

## 使用方法
1.将“myobsidian.exe”文件保存到您希望的地方

2. 右键点击“Register MyObsidian.reg”，选择“编辑”
3. 修改最后一行"\"path\\myobsidian.exe\" \"%1\""中“path\\myobsidian.exe\”，把它改为您保存myobsidian.exe的位置，路径中“\”使用“\\”
4. 双击“Register MyObsidian.reg”，添加进注册表
5. OK！可以使用了，试试吧。在Obsidian链接前面加上“my”，即：原本的obsidian://advanced-uri?vault=Obsidian&uid=690e32dd-fac6-4b41-a154-9810ddb045d9，改为“myobsidian://advanced-uri?vault=Obsidian&uid=690e32dd-fac6-4b41-a154-9810ddb045d9”

## 注意的前提
1. windows系统
2. tray插件设置的唤醒窗口快捷键为Ctrl+Shift+B，若不是，可以手动修改Python文件，并自己编译

## 原理
很简单（因为复杂的我就不会弄了……）
1、win系统中注册表注册“myobsidian://”的链接，这种链接用我们的exe打开
2、我们的exe做两件事：
  1. 提取myobsidian://链接，替换为obsidian://的，在Obsidian中打开
  2. 输入快捷键，唤醒Obsidian窗口

## 源码附上
1.编译时用Python自带的也可以，但运行速度会略慢：pyinstaller --noconsole --onefile myobsidian.py

2.也可以用nuitka，体积小了一点点，速度略快（前面提供的是这个版本）：
pip install nuitka
python -m nuitka --onefile --windows-disable-console --output-dir=build myobsidian.py
生成build文件夹，exe在这个目录下
