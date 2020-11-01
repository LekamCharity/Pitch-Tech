from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProf(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')

class IdeaForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    category = SelectField('Category',choices=[('Interview','Interview'),('Events','Events'),('Job','Job')],validators=[Required()])
    post = TextAreaField('Any comment..',validators=[Required()])
    submit = SubmitField('Your Opinion')

class CommentForm(FlaskForm):
    comment = TextAreaField('Type a comment',validators=[Required()])
    submit = SubmitField('Comment')
    