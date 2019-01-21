from django import forms

from blog_back.models import User


class StuForm(forms.Form):
    username = forms.CharField(max_length=10,
                               min_length=2,
                               required=True,
                               error_messages={
                                   'required': '姓名必填',
                                   'min_length': '不能少于2个字符',
                                   'max_length': '不能多于10个字符'
                               })

    gender = forms.CharField(required=True, error_messages={
        'required': '性别不能为空'})

    userkname = forms.CharField(max_length=10,
                                min_length=2,
                                required=True,
                                error_messages={
                                    'required': '昵称必填',
                                    'min_length': '不能少于2个字符',
                                    'max_length': '不能多于10个字符'
                                })
    userage = forms.IntegerField(max_value=255,
                                 min_value=0,
                                 error_messages={
                                     'max_value': '请输入正确的年龄',
                                     'min_value': '请输入正确的年龄'
                                 })
    password1 = forms.CharField(required=True,
                                error_messages=
                                {'required': '密码不能为空'})

    password2 = forms.CharField(required=True,
                                error_messages=
                                {'required': '密码不能为空'})

    # 重新定义校验方法
    def clean(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        # 如果数据库中存在就直接抛出异常raise并定义error_messages为姓名重复
        if user:
            raise forms.ValidationError({'username': '姓名重复'})

        gender = self.cleaned_data.get('gender')
        if gender == '男':
            self.cleaned_data['gender'] = 1
        else:
            self.cleaned_data['gender'] = 0

        password1 =self.cleaned_data.get('password1')
        password2 =self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError({'password2': '两次密码不一致'})
