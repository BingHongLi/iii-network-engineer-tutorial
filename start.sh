docker run -d -p 5000:5000 -p 8888:8888 --name iii-tutorial -v $(pwd)/tutorial:/home/jovyan/ jupyter/base-notebook start-notebook.sh --NotebookApp.token=''
