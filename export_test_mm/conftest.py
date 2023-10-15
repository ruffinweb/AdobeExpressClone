
import pytest
import shutil
from pathlib import Path
from mediaApp.mm_app import create_app, db
from mediaApp.mm_app.config import TestingConfig


@pytest.fixture()
def app():
    # app = create_app()
    app = create_app(config_class=TestingConfig, static_database_url="/sqlite:///")

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def temp_dir_fix():
    test_dir: str = "./sandbox/test_directory"
    temp_path = Path(test_dir)

    temp_path.mkdir(parents=True, exist_ok=True)
    (temp_path / 'video1.mp4').touch()
    (temp_path / 'video2.mov').touch()

    yield temp_path


# Creates a video file for each file type.
@pytest.fixture()
def sample_video_fix():
    video_exts = ['mp4', 'mov', 'mkv']
    test_dir: str = "./sandbox/test_directory"

    for video_file in Path(test_dir).iterdir():
        if video_file.suffix in video_exts:
            return True
        else:
            return False


# Real Videos are used here.
@pytest.fixture()
def sample_video_fix_real(test_dir: str = r"C:\Workspace\Sandbox\testVideoDir/aa.mp4"):
    temp_video = Path(test_dir)

    yield temp_video


@pytest.fixture()
def sample_videos_dir_fix_real(test_dir: str = r"C:\Workspace\Sandbox\testVideoDir"):
    temp_path = Path(test_dir)

    yield temp_path

