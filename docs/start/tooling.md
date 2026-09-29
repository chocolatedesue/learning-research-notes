> 出处：[原文链接](https://pengsida.notion.site/59569d7b66954578b21bf1dc6ea35776)

## 设备配置

## 一 shell的配置
采用zsh作为默认的shell十分好用
首先是oh my zsh这一zsh管理工具的安装：
[https://github.com/ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
然后是插件的安装
1.设备之间复制shell的配置：[https://github.com/rutchkiwi/copyzshell](https://github.com/rutchkiwi/copyzshell)
2.命令高亮以及命令语法检测（必装）：[https://github.com/zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
3.自动补全auto suggestion（必装）：[https://zhuanlan.zhihu.com/p/111707433](https://zhuanlan.zhihu.com/p/111707433)
补全如果出现了想要的语句，则直接ctrl+f选择
如果需要显示所有可选项目，点击一次tab只能显示所有可选项但还是需要手动输入；点击两次tab可以直接用方向键选择项目
1. fzf 配合 history (必装）
手动切换默认shell：
```Shell
cat /etc/shells  #查看所有shell

echo $SHELL      #查看当前使用的shell

chsh -s /usr/bin/zsh  #更改默认shellOx
```
如果需要密码来修改默认shell，不知道密码的话比较好的办法是：
在~/.bashrc的最后加上zsh这句话，这样就直接启动zsh了，并且在启动后会执行一次~/.zshrc
### 一些常用的工具：
ncdu： apt-get install ncdu，查看文件夹占用
nvtop, 如果装不上就用nvitop（github安装到python环境中）
fzf： ‣ 其中还有一些使用说明
ctop：监控每个docker 容器的资源使用情况（需要sudo）
tmux：如下
vim：如下
### tmux配置：
tmux中添加鼠标:
对于已经有一份oh my zsh配置的机器，如果有新的机器需要配置，在有zsh的情况下不用重新执行下面的几步(不要安装oh my zsh，直接传就可以了，安装了的话无法直接覆盖会比较麻烦！），而是直接传送就可以了，如果需要添加机器的port，参考issue
*注意：用里面oh my zsh的安装方式，方便迁移
```Python
touch ~/.tmux.conf
echo "set -g mouse on" >> ~/.tmux.conf 

#如果上面的不行就先在~/.tmux.conf中添加：
setw -g mode-mouse on
setw- g mouse-resize-pane
setw -g mouse-select-pane
setw -g mouse-select-window
set-option -g history-limit 5000

#然后
tmux source-file ~/.tmux.conf
```
tmux中好用的综合配置（强烈建议安装）:
[https://github.com/samoshkin/tmux-config](https://github.com/samoshkin/tmux-config)
需要tmux版本大于2.4，查看版本:tmux -V
发现2.1也可以
注意依然需要 tmux souce-file xx
如果有syntex error,参考下面的
[https://github.com/samoshkin/tmux-config/issues/38](https://github.com/samoshkin/tmux-config/issues/38)
### vim配置：
[https://github.com/amix/vimrc](https://github.com/amix/vimrc)
ssh-keygen -t rsa
```Python
vim ~/.vimrc
set nu   # 在vimrc文件中添加set nu打开显示行
let g:snipMate = { 'snippet_version' : 1 } # 在vimrc文件最后加上防止一打开vim就报xxdecrepit
```
给vim添加file tree：
[https://github.com/preservim/nerdtree](https://github.com/preservim/nerdtree)
然后：
添加NERDTree的自动打开与关闭：
[https://riptutorial.com/vim/example/30660/nerd-tree](https://riptutorial.com/vim/example/30660/nerd-tree)
如果要将打开后的cursor放在当前文件下，那么就用这个指令而不是链接里面的那个 
```Python
# Start NERDTree and put the cursor back in the other window.
autocmd VimEnter * NERDTree | wincmd p
```
## 二 anaconda/miniconda下载与配置
anaconda：
```Shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.10-Linux-x86_64.sh
```
如果这个太慢了就用miniconda：
[https://repo.anaconda.com/miniconda/](https://repo.anaconda.com/miniconda/)
```Python
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh
```
在这里找到想要的版本将anaconda的路径换成想要的就好了
安装与刷新：
```Shell
zsh Anaconda3-2019.10-Linux-x86_64.sh

source ~/.zshrc
```
名称换成下载好的文件名称
如果发现这样之后conda找不到指令，那就是安装到bashrc下了，vi ~/.bashrc下找到所有的复制到~/.zshrc，然后再source
### 2.1 conda环境配置指令
[https://blog.csdn.net/hejp_123/article/details/92151293](https://blog.csdn.net/hejp_123/article/details/92151293)
创建新环境：
```Shell
conda create --name your_env_name python=3.6
```
通过yaml创建新环境：
```Python
conda env create -f filepath.yaml
```
删除环境：
```Shell
conda remove -n your_env_name --all

conda remove --name your_env_name --all
```
使用国内conda软件源进行加速：
```Shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```
使用公司conda源加速：
[https://dx-mirrors.sensetime.com/help/use-conda-mirror.html](https://dx-mirrors.sensetime.com/help/use-conda-mirror.html)
### 2.2 pip指定源
```Shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorboard
```
**注意检查一下使用的pip是否是当前conda environment下的：
```Python
which pip 
# if not(经常会掉）
conda deactivate
conda activate
which pip
```
如果pip是通过conda 装的那么pip和conda就是通的，可以相互找到对方装的包。
```Python
# update package
pip install -U name
```
使用国内pip软件源加速：
```Shell
1.临时设置方法：

可以在使用pip的时候加在最后面加上参数 -i https://pypi.tuna.tsinghua.edu.cn/simple

例如：pip install jieba -i https://pypi.tuna.tsinghua.edu.cn/simple  # jieba 是一个包

2.永久设置方法：

pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

配置完之后就可以像平常一样安装包，速度提升几十倍

例如：pip install jieba

切换为阿里云进行下载

pip install pandas -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
pip install pandas -i http://mirrors.aliyun.com/pypi/simple/


阿里云 http://mirrors.aliyun.com/pypi/simple/
豆瓣(douban) http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```
## 三 cuda版本的选择：
选择cuda版本，在~/.zshrc中配置如下：
如果nvcc -V 失败，则同样需要添加如下：
```Shell
export CUDA_VER=版本号（例如：9.0）

export PATH=/usr/local/cuda-$CUDA_VER/bin:$PATH

export LD_LIBRARY_PATH=/usr/local/cuda-$CUDA_VER/lib64:$LD_LIBRARY_PATH
```
下面的路径以实际的cuda位置为准
最后source ~/.zshrc启用
cuda版本的对应问题：
pytorch的版本、cudatoolkit的版本、系统使用的cuda版本三者大版本需要对应
```Shell
python -c "import torch; print(torch.version.cuda)”    #查看pytorch的版本

conda list | grep cudatoolkit                          #查看cudatoolkit版本

cacdt /path_to_cuda_your_using/version.txt               #查看系统使用的cuda版本，路径还得看~/.zshrc

或者用：nvcc --version                                  #查看系统使用的cuda版本
```
注意：在上述三者对应的情况下，如果gpu driver的版本与cuda版本不对应的话会导致cuda无法使用。检查cuda是否可用：
```Python
import torch
print(torch.cuda.is_available())
```
## 四 服务器免密登陆
通过ssh秘钥的方式，将本机的id_rsa.pub文件中的秘钥拷贝到目标服务器.ssh/中的authorized_keys文件中。如果这个文件不存在则新建一个，将本地的id_rsa.pub cat进去
如果出问题则可能是文件夹权限不对：
[https://serverfault.com/questions/525045/ssh-connection-asks-for-password-although-key-is-accepted](https://serverfault.com/questions/525045/ssh-connection-asks-for-password-although-key-is-accepted)
```Shell
chmod 755 ~/.ssh                  #修改.ssh目录权限755
```
或者是copy错误，建议现将本机的id_rsa.pub rsync到目标机器，然后：
```Python
cat temp.pub >> authorized_keys
```
