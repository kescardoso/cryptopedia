# The Cryptopedia World

## Introduction
The Cryptopedia is a community encyclopedia about crypto assets, crypto economy, and blockchain technology. When we first start working with cryptocurrencies, terms and concepts may sound foreign. It can take significant time to understand this information and gain momentum to dive into the fantastic possibilities available in crypto investments and decentralized finance. The goal of The Cryptopedia is to help people get to the fundamentals faster and in a friendly manner. The Cryptopedia is free to use, and all are welcome to join in contributing and building the archives.

![](https://i.ibb.co/qsKs85k/Cryptopedia-Responsive.png)

The Cryptopedia is a Python-Flask based web application that lists crypto informational content in the form of an online interactive encyclopedia, backed by a MongoDB collection. The Cryptopedia is a cloud web app deployed via the Heroku PaaS and consists of a lightweight, responsive website designed with Google's Materialize CSS Framework. As you read this document, you find my complete development process, from UX strategy to deployment.

- [View The Cryptopedia on Heroku](https://thecryptopedia.herokuapp.com)
- [View the Repository on GitHub](https://github.com/kescardoso/cryptopedia)

This project has both educational and entrepreneurial goals.
Thanks for appreciating The Cryptopedia World with me!

[Kes Cardoso](http://www.kescardoso.com)

## Contents table

 1. [UX](##ux)
 
     - 1.1 [Wireframe](###wireframe)
     - 1.2 [Target User and What They Want to Achieve](###who-is-the-target-user)
     - 1.3 [Target-user main challenges](###target-users-main-challenges)
     - 1.4 [User Stories](###user-stories)

 2. [Features](#features)
     
     - 2.1 [Existing Features](#existing-features)
     - 2.2 [Features Left to Implement](#features-left-to-implement)
     
 3. [Technologies Used](#technologies-used)
 4. [Testing](#testing)
 5. [Deployment](#deployment)
 6. [Credits](#credits)

## 1 UX

###  1.1 Wireframe

Link to the initial wireframe for this app on [Figma](https://www.figma.com/file/6wA5cckeO90uYpP8XeUPkE/CRYPTOPEDIA?node-id=0:1)

###  1.2 Who is the target user

According to Binance, active cryptocurrency users total number currently stands [somewhere around 19 million](https://www.similarweb.com/website/binance.com), and according to Bitcointalk [about 82% of this users identify as male](https://bitcointalk.org/index.php?action=stats) between 18 and 45 years-old interested in the following areas: trading, investing, computers, software, design and animation, employement and career change, electronic gadgets, and banking systems. The current geographical engagement is mainly caucasian: Europe followed byt the US are the most important crypto markets and blockchain technology providers.

This demographic concentration could be due to a lack of educational and informational systems available for people who are outside the dominant fintech industry and network. Overall we see that the typical crypto user can be described as the following: **a European male, between the ages of 25 and 34, who is interested in finances, investing and technology**. He is relatively risky, not overly fearful of the volatile nature of cryptocurrency, while being tech-savvy enough to understand the basic mechanics of how crypto-related products and services work (source: [CoinTraffic](https://cointraffic.io/blog/crypto-audience-revealed-who-is-your-target-user/)).

The Cryptopedia World aims to provide entry-level information to people who are new to crypto and who are looking for alternatives to elevate their financial status and begin investing outside the traditional bank system or the stock and bonds market. Therefore, this project gears towards empowering new users, from a different background than those above, so crypto mass adoption can happen as intended: openly and democratically, all the while encouraging decentralized global wealth.

**Target-user and what they want to achieve:**
 
- **Client Avatar:** Cross-cultural English speaking men and women, from GenX and Millenials, who are researching basic information on how to get started with cryptocurrencies, digital asset trading, Bitcoin, Ethereum, Litecoin and Decentralised Finances (DeFi). This user demographic is based on the following:

    - Women: female engagement with Bitcoin and other cryptocurrencies is rising and currently at an all-time high. The Cryptopedia aims at bridging the gender technological and monetary gab, by also offering women vision and possibilities for financial and professional sustainability
    - Coding Bootcamp students interested in software and undergoing a career change, who are looking to achieve financial stability with an initial low monetary support.
    - Entrepreneurs interested in the new economy and looking for alternatives within staking, investing, accounting, affordable online payments, and low-cost international banking systems;
    - Travelers, digital nomads, culture and art lovers, and political enthusiasts with interests in open finance and global economy solutions.

### 1.3 Target-user's main challenges

These are some of the main reasons why people don’t invest in cryptocurrencies or blockchain-related products, and the biggest hindrances to the adoption of crypto, according to [CoinTraffic](https://cointraffic.io/blog/crypto-audience-revealed-who-is-your-target-user/):

-   They find crypto hard to understand.
-   They consider it to be too volatile.
-   They believe their investments could lose all of their value.
-   They believe all crypto to be a scam or in a bubble.
-   They are under the impression it is illegal in their jurisdiction.
-   They find crypto to be too difficult to spend in every-day life.