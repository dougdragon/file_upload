from ftplib import FTP

username = 'username'
passwd = 'password'
dir_loc = 'directory_of_ftp'
file_name = 'filename_to_upload'


def main():
    session = FTP(dir_loc)
    session.login(username, passwd)
    session.cwd(dir_loc)
    file = open(file_name, 'rb')
    try:
        session.storbinary('STOR {}'.format(file_name), file)
        print("\n\n------> {} uploaded.".format(file_name))
    except:
        print("Something went wrong")
    finally:
        file.close()
        session.quit()
        print("\n\nAll done!\n")

if __name__ == "__main__":
    main()
