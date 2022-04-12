import pytest
import os
import logging
import shutil


def copyFolderRec(src_path:str,dest_path:str):
    try:
        if os.path.isdir(src_path) == True:
            logging.debug('path existed!')
            try:
                if os.path.isdir(dest_path):
                    logging.info('Destination Dir already existed!')
                else:
                    os.mkdir(dest_path)
                    # for item in os.listdir(src_path):
                    #     item_normal = os.path.join(src_path, item)
                    #     try:
                    #         if os.path.isfile(item_normal):
                    #             print(f'Copying file {item_normal} to {dest_path}')
                    #             shutil.copy(item_normal, dest_path)
                    #         if os.path.isdir(item_normal):
                    #             pass
                    #     except Exception as e:
                    #         logging.error(f'Can not copy file {item_normal}!')
                    #         return -4
            except Exception as e:
                logging.error('Can not create destination path!')
                return -3
        else:
            logging.error('Invalid path, please enter correct path!')
            return -2
    except Exception as e:
        logging.critical('Unexpected error encountered!')
        return -1
    return 0

def test_usecase1_test_callable_function():
    source = 'F:\\Githup repo\\test1'
    dest = 'f:\\test1'
    result = copyFolderRec(source,dest)
    assert result == 0

def test_usecase2_check_path():
    # 2. check if input path existed
    source = 'F:\\Githup repo\\test1'
    dest = 'f:\\test1'
    failed_path = 'f:\\test2'
    assert copyFolderRec(source, dest) == 0 and copyFolderRec(failed_path, dest) != 0

def test_usecase3_creating_a_folder_if_needed():
    # 3.try creating a folder if needed
    source = 'F:\\Githup repo\\test1'
    dest = 'f:\\test1'
    result = copyFolderRec(source, dest)
    assert os.path.isdir(dest) == True

def test_usecase4_try_copying_a_file():
    source = 'F:\\Githup repo\\test1'
    dest = 'f:\\test1'
    result = copyFolderRec(source,dest)
    assert sorted(os.listdir(dest)) == sorted(os.listdir(source))
