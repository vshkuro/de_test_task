# DE Test task
Project for creating a pandas DataFrame chunker.

## Installation notes
1. Clone repo:
    ```bash
    git clone https://github.com/vshkuro/de_test_task.git
    cd de_test_task
    ```
2. Run install command based on your OS (creates venv and installs dependencies)  
    - macOS/Linux:
        ```make install_lin```
    - Windows:
        ```make install_win```

## Usage notes
To run example use command:
```make example``` (it will use default values for chunk and dataframe sizes)

To set these parameters use following command:
```make example chunk=3 repeat=3```

To run tests use:
```make pytest```


> All commands info: ```make help```
