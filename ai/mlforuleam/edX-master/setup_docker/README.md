In order to simplify the setup of a common environment for all students on any Operating System, we recommend to run Python using `Docker`. Thanks to `Docker`, you can access the Jupyter Notebook and all of the Python Data Science stack without installing any library on your computer. Just install `Docker` and then download a **container** that packages up all the required libraries and use your browser to connect to the Jupyter Notebook running inside this container.

# 1) Install Docker

You will need the Administrator password on Windows or `sudo` permissions on Linux to install Docker.

## Windows 10

Docker requires 64bit Windows 10 Pro, Enterprise and Education (1511 November update, Build 10586 or later)
Follow instructions on the Docker official website at https://docs.docker.com/docker-for-windows/install/

* Choose the `Stable` version
* Download and install the package
* At the prompt to enable `Hyper-V`, choose `Ok` and reboot your system.
* If your machine does not support `Hyper-V`, Docker for Windows will install `Virtualbox`

## Windows 7 and 8

Docker maintains also the `Docker toolbox`, a legacy system that works on 64bit Windows 7 and 8, follow the instructions here:

<https://docs.docker.com/toolbox/toolbox_install_windows/>

## Mac

Docker for Mac has substantial system requirements, check on the **System requirements** section on this page to check if your machine is supported:

<https://docs.docker.com/docker-for-mac/install/>

* Choose the `Stable` version

If you have an older system, install `Docker Toolbox for Mac` from <https://docs.docker.com/toolbox/toolbox_install_mac/>

## Linux

Check if your distribution is supported on the Docker official website:

https://docs.docker.com/engine/installation/linux/

Then follow the instructions to install the **Community Edition (CE)** and choose the `stable` channel.

# 2) Open a terminal

* On Linux open a Terminal application, type `cd` and enter to make sure you are in your home folder
* On a newer Mac with Docker for Mac, ?
* On an older Mac with Docker Toolbox for Mac, open the `Docker Quickstart Terminal`
* If you installed Docker for Windows in Windows 10, open Microsoft Powershell or the Command Prompt (search within the Windows applications)
* If you installed Docker Toolbox for Windows, open the `Docker Quickstart Terminal`

# 3) Install and run the Scientific Python docker container

## Create a folder on your machine to preserve your work

In this section we will create a folder named `Python4DS` in your home folder. This folder will be available within the container so that you can save your work back to your host Operative System.

Open a terminal (see section 2), type `mkdir Python4DS` to create a new folder inside your home folder.

Just in Docker for Windows 10, you need to open the Settings (right click on the system tray icon and choose Settings), click on the `Shared Drives` tab and check the checkbox Shared for the `C` drive. For this setting Docker might require your password. Remember to click `Apply` once you modified this setting.

## Launch the container for the first time

If you are installing Docker on your personal laptop or desktop, you can run (possibly add `sudo` at the beginning for Linux): 

    docker run -d -p 8888:8888 --name python4ds -v /c/Users/yourusername/Python4DS:/home/jovyan/work jupyter/scipy-notebook start-notebook.sh --NotebookApp.token='' 
    
Instead of `/your/home/folder/Python4DS`, use the full path to the folder you created above, generally it will be `/home/yourusername/Python4DS` on Linux, `/Users/yourusername/Python4DS` on Mac and `/c/Users/yourusername/Python4DS` on Windows. This will be mounted in the containter at the location `/home/jovyan/work` which is the starting folder of Jupyter Notebook.

If you cannot copy-paste the command into the Terminal on Windows, right-click with the mouse on the window title and choose Edit then Paste from the menu.
    
Instead if you are using a shared system, launch the same command but remove the keyword `--NotebookApp.token=''`, the Notebook will provide an authentication token to prevent other users from connecting to your Notebook.

Just for the first time, Docker will have to download all of the layers of the filesystem of the containter (~2GB) and will require 20 or more minutes, depending on the speed of your internet connection and performance of your machine.

After the first execution, the startup will be quick and won't require internet connection.

For more configuration options of the container, see [its homepage on Github](https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook).

## Find the address of the running container

* On Linux and on Docker for Windows (Windows 10) with Hyper-v enabled (see section 1), the address is always `localhost`.
* On Docker for Windows (Windows 10) with VirtualBox, open a terminal, type `ipconfig` and look for a `VirtualBox Host-Only adapter` and look for its `IPv4 Address`, it should generally be `192.168.56.1`.
* On Docker Toolbox for Mac or Windows (Windows 7 or later), open a terminal and type `docker-machine ip default` (generally `192.168.99.100`), this address should also be displayed at the launch of the `Docker Quickstart Terminal`

## Access the Jupyter Notebook

* Open a browser on your local machine (Chrome recommended, but any browser should work)
* Type `http://container_address:8888` on your browser bar, e.g. `http://192.168.99.100:8888` or `http://localhost:8888`
* You should now visualize the Jupyter Notebook dashboard, in particular you should see the content of the `Python4DS` folder, possibly empty.

## Stop the execution of the container

From the terminal, type `docker ps` to check the running containters, then `docker stop python4ds` to stop the execution of the container.

## Launch the container again

Now that the container has already been created, you can launch it with:

    docker start python4ds
    
# 4) Troubleshooting

## Wipe and create again the container

If you have a configuration issue in the container you can delete with:

    docker rm -f python4ds
    
then follow the instructions in "Launch the container for the first time" to create it again.

## Certificate issue on Windows 7/8

Docker might give the warning:

    Unable to use system certificate pool: crypto/x509: system root pool is not available on Windows
    
This does not impact the functionality of Docker, eveything should work as expected.

## Connection failed on Windows 10

If after installation Docker for Windows gives this error:

```
Error response from daemon: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.

at Docker.Backend.DockerDaemonChecker.Check(Func`1 isDaemonProcessStillRunning)
at Docker.Backend.ContainerEngine.Linux.DoStart(Settings settings)
at Docker.Backend.ContainerEngine.Linux.Start(Settings settings)
at Docker.Core.Pipe.NamedPipeServer.<>c__DisplayClass8_0.b__0(Object[] parameters)
at Docker.Core.Pipe.NamedPipeServer.RunAction(String action, Object[] parameters)
```
Right click on the Docker system tray icon, open Settings, Reset, click on `Restart Docker`

## Not enough memory to start Docker

In machines with 4GB of RAM or less, on Windows 10 with Docker for Windows, Docker might not be able to start.
Right click on the Docker system tray icon, open Settings, in the tab named Advanced you can choose the amount of resources dedicated to docker, reduce memory to 1.5 GB or even 1 GB.
