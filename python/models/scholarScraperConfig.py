from selenium import webdriver

class ScholarScraperConfig:
    def __init__(
        self,
        is_verbose: bool = False,
        headless: bool = False,
        proxy: str = None,
        no_sandbox: bool = True,
        disable_dev_shm: bool = True,
        disable_gpu: bool = True,
        disable_software_rasterizer: bool = True,
        remote_allow_origins: bool = True,
        extra_args: list = None,
    ):
        self._is_verbose = is_verbose
        self._headless = headless
        self._proxy = proxy
        self._no_sandbox = no_sandbox
        self._disable_dev_shm = disable_dev_shm
        self._disable_gpu = disable_gpu
        self._disable_software_rasterizer = disable_software_rasterizer
        self._remote_allow_origins = remote_allow_origins
        self._extra_args = extra_args or []

    # Setter
    def is_verbose(self) -> bool:
        return self._is_verbose

    def set_verbosity(self, is_verbose: bool):
        self._is_verbose = is_verbose

    # Getter
    def is_headless(self) -> bool:
        return self._headless

    def get_proxy(self) -> str:
        return self._proxy

    def use_no_sandbox(self) -> bool:
        return self._no_sandbox

    def disable_dev_shm(self) -> bool:
        return self._disable_dev_shm

    def disable_gpu(self) -> bool:
        return self._disable_gpu

    def disable_software_rasterizer(self) -> bool:
        return self._disable_software_rasterizer

    def allow_remote_origins(self) -> bool:
        return self._remote_allow_origins

    def get_extra_args(self) -> str:
        return self._extra_args

    # WebDriver
    def set_headless(self, value: bool):
        self._headless = value

    def set_proxy(self, proxy: str):
        self._proxy = proxy

    def add_extra_arg(self, arg: str):
        if arg not in self._extra_args:
            self._extra_args.append(arg)

    def remove_extra_arg(self, arg: str):
        if arg in self._extra_args:
            self._extra_args.remove(arg)
            
    def apply_to_chrome_options(self) -> webdriver.ChromeOptions:
        options = webdriver.ChromeOptions()

        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36")

        if self._headless:
            options.add_argument("--headless=new")
        if self._no_sandbox:
            options.add_argument("--no-sandbox")
        if self._disable_dev_shm:
            options.add_argument("--disable-dev-shm-usage")
        if self._disable_gpu:
            options.add_argument("--disable-gpu")
        if self._disable_software_rasterizer:
            options.add_argument("--disable-software-rasterizer")
        if self._remote_allow_origins:
            options.add_argument("--remote-allow-origins=*")
        if self._proxy:
            options.add_argument(f"--proxy-server={self.proxy}")

        for arg in self._extra_args:
            options.add_argument(arg)

        return options

    # String representation
    def __repr__(self) -> str:
        return (
            f"ScholarScraperConfig("
            f"is_verbose={self._is_verbose}, "
            f"headless={self._headless}, "
            f"proxy={self._proxy}, "
            f"no_sandbox={self._no_sandbox}, "
            f"disable_dev_shm={self._disable_dev_shm}, "
            f"disable_gpu={self._disable_gpu}, "
            f"disable_software_rasterizer={self._disable_software_rasterizer}, "
            f"remote_allow_origins={self._remote_allow_origins}, "
            f"extra_args={self._extra_args}"
            f")"
        )
