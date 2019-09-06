import subprocess

# test1
print('Running test for level1')
subprocess.os.chdir('level1')
subprocess.run('python -m unittest test_main', shell=True)

# test2
print('Running test for level2')
subprocess.os.chdir('../level2')
subprocess.run('python -m unittest test_main', shell=True)

# test3
print('Running test for level3')
subprocess.os.chdir('../level3')
subprocess.run('python -m unittest test_main', shell=True)


# test4
print('Running test for level4')
subprocess.os.chdir('../level4')
subprocess.run('python -m unittest test_main', shell=True)


# test5
print('Running test for level5')
subprocess.os.chdir('../level5')
subprocess.run('python -m unittest test_main', shell=True)
