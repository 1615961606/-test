-----------2018年4月3日--------------
注意：请使用sublime打开本文本 按alt+m快捷键，就会自动启动浏览器，请在浏览器中看
http://wowubuntu.com/markdown/#precode  我们使用sublime text 3进行markdown的编写，链接为markdwon语法教程链接，花5-10分钟即可以学会这种
专门用于编辑的博文的语法
-----------------------------------------

####北京财经专修学院 人工智能专业 Ubuntu系统优化和定制软件包 2018年4月3日基础beta版本
致力于打造``开箱即用``的``好用的``Linux系统
#### 如有bug可以发邮件至wengwenyu888@aliyun.com
#安装：
## 1、安装了搜狗输入法
## 2、安装了vim
## 3、安装了git
## 4、安装Python3的包管理软件pip3
## 5、安装了ipython3
## 6、安装了终端目录查看插件tree
## 7、安装了sublime text3
## 8、安装了谷歌浏览器
## 9、安装了stacer主要有如下功能，虽说诸多功能我们可以通过命令操作，但是有了stacer也可以让你得心应手：
####1、快速浏览系统资源（如内存、CPU)
####2、释放空间(可以清理5种类型达到释放空间的目的，如APT 系统日志缓存 回收站等等）
####3、管理启动应用程序（启动应用程序对系统的启动时间具有很大影响，启动应用越多，加载时间越长）
####4、管理服务（可以让你搜索到当前Linux系统中的可用系统服务，在此可将其切换为启用或者禁用）
####5、查看和管理进程（top或者htop功能类似）
####6、查看和移除软件（其实Ubuntu自带软件商店也有这个功能）
####7、资源查看器 （查看当前操作系统的CPU网络和内存相关的资源利用动态情况）
####8、应用设置 （对stacer设置皮肤，可惜没有中文界面）
###10、安装了pycharm集成开发环境
###11、安装了htop htop相关使用教程（Linux下强大的监控软件）
链接1：http://www.open-open.com/lib/view/open1417612210323.html
链接2：http://www.cnblogs.com/lizhenghn/p/3728610.html
#优化：
##1、安装了virtualbox增强插件
##2、将所有软件和依赖文件更新到最新版本
##3、切换镜像源为阿里云镜像源
##4、卸载了笨重而又古老的火狐浏览器（如果需要，可以sudo apt install firefox自行下载）
##5、卸载了libreoffice
##6、删除了amazon链接
##7、删除基本不用自带的软件（到时候装也来得及）
##8、安装了mysql5.7版本
##9、安装了pymysql
##10、升级了Python-pip3版本
##11、安装了unity-tweak-tool系统美化设置工具
##12、安装了Ubuntu下扁平化主题Flatabulous和配套图标
##13、配置了sublime text 3(之后简称ST3)如下内容：
####1、解决了中文输入法无法输入问题
####2、安装了ST3的包管理工具
####3、搭建了Python的开发环境，主要是anaconda插件，已配置好默认路径和用户路径相关内容
####4、设置好了Python3的编译环境
####5、配置好了ST3中文
####6、安装了Emmet插件
####7、安装了autofilename插件
####8、安装了HTML-CSS-JS格式化插件
####9、安装了javascript-api插件
####10、安装了Jquery插件
####11、安装了菜单栏增强插件
####12、安装了markdown预览插件(并且设置了快捷键alt+m)
##14、安装了``高逼格``zsh和oh-my-zsh

#vim做了如下配置，配置信息没有放在/etc目录下，而放在家目录下隐藏文件（.vimrc)：
#补充说明：本Ubuntu虚拟机包作者计划下一版本完善 VIM-Python IDE  和 前端IDE 以及emacs的全套配置以满足不同人的开发需求
vim教程链接推荐：http://www.runoob.com/linux/linux-vim.html
syntax on " 自动语法高亮  
set number " 显示行号  
set cursorline " 突出显示当前行  
set ruler " 打开状态栏标尺  
set shiftwidth=4 " 设定 << 和 >> 命令移动时的宽度为 4  
set softtabstop=4 " 使得按退格键时可以一次删掉 4 个空格  
set tabstop=4 " 设定 tab 长度为 4  
set nobackup " 覆盖文件时不备份  
set autochdir " 自动切换当前目录为当前文件所在的目录  
filetype plugin indent on " 开启插件  
set backupcopy=yes " 设置备份时的行为为覆盖  
set ignorecase smartcase " 搜索时忽略大小写，但在有一个或以上大写字母时仍保持对大小写敏感  
set nowrapscan " 禁止在搜索到文件两端时重新搜索  
set incsearch " 输入搜索内容时就显示搜索结果  
set hlsearch " 搜索时高亮显示被找到的文本  
set noerrorbells " 关闭错误信息响铃  
set novisualbell " 关闭使用可视响铃代替呼叫  
set t_vb= " 置空错误铃声的终端代码  
set showmatch " 插入括号时，短暂地跳转到匹配的对应括号  
set matchtime=2 " 短暂跳转到匹配括号的时间  
set magic " 设置魔术  
set hidden " 允许在有未保存的修改时切换缓冲区，此时的修改由 vim 负责保存  
set guioptions-=T " 隐藏工具栏  
set guioptions-=m " 隐藏菜单栏  
set smartindent " 开启新行时使用智能自动缩进  
set backspace=indent,eol,start  
" 不设定在插入状态无法用退格键和 Delete 键删除回车符  
set cmdheight=1 " 设定命令行的行数为 1  
set laststatus=2 " 显示状态栏 (默认值为 1, 无法显示状态栏)  
set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %c:%l/%L%)\  
" 设置在状态行显示的信息  
set foldenable " 开始折叠  
set foldmethod=syntax " 设置语法折叠  
set foldcolumn=0 " 设置折叠区域的宽度  
setlocal foldlevel=1 " 设置折叠层数为  
set foldclose=all " 设置为自动关闭折叠  
