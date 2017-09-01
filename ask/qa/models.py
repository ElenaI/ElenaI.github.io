# Create your models here.
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add =  True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User,related_name = 'quest_set')
    likes = models.ManyToManyField(User,related_name = 'likes_set')
    class Meta:
        db_table = 'question'
class QuestionManager(models.Manager):
    def new():
        self.order_by('-added_at')
    def popular():
        self.order_by('-rating')



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add =  True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User,related_name = 'ans_set')
    class Meta:
        db_table = 'answer'
