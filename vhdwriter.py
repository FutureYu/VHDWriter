import os
import sys

def Run(sector, inputfile, outputfile):
    # 判断文件存在
    if not os.path.exists(inputfile):
        print("\033[31m [fatal error] 二进制文件不存在 \033[0m")
        sys.exit(1)
    if not os.path.exists(outputfile):
        print("\033[31m [fatal error] vhd 文件不存在 \033[0m")
        sys.exit(1)

    with open(inputfile, "rb") as f:
        inputbyte = f.read()
    with open(outputfile, "rb") as f2:
        outputbyte = bytearray(f2.read())

    # 判断扇区号存在
    if len(outputbyte) - 512 < sector * 512 + len(inputbyte):
        print("")
        print("\033[31m [fatal error] 扇区号超过磁盘大小 \033[0m")

        sys.exit(1)

    # 写入
    outputbyte[sector * 512:sector * 512 + len(inputbyte)] = inputbyte

    try:
        with open(outputfile, "wb") as f:
            f.write(outputbyte)
            print(f" 写入成功，在 {outputfile} 的 {sector} 扇区写入了 {(len(inputbyte) + 511) // 512} 扇区 ")
    except:
        print("\033[31m [fatal error] 文件被占用，请关闭虚拟机 \033[0m")

def main(argv):
    # 读取参数
    if len(argv) != 3:
        print(" 版权所有 FutureYu 2019")
        print(" 使用方法:")
        print(" use 'vhdwriter (.exe) < 扇区号 > < 二进制文件 > <vhd 文件 >'")
        print(" 例如 vhdwriter (.exe) 0 'loader.bin' 'exp.vhd'")
        print(" 添加环境变量可不输入 .exe ")
        print(" 如路径中含有空格，请使用引号 ")
        print(" 仅可写入固定大小的虚拟磁盘文件，否则后果自负 ")
    else:
        try: 
            sector = int(argv[0])
        except:
            print("\033[31m [fatal error] 参数 1 扇区号错误 \033[0m")

        Run(sector, argv[1], argv[2])


if __name__ == "__main__":
    main(sys.argv[1:])
