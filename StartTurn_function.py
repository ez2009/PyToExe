def StartTurn():
    msgbox("开始打包，请耐心等待", "提示")
    if file != "0":
        run_file = os.getcwd()
        shutil.copy(file, run_file)
        basename = os.path.basename(file)
        name = "pyinstaller -F -w ", basename
        system = "".join(name)
        os.system(str(system))
        delete_filename = run_file + '\\' + os.path.basename(file)
        delete_file = ''.join(delete_filename)
        os.remove(delete_file)
        show_text = "打包完成！请到路径", run_file, "里的 dist文件夹查看，有导入素材的文件要把exe程序移动回原文件夹才可使用！"
        msgbox(show_text, "提示")
    else:
        msgbox("文件路径为空，请重新选择文件！", "警告")