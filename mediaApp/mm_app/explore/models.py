
from mediaApp.mm_app import db


class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(80), nullable=False)
    preview_url = db.Column(db.String(80), nullable=False)
    thumbnail_url = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    runtime = db.Column(db.String(80), nullable=False)
    resolution = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return (f"Video('{self.file_name}', '{self.preview_url}', '{self.thumbnail_url}', "
                f"'{self.description}', '{self.runtime}', '{self.resolution}')")


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(80), nullable=False)
    category_preview_url = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Tag('{self.category_name}', '{self.category_preview_url}')"


class VideoCategory(db.Model):
    video_category_id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"videoTag('{self.video_id}', '{self.tag_id}')"


# class Tag(db.Model):
#     tag_id = db.Column(db.Integer, primary_key=True)
#     tag_name = db.Column(db.String(80), nullable=False)
#
#     def __repr__(self):
#         return f"Tag('{self.tag_name}')"
#
#
# class videoTag(db.Model):
#     video_tag_id = db.Column(db.Integer, primary_key=True)
#     video_id = db.Column(db.String(80), nullable=False)
#     tag_id = db.Column(db.String(80), nullable=False)
#
#     def __repr__(self):
#         return f"videoTag('{self.video_id}', '{self.tag_id}')"


