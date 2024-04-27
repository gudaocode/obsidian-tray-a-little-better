# obsidian-tray-a-little-better
Attempting to resolve the issue where, after enabling the [obsidian-tray plugin](https://github.com/dragonwocky/obsidian-tray), clicking on URL links from outside of Obsidian does not wake up the Obsidian window.
Limited to the Windows system.

解决[obsidian-tray插件](https://github.com/dragonwocky/obsidian-tray)启用后，从Obsidian外点击url链接时，无法唤醒Obsidian窗口的问题。
限Windows系统

---

How to use
1. Save the "myobsidian.exe" file wherever you prefer.
2. Right-click on "Register MyObsidian.reg" and select "Edit".
3. Modify the last line ""path\myobsidian.exe" "%1"" to the location where you saved myobsidian.exe, using "\" for paths.
4. Double-click "Register MyObsidian.reg" to add it to the registry.
5. Done! Try it out. Prefix Obsidian links with "my", e.g., the original obsidian://advanced-uri?vault=Obsidian&uid=690e32dd-fac6-4b41-a154-9810ddb045d9 becomes "myobsidian://advanced-uri?vault=Obsidian&uid=690e32dd-fac6-4b41-a154-9810ddb045d9".

使用方法
1. 将“myobsidian.exe”文件保存到您希望的地方。
2. 右键点击“Register MyObsidian.reg”，选择“编辑”。
3. 修改最后一行""path\myobsidian.exe" "%1""中“path\myobsidian.exe\”，把它改为您保存myobsidian.exe的位置，路径中“\”使用“\”。
4. 双击“Register MyObsidian.reg”，添加进注册表。
5. OK！可以使用了，试试吧。在Obsidian链接前面加上“my”，即：原本的obsidian://advanced-uri?vault=Obsidian&uid=690e32dd-fac6-4b41-a154-9810ddb045d9，改为“myobsidian://advanced-uri?vault=Obsidian&uid=690e32dd-fac6-4b41-a154-9810ddb045d9”。

---

Preconditions to note
1. Windows system.
2. The tray plugin's wake-up window shortcut is set to Ctrl+Shift+B; if not, you can manually modify the Python file and compile it yourself.

前提:
1. windows系统。
2. tray插件设置的唤醒窗口快捷键为Ctrl+Shift+B，若不是，可以手动修改Python文件，并自己编译。

---

Principle
Quite simple (because I wouldn't know how to handle complex...):

In the Windows system, register the "myobsidian://" link in the registry to be opened with our exe.
Our exe does two things:
Extracts the myobsidian:// link, replaces it with obsidian://, and opens it in Obsidian.
Inputs the shortcut to wake up the Obsidian window.

原理
很简单（因为复杂的我就不会弄了……）

在win系统中注册表注册“myobsidian://”的链接，这种链接用我们的exe打开。
我们的exe做两件事：
提取myobsidian://链接，替换为obsidian://的，在Obsidian中打开。
输入快捷键，唤醒Obsidian窗口。

---

Source code provided
1. The Python code needs corresponding libraries (for invoking shortcuts):
pip install pynput

2. You can compile using Python's own, but it will be slightly slower: pyinstaller --noconsole --onefile myobsidian.py

Or use nuitka, which is a bit smaller in size and slightly faster (the provided version is this one):
pip install nuitka
python -m nuitka --onefile --windows-disable-console --output-dir=build myobsidian.py
This generates a build folder, and the exe is in this directory.

源码附上
1. py代码需要装对应的库（用于调用快捷键）：
pip install pynput

2. 编译时用Python自带的也可以，但运行速度会略慢：pyinstaller --noconsole --onefile myobsidian.py

也可以用nuitka，体积小了一点点，速度略快（前面提供的是这个版本）：
pip install nuitka
python -m nuitka --onefile --windows-disable-console --output-dir=build myobsidian.py
生成build文件夹，exe在这个目录下。
