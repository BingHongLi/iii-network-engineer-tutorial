docker run -d -p 8888:8888 --name iii-tutorial -v $(pwd)/tutorial:/home/jovyan/ jupyter/base-notebook start-notebook.sh --NotebookApp.token=''
