# blogAPP-restframework

# საინფორმაციო ერთეულები მონაცემთა ბაზაში ბლოგის დიზაინისთვის შეიძლება შეიცავდეს შემდეგს:

## Post: / პოსტი:

     - სათაური / Title (CharField): The title of the blog post.
     - შინაარსი  / Content (TextField): The main content of the blog post.
     - ავტორი  /   Author (ForeignKey): A reference to the user who wrote the blog post.
     - გამოქვეყნების თარიღი /  Date Published (DateTimeField): The date and time when the blog post was published. 
     - კატეგორია / Category (ForeignKey): A reference to the category/topic the blog post belongs to.


## Category/Topic: / კატეგორია/თემა:

     - სახელი: კატეგორიის ან თემის სახელი. / Name (CharField): The name of the category or topic.

## User: / მომხმარებელი:

     - მომხმარებლის სახელი / Username (CharField): The username of the user.
     - ელფოსტა / Email (EmailField): The email address of the user.
     - პაროლი / Password (CharField): The hashed password of the user.
     - პროფილის სურათი (არასავალდებულო) / Profile Picture (ImageField): An optional profile picture for the user.

# plan to make this all work:

# Back-end tasks

## Step 1: Set up Django Project / 
     Create a new Django project.
     Set up the database and connect it to the project.
     შექმენით ახალი Django პროექტი.
     დააყენეთ მონაცემთა ბაზა და დააკავშირეთ იგი პროექტთან.

## Step 2: Define Models / განსაზღვეთ მოდელები
    Define the models (Post, Category, User) with their respective fields.
    განსაზღვრეთ მოდელები (Post, Category, User) შესაბამისი ველებით.

## Step 3: Create Views and URLs
     Create views to handle rendering the blog homepage, blog post page, category pages, user profile, user registration, and login forms.
     Define URLs to map views to specific URLs.
     შექმენით Views ბლოგის საწყისი გვერდის, ბლოგის პოსტის გვერდის, კატეგორიის გვერდების, მომხმარებლის პროფილის, მომხმარებლის რეგისტრაციისა და შესვლის ფორმების .....
     განსაზღვრეთ URL-ები Views კონკრეტულ URL-ებზე გადასატანად.

## Step 4: Implement API /  API-ების დანერგვა
     Create APIs to handle data retrieval for blog posts, categories, user information, and authentication.
     შექმენით API-ები ბლოგის პოსტების, კატეგორიების, მომხმარებლის ინფორმაციისა და ავთენტიფიკაციის მონაცემების მოსაძიებლად.

## Step 5: User Authentication / მომხმარებლის ავთენტიფიკაცია
     Implement user registration and login views to handle user authentication.
     Use Django's built-in authentication system or a third-party library like Django Rest Framework for token-based authentication.
     დანერგეთ მომხმარებლის რეგისტრაცია და შესვლის ხედები მომხმარებლის ავტორიზაციის დასამუშავებლად.
     გამოიყენეთ Django-ს ჩაშენებული ავტორიზაციის სისტემა ან მესამე მხარის ბიბლიოთეკა, როგორიცაა Django Rest Framework ტოკენზე დაფუძნებული ავთენტიფიკაციისთვის.

## Step 6: Set up Media Handling
    Configure Django settings to handle media files (images) uploaded by users.
    დააკონფიგურირეთ Django პარამეტრები მომხმარებლების მიერ ატვირთული მედია ფაილების (სურათების) დასამუშავებლად.

## Step 7: Admin Interface
    Set up the Django admin interface to allow administrators to manage blog posts, categories, and users.
    დააყენეთ Django ადმინისტრატორის ინტერფეისი, რათა ადმინისტრატორებს მისცეთ საშუალება მართონ ბლოგის პოსტები, კატეგორიები და მომხმარებლები.

## Step 8: Deploy
    Deploy the Django application to a web server or cloud platform.

## Step 9: Testing and Debugging
    Test the application thoroughly to identify and fix any bugs or issues.

## Step 10: Security Considerations
    Implement security measures like input validation, protection against cross-site scripting (XSS) attacks, and protecting sensitive user data.
    განახორციელეთ უსაფრთხოების ზომები, როგორიცაა შეყვანის ვალიდაცია, დაცვა საიტის სკრიპტირების (XSS) თავდასხმებისგან და მომხმარებლის მონაცემების დაცვა.

## Step 11: Performance Optimization
    Optimize the application's performance to ensure it loads quickly and handles traffic efficiently.
    აპლიკაციის მუშაობის ოპტიმიზაცია, რათა დარწმუნდეთ, რომ ის სწრაფად იტვირთება და ეფექტურად უმკლავდება ტრაფიკს.

## Step 12: Documentation
    Document the code and the process of setting up and running the application.




# Front-end tasks:

## Step 1: Design Integration / დიზაინის ინტეგრაცია
     Convert the Figma design into HTML, CSS, and JavaScript.
     Implement responsive design to ensure the blog looks good on various devices.
     გადააკეთეთ Figma დიზაინი HTML, CSS და JavaScript-ად.
     განახორციელეთ რესპონსივ დიზაინი, რათა დარწმუნდეთ, რომ ბლოგი კარგად გამოიყურება სხვადასხვა მოწყობილობებზე.

## Step 2: Fetching Data / მონაცემების მიღება
     Use API calls to fetch blog posts and categories from the Django backend.
     Display the fetched data on the blog's homepage and category pages.
     გამოიყენეთ API fetch-ი, რათა მიიღოთ ბლოგის პოსტები და კატეგორიები Django backend-იდან.
     მოტანილი მონაცემების ჩვენება ბლოგის მთავარ გვერდზე და კატეგორიის გვერდებზე.

## Step 3: Blog Post Page / ბლოგის პოსტის გვერდი
     Create a template to display individual blog posts with their full content, author, date, and category.
     Implement the necessary logic to navigate from the homepage to a specific blog post page.
     შექმენით შაბლონი ინდივიდუალური ბლოგის პოსტების საჩვენებლად მათი სრული შინაარსით, ავტორით, თარიღით და კატეგორიით.
     განახორციელეთ საჭირო ლოგიკა საწყისი გვერდიდან კონკრეტულ ბლოგის პოსტის გვერდზე გადასასვლელად.

## Step 4: User Registration and Login / მომხმარებლის რეგისტრაცია და შესვლა
     Design and implement user registration and login forms.
     Use AJAX or API calls to handle user authentication.
     მომხმარებლის რეგისტრაციისა და შესვლის ფორმების შემუშავება და დანერგვა.
     გამოიყენეთ AJAX ან API მომხმარებლის ავთენტიფიკაციის დასამუშავებლად.

## Step 5: User Profile / მომხმარებლის პროფილი
     Design and implement a user profile page where users can view and update their information, including the profile picture.
     შეიმუშავეთ და დანერგეთ მომხმარებლის პროფილის გვერდი, სადაც მომხმარებლებს შეუძლიათ ნახონ და განაახლონ თავიანთი ინფორმაცია, პროფილის სურათის ჩათვლით.

