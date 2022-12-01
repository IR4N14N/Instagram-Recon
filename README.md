# Instagram-Recon V1.0
This is an OSINT Tool on Instagram.  
It can be used to get the data of public accounts as well as Private accounts like their Username, User-id, Full-Name, Followers and Following count, Profile-pic-HD etc. that can be used to recon the user on Instagram.
![InstaRecon-test](https://user-images.githubusercontent.com/97558053/205157780-02c02c48-bbd6-4358-be6b-f6de6119b033.png)

<h2>Installation and Usage (python 3)</h2>

pip install -r requirements.txt <br />
python InstaRecon.py <br />

→ Now Just Enter username of any Account<br />
<hr />
<h1>Installation and Usage JavaScript</h1>


https://user-images.githubusercontent.com/97558053/205157614-316b24a8-0fa3-40ed-afbe-09069a1579aa.mp4


Step 1 : Open Instagram.com in a web browser and then enter your Instagram username or the phone number or email address associated with the account. After that, enter your password and tap Log In.<br />
Step 2 : Open your browser console and then paste the code below and press enter to execute the code! <br />

```js
(async () => {console.clear();const url = prompt("Enter Username : ");await fetch(`https://www.instagram.com/${url}/?__a=1&__d=dis`, {method: 'GET',headers: {'Accept': 'application/json',},}).then(response => response.json()).then(response => JSON.stringify(response)).then(response => JSON.parse(response)).then(objects => {let ReconList = ["edge_followed_by", "edge_follow", "username", "fbid", "id", "full_name", "biography", "is_verified", "is_private", "is_joined_recently", "is_business_account", "business_category_name", "business_email", "business_phone_number", "hide_like_and_view_counts", "profile_pic_url", "profile_pic_url_hd"];for (i = 0; i < ReconList.length; i++) {if (ReconList[i] == "edge_followed_by") {console.clear();console.log('%c InstaRecon', 'font-family: "Times New Roman", Times, serif; background: #222; color: #9400D3; font-size: 45px; display:inline');console.log('%c \t —  By IR4N14N  —', 'font-family: "Times New Roman", Times, serif; background: #222; color: #7FFF00; font-size: 15px');console.log(`Followers : ${objects["graphql"]['user'][ReconList[i]]['count']}`);} else if (ReconList[i] == "edge_follow") {console.log(`Following : ${objects["graphql"]['user'][ReconList[i]]['count']}`);} else {console.log(`${ReconList[i]} : ${objects["graphql"]['user'][ReconList[i]]}`);}}})})();
```
