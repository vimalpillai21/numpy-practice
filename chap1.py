import threading,time

def write_to_file():
    """Writing data to a file"""
    f = open('sample.txt','w+')
    try:
        line_list = ['Hello World\n','This is threading tutorial\n','current Thread\n']
        f.writelines(line_list)
        f.write("Hello I am Vimal")
        time.sleep(5)
        f.write("Hello I")
        f.close()
    except IOError as e:
        print(f"Exception occured while writing - {str(e)}")
    finally:
        f.close()

def read_data_from_file():
    """reading file and dispalying the data"""
    f = open('sample.txt','rt+')
    try:
        lines_list = f.readlines()
        # for line in lines_list:
        #     print(line)
        return lines_list
    except Exception as e:
        print(str(e))
        return None

s = threading.Thread(target=write_to_file,kwargs={},daemon=True)
s.start()
# s.join()
r = threading.Thread(target=read_data_from_file,kwargs={}, daemon=True).start()
