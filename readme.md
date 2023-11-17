Install react modules
1 - cd frontend
2 - npm install

npx create-react-app frontend
cd frontend
npm start

xóa file không cần: app.css,app.text, setupTest.js
cài đặt bootstrap.min.css

npm install react-bootstrap bootstrap

install navbar from: https://react-bootstrap.netlify.app/docs/components/navbar/
install font from: https://cdnjs.com/libraries?q=font

npm install react-router-dom react-router-bootstrap

virtualenv myenv
myenv\scripts\activate
pip install django

cd frontend
npm install axios

cd backend
pip install django-cors-headers

pip install pillow, sau đó thêm vào setting dòng dưới, ta chỉ định xong thư mục up hình ảnh
MEDIA_URL = '/images/'
CORS_ALLOW_ALL_ORIGINS = True
STATICFILES_DIRS = [
BASE_DIR / 'static'
]
MEDIA_ROOT = 'static/images'
-- trong urls.py, thêm
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

tạo serializer
class ProductSerializer(serializers.ModelSerializer):
class Meta:
model = Product
fields = '**all**'

npm install redux react-redux redux-thunk redux-devtools-extension

pip install djangorestframework-simplejwt
pip install setuptools

sử dụng POSTMAN
tab HEADER, KEY = Authorization, VALUE = Bearer {api key}

npm run build
