import instaloader

loader = instaloader.Instaloader()

username = input("Instagram kullanıcı adınızı girin: ")
password = input("Instagram şifrenizi girin: ")

loader.login(username, password)

post_url = input("İndirmek istediğiniz Instagram gönderisinin URL'sini girin: ")

try:
    post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])

    # Post'u indiriyoruz
    loader.download_post(post, target="instagram_video")
    print("Video başarıyla indirildi.")
except Exception as e:
    print("Bir hata oluştu:", e)
