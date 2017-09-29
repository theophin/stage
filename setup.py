from cx_Freeze import setup,Executable

#Permet de creer lexecutable il suffit dexecuter en ecrivant "setup.py build" dans le cmd
setup(
	name="Main",
	version="0.1",
	description ="conversion csv commtrade",
	executables=[Executable("Main.py")],
	)