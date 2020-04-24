# The Cryptopedia World

## Introduction
The Cryptopedia is a community encyclopedia about crypto assets, crypto economy, and blockchain technology. When we first start working with cryptocurrencies, terms and concepts may sound foreign. It can take significant time to understand this information and gain momentum to dive into the fantastic possibilities available in crypto investments and decentralized finance. The goal of The Cryptopedia is to help people get to the fundamentals faster and in a friendly manner. The Cryptopedia is free to use, and all are welcome to join in contributing and building the archives.

![](https://i.ibb.co/qsKs85k/Cryptopedia-Responsive.png)

The Cryptopedia is a Python-Flask web application that lists crypto informational content in the form of an online interactive encyclopedia, backed by a MongoDB collection. The Cryptopedia is a cloud web app deployed via the Heroku PaaS and consists of a lightweight, responsive website designed with Google's Materialize CSS Framework. As you read this document, you find my complete development process, from UX strategy to deployment.

- [View The Cryptopedia on Heroku](https://thecryptopedia.herokuapp.com)
- [View the Repository on GitHub](https://github.com/kescardoso/cryptopedia)

This project has both educational and entrepreneurial goals.
Thanks for appreciating The Cryptopedia World with me!

[Kes Cardoso](http://www.kescardoso.com)

## Contents table

 1. [UX](#ux)
 
     - [Wireframe](#wireframe)
     - [Target User and What They Want to Achieve](#who-is-the-target-user)
     - [Target User's Main Challenges](#main-challenges)
     - [User Stories](#user-stories)

 2. [Features](#features)
     
     - [Existing Features](#existing-features)
     - [Features Left to Implement](#features-left-to-implement)
     
 3. [Technologies Used](#technologies-used)
 4. [Testing](#testing)
 5. [Deployment](#deployment)
 6. [Credits](#credits)

## UX

### Wireframe

Link to the initial wireframe for this app on [Figma](https://www.figma.com/file/6wA5cckeO90uYpP8XeUPkE/CRYPTOPEDIA?node-id=0:1)

### Who is the target user

According to Binance, active cryptocurrency users total number currently stands [somewhere around 19 million](https://www.similarweb.com/website/binance.com), and according to Bitcointalk [about 82% of this users identify as male](https://bitcointalk.org/index.php?action=stats) interested in the following areas: trading, investing, computers, software, design and animation, employement and career change, electronic gadgets, and banking systems. The current geographical engagement is mainly caucasian: Europe, followed by the US are the most important crypto markets and blockchain technology providers.

This demographic concentration could be due to a lack of educational and informational systems available for people who are outside the dominant fintech industry. Overall we see that the typical crypto user can be described as the following: "**European male, between the ages of 25 and 34, who is interested in finances, investing and technology**. He is relatively risky, not overly fearful of the volatile nature of cryptocurrency, while being tech-savvy enough to understand the basic mechanics of how crypto-related products and services work" (source: [CoinTraffic](https://cointraffic.io/blog/crypto-audience-revealed-who-is-your-target-user/)).

The Cryptopedia World aims to provide entry-level information to people who are new to crypto and who are looking for alternatives to elevate their financial status and begin investing outside the traditional bank system or the stock and bonds market. Therefore, this project gears towards empowering new users, from a different background than those above, so crypto mass adoption can happen as intended: openly and democratically, all the while encouraging decentralized global wealth.

**Target-user and what they want to achieve:**
 
- **Client Avatar:** Cross-cultural English speaking men and women, from GenX and Millenials, who are researching basic information on how to get started with cryptocurrencies, digital asset trading, Bitcoin, Ethereum, Litecoin and Decentralised Finances (DeFi). This user demographic is based on the following:

    - Working women: female engagement with cryptocurrencies is rising and currently at an all-time high. The Cryptopedia aims to bridge the gender technological and monetary gab, by also offering women with resources and possibilities for financial and professional sustainability.
    - Coding Bootcamp students interested in software and undergoing a career change, who are looking to achieve financial stability with an initial low monetary support.
    - Entrepreneurs interested in the new economy and looking for alternatives within staking, investing, accounting, affordable online payments, and low-cost international banking systems;
    - Travelers, digital nomads, culture and art lovers, and political enthusiasts with interests in open finance and global economy solutions.

### Main challenges

These are some of the main reasons why people don’t invest in cryptocurrencies or blockchain-related products, according to [CoinTraffic](https://cointraffic.io/blog/crypto-audience-revealed-who-is-your-target-user/):

-   They find crypto hard to understand.
-   They believe all crypto to be a scam.
-   They are under the impression it is illegal in their jurisdiction.
-   They find crypto to be too difficult to spend in every-day life.

The goal of the Cryptopedia is to pass information about the fundamentals of crypto finance through a simple, user-friendly interface. Structures are lightweight, from design to copy, and information is recorded from reliable sources and research. The reader can pick and choose what they need to learn and clarify and build on their knowledge. They can also contribute and enrich the collection with their research. The Cryptopedia follows the same ideology of decentralized blockchain systems: it is a trustless and permissionless encyclopedia for the crypto learner.

### User Stories

Chloé is a 35-year-old European female, based in France. She is a cross-cultural English-speaking solo-entrepreneur, and she is looking for financial solutions during the current pandemic and economic downturn. She has savings on her French bank account, but she worries about her long-term sustainability, and how she will send money contributions to her retired mother who lives in Guadalupe, as the quarantine and social distancing are preventing her regular revenue.

Apart from finding online alternatives to continue running her business, Chloé wants to find a more profitable money management system, and she heard about crypto and how crypto transactions accross frontiers are cheaper and how DeFi could be an alternative for her savings. But Chloé is not tech-savvy, and she is afraid of running risks and losing her money.

When Chloé researches the internet about crypto assets, she finds very complex information, with lots of financial and technical jargon. But amid her google search, she spots The Cryptopedia World, which seems to be a more straightforward and accessible place to get started.

1. She opens The Cryptopedia web app on her Chrome browser and starts experimenting with it.

2. The interface is very straight forward, and soon she performs a term search through the glossary to find information about Etherium.

3. The search brings out a short text about what Etherium is and the possibilities around Ether and stable coins.

4. So Chloé goes to the categories tab and searches for "stable coins" and pulls out another short text, and she finds out about DeFi.

5. Chloe decides then to go back to google to find out more in-depth information related to DeFi. She learns about terms such as Smart Contracts, and the possibilities of lending-borrowing with higher interest rates than traditional banking, all using stable coins which are not affected by high volatility such as Bitcoin.

6. She is now very excited about the possibility of having a crypto staking and savings account, so she goes back to The Cryptopedia and decides to share this information with the archives.

7. Chloé quickly finds the register and login page; she enters her user information and logs in to The Cryptopedia. She is now able to add a new term to the glossary 'DeFi' and contribute to the database with her research.

8. She clicks the button "add new term", she fills out the form, and she clicks save. And her contribution is added to the glossary.

9. Chloé is also able to enter new category names to the archives. She can, too, search for terms using the category lists, which group terms by categories. And she finds, on the categorie list "Financial Terms", the term "Exchanges".
 
10. She reads about exchanges and learns that these are the plataforms where we can buy, sell and send crypto beyond borders for a very affordable price. She feels very good about this possibility for sending money to her retired mother and she wants to find out more about exchanges and wallets.
 
12. Chloé now feels empowered and motivated to continue growing her knowledge about crypto finances. The Cryptopedia is friendly and easy to use, and her participation counts: she is motivated. She is also looking forward to learning more about staking stable coins and finding a crypto banking solution to use her stable coins with a crypto visa card for her weekly groceries. The possibilities are now endless!

## Features
 
### Existing Features

1. **Navbar:** contains the logo and the main menu with easy access to the glossary, add new term and category, term lists by category and the login button

2. **Search Box:** this is a full-text search box that allows the user to locate a term to on the glossary. The Search Box is wired to the Cryptopedia MongoDB atlas.

3. **The Glossary:** this is the Cryptopedia itself, where all the information is stored (listed by term name, term category and term description) in the form of a collapsable accordion list.

4. **Add New Buttons** this offers the possibility for users and admins to add new terms and new categories to the glossary, via a form wired to the database.

5. **Edit Button** this offers the possibility for users and admins to edit existing terms and categories already in the glossary.

6. **Delete Button:** this offers the possibility for admins only to curate and erase terms and categories from the glossary.

7. **Footer:** Displays credits and contact links. It also has a login/logout ticker that becomes available during user sessions.

### Features Left to Implement

1. **Autocomplete Search:** at the moment, the app disposes of a full-text search form (which is the feature available for MongoDB search forms). With more complex functionalities such as Elastic search, it is possible to have a autocomplete search feature.

2. **Pagination:** as the glossary grows with more terms, a pagination feature becomes necessary and is planned to be implemented soon.

3. **Fix Add New Category Dropdown Form:** there is an issue coming from MaterializeCss where the dropdown doesn't display correctly on the first click.

## Technologies Used

1. HTML & CSS.

2. Programing languages - this project uses [Python](https://www.python.org/) as the main programing language, as well as  [Javascript](www.javascript.com) and the [JQuery library](https://jquery.com/).

3. [Flask](https://flask.palletsprojects.com/en/1.1.x/) - This project uses the **Flask** frameqork and the Jinja library.

4. [MongoDB](https://www.mongodb.com/) - This project uses **MongoDB** as a document-oriented database to store data in JSON-like objects with dynamic schema.

5. [Materialize](https://materializecss.com/) - This project uses the **Materialize** Css Framework to facilitate a grid-system, responsive design, and optimal user experience.

6. [GitPod](https://gitpod.io/) - This project uses **Gitpod** as a development and testing environment.

7. [FontAwesome](https://fontawesome.com/) - This project uses **FontAwesome** to style the footer with icons.

8. [Git](https://git-scm.com) - This project uses **Git** for version-control and for tracking changes in source code during development. 

9. [GitHub](https://github.com/) - This project uses **GitHub** as a remote code repository.

10. [Heroku](https://www.heroku.com/) - This project uses **Heroku** for app deployment.

11. [StackEdit](https://pages.github.com/) - This project uses **StackEdit** as an in-browser Markdown editor for beautiful, stress-free README writing.