# BuyBot

You can use this source code for free.  

Please Pay Attention!!!  

You must not modify "sleep()". If you change it, you may get your Amazon account deleted.  

## How to use??

First : You have to install "Heroku CLI" and "Git".  
＞ [Heroku](https://devcenter.heroku.com/ja/articles/heroku-cli)  
＞ [Git](https://gitforwindows.org/)  

Second : You have to make Heroku's account.  
＞ [Heroku SignUp](https://signup.heroku.com/)  

Third : Let's deploy the source code. Open the cmd(windows) or terminal(mac).And please change to the directory where the source code is located.  
- heroku login
  - Please login your heroku account.
- heroku create project_name

Open the project on the Heroku website, click on created "Project", click on "Settings". the following URL in Bulidpacks.  
- https://github.com/heroku/heroku-buildpack-chromedriver.git  
- https://github.com/heroku/heroku-buildpack-google-chrome.git  

- git init
- git add .
- git remote add heroku https:// (When you created heroku's project, you can get https://~~)
- git commit -m "commit name"
- git push heroku master  

One more open the project on the Heroku website, click on created "Project", click on "Overview", click on "Configure Dynos", click on Pen Symbol, click on slide bar, click on "Confirm".  

Finish Deploy to Heroku !!
