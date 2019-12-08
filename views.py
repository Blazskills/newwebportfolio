from run import *
from models import Regtb
from models import *


ALLOWED_EXTENSIONS = set(['png','gif','jpg','jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def mailclient(mails):
    msg = Message('TEMITOPE ISAAC NEWSLETTER', sender='info@toismatt.com', recipients=[str(mails)])
    msg.body = 'Your Email is {}'.format(mails)+' And you have succssfully Subscribe to my newsletter '+'  Thank You'
    mail.send(msg)

@app.route('/mailletter', methods=['GET', 'POST'])
def mailletter():
    try:
        if request.method =='POST':
            mails = request.form['mails']
            usermails = mailtb.query.filter_by(mails=mails).first()
            if not usermails:
                mailreg = mailtb(mails=mails)
                db.session.add(mailreg)
                mailclient(mails)
                db.session.commit()
                flash("Subscribed Successfully","success")
                return redirect(url_for('index'))
            else:
                flash("Email already exit, You can only subscribe once. THanks for your interest.","danger") 
                return redirect(url_for('index'))
    except socket.error:
        flash("sorry we could not connect to your email due to network problem","danger") 
        return redirect(url_for('index'))
    

    #Starting of Site routes
@app.route('/')
def index():
     bioposts=Biotb.query.all()
     portposts=portfoliotb.query.all()
     serviceposts=servicetb.query.all()
     testposts=testimonytb.query.all()
     return render_template('index.html', bioposts=bioposts, portposts=portposts, serviceposts=serviceposts, testposts=testposts)



@app.route('/portfolio_single/<int:id>')
def portfolio_single(id):
    newportposts = portfoliotb.query.filter_by(id=id).first()
    portposts=portfoliotb.query.all()
    return render_template('portfolio-single.html',newportposts=newportposts, portposts=portposts)

@app.route('/blogposts')
def blogposts():
    return render_template('blog.html')

@app.route('/single_blogpost')
def single_blogpost():
    return render_template('single_blogpost.html')
#End of Site routes


# Begining of Admin routes

@app.route('/admin')
@login_required
def admin():
    posts = Regtb.query.all()
    return render_template('./admin/page-starter.html')


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    newportposts=portfoliotb.query.all()
    if request.method == 'POST':
        portfoliocontent = request.form['portfoliocontent']
        portfoliotitle = request.form['portfoliotitle']
        clientname = request.form['clientname']
        portcategory = request.form['portcategory']
        portwebname = request.form['portwebname']
        dod = request.form['dod']
        portpix = request.files['portpix']
        if portpix and allowed_file(portpix.filename):
                filename=secure_filename(portpix.filename)
                portpix.save(os.path.join('./static/admin/portpix',filename))
                url = str(filename)
                new_reg = portfoliotb(portfoliocontent=portfoliocontent,portfoliotitle=portfoliotitle,clientname=clientname,portcategory=portcategory,portwebname=portwebname,dod=dod,portpix=url)
                db.session.add(new_reg)
                db.session.commit()
                flash("Portfolio Submitted successful","success")
                return redirect(url_for('admin'))
        else:
            flash("something went wrong with the picture, try again","danger")
            return redirect(url_for('portfolio'))
    # return render_template('./admin/register.html')
    return render_template('portfolio.html' ,newportposts=newportposts)


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        career = request.form['career']
        phone = request.form['phone']
        email = request.form['email']
        usermail=Regtb.query.filter_by(email=email).first()
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        userpix = request.files['userpix']
        secure_password = generate_password_hash(password, method="sha256")
        if userpix and allowed_file(userpix.filename):
             filename=secure_filename(userpix.filename)
             userpix.save(os.path.join('/home/blazskills/Documents/webportfolio/static/admin/userpix',filename))
             url = str(filename)
             if not usermail:
                 if password == confirm_password:
                    new_reg = Regtb(name=name,username=username,email=email,career=career,phone=phone,password=secure_password,userpix=url)
                    db.session.add(new_reg)
                    db.session.commit()
                    flash("Login successful","success")
                    return redirect(url_for('admin'))
                 else:
                    flash("password does not match","danger")
                    return redirect(url_for('register'))
             else:
                flash("Email already exit","danger")
                return redirect(url_for('register'))
        else:
            flash("something went wrong with the picture, try again","danger")
            return redirect(url_for('register'))
    return render_template('./admin/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user=Regtb.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user) #save session
                flash("Login successful","success")
                return redirect(url_for('admin'))
            else:
               flash("wrong password","danger")
               return redirect(url_for('login'))
        else:
          flash("wrong username","danger")
          return redirect(url_for('login'))

    return render_template('./admin/login.html')


@app.route('/bio', methods=['GET','POST'])
@login_required
def bio():
    posts = Biotb.query.all()
    if request.method =='POST':
        aboutcontent = request.form['aboutcontent']
        whycontent = request.form['whycontent']
        visioncontent = request.form['visioncontent']
        career1 = request.form['career1']
        career2 = request.form['career2']
        career3 = request.form['career3']
        fblk = request.form['fblk']
        twlk = request.form['twlk']
        gitlk = request.form['gitlk']
        linkedinlk = request.form['linkedinlk']
        anylk = request.form['anylk']
        userpix = request.files['userpix']
        if userpix and allowed_file(userpix.filename):
            filename=secure_filename(userpix.filename)
            userpix.save(os.path.join('./static/admin/userpix',filename))
            url = str(filename)
            new_post = Biotb(aboutcontent=aboutcontent,whycontent=whycontent,visioncontent=visioncontent,career1=career1,career2=career2,career3=career3,fblk=fblk,twlk=twlk,gitlk=gitlk,linkedinlk=linkedinlk,anylk=anylk,userpix=url)
            db.session.add(new_post)
            db.session.commit()
            flash("Bio posted","success")
            return redirect(url_for('biodash'))
        else:
            flash("invalid pictures","danger")
            return redirect(url_for('bio'))
    return render_template('./admin/formelement.html', posts=posts)

@app.route('/service', methods=['GET', 'POST'])
@login_required
def service():
    if request.method =='POST':
        headings = request.form['headings']
        servicecontent = request.form['servicecontent']
        servicepost = servicetb(headings=headings,servicecontent=servicecontent)
        db.session.add(servicepost)
        db.session.commit()
        flash("Service posted","success")
        return redirect(url_for('admin'))
    return render_template('./admin/service.html')

@app.route('/admin_portfolio')
@login_required
def admin_portfolio():
    return render_template('./admin/portfolio.html')

@app.route('/testimony', methods=['GET', 'POST'])
@login_required
def testimony():
    if request.method =='POST':
        name = request.form['name']
        testcontent = request.form['testcontent']
        jobdescription = request.form['jobdescription']
        testpix = request.files['testpix']
        if testpix and allowed_file(testpix.filename):
            filename=secure_filename(testpix.filename)
            testpix.save(os.path.join('./static/admin/userpix',filename))
            url = str(filename)
            servicepost = testimonytb(name=name,testcontent=testcontent,jobdescription=jobdescription,testpix=url)
            db.session.add(servicepost)
            db.session.commit()
            flash("testimony posted","success")
            return redirect(url_for('admin'))
    return render_template('./admin/testimony.html')


@app.route('/contactmsg', methods=['GET', 'POST'])
@login_required
def contactmsg():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        contactpost = contactmsgtb(name=name,email=email,message=message)
        db.session.add(contactpost)
        db.session.commit()
        flash("Message Sent","success")
        return redirect(url_for('index'))



@app.route('/testimonydash')
@login_required
def testimonydash():
    serviceposts = testimonytb.query.all()
    return render_template('./admin/testimony_dash.html', serviceposts=serviceposts)


@app.route('/admin_blog')
@login_required
def admin_blog():
    return render_template('./admin/adminblog.html')

@app.route('/contact')
@login_required
def contact():
    return render_template('./admin/contact.html')

@app.route('/sponsor')
@login_required
def sponsor():
    return render_template('./admin/sponsor.html')

# End of Admin routes

#dashboad routes

@app.route('/biodash')
@login_required
def biodash():
    bioposts=Biotb.query.order_by(Biotb.today.asc()).all()
    return render_template('./admin/bio_dash.html', bioposts=bioposts )

@app.route('/regdash')
@login_required
def regdash():
    posts = Regtb.query.order_by(Regtb.Reg_Date.asc()).all()
    return render_template('./admin/reg_dash.html', posts=posts)

@app.route('/servicedash')
@login_required
def servicedash():
    _contactmsgs = contactmsgtb.query.all()
    return render_template('./admin/service_dash.html', _contactmsgs =_contactmsgs)

@app.route('/portdash')
@login_required
def portdash():
    posts = portfoliotb.query.order_by(portfoliotb.today.asc()).all()
    return render_template('./admin/portfolio_dash.html', posts = posts)



@app.route('/blogdash')
@login_required
def blogdash():
    return render_template('./admin/blog_dash.html')

@app.route('/contactdash')
@login_required
def contactdash():
    return render_template('./admin/contact_dash.html')

@app.route('/sponsordash')
@login_required
def sponsordash():
    return render_template('./admin/sponsors_dash.html')

@app.route('/newsletterdash')
@login_required
def newsletterdash():
    mailposts=mailtb.query.all()
    return render_template('./admin/newsletter_dash.html', mailposts = mailposts)


#extral routes 

@app.route('/delete/<int:id>')
def drop(id):
       blog_content = Regtb.query.filter_by(id=id).delete()
       db.session.commit(blog_content)
       return redirect(url_for('regdash'))

@app.route('/maildrop/<int:id>')
def maildrop(id):
       mailcontent = mailtb.query.filter_by(id=id).delete()
       db.session.commit()
       return redirect(url_for('newsletterdash'))

@app.route('/portdelete/<int:id>')
def portdelete(id):
       port_content = portfoliotb.query.filter_by(id=id).delete()
       db.session.commit()
       return redirect(url_for('portdash'))


@app.route('/testdrop/<int:id>')
def testdrop(id):
       test_content = testimonytb.query.filter_by(id=id).delete()
       db.session.commit()
       flash("testimony deleted","success")
       return redirect(url_for('admin'))


#logout route
@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash("You're logout Successfully","success")
  return redirect(url_for('index'))




@app.route('/edit/<int:id>')
def edit(id):
    content = Biotb.query.filter_by(id=id).first()
    return render_template('./admin/formelement.html',content=content)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    update_bio = Biotb.query.filter_by(id=id).first()
    if request.method == 'POST':
        aboutcontent = request.form['aboutcontent']
        whycontent = request.form['whycontent']
        visioncontent = request.form['visioncontent']
        career1 = request.form['career1']
        career2 = request.form['career2']
        career3 = request.form['career3']
        fblk = request.form['fblk']
        twlk = request.form['twlk']
        gitlk = request.form['gitlk']
        linkedinlk = request.form['linkedinlk']
        anylk = request.form['anylk']
        userpix = request.files['userpix']
        if userpix and allowed_file(userpix.filename):
            filename=secure_filename(userpix.filename)
            userpix.save(os.path.join('./static/admin/userpix',filename))
            url = str(filename)
            update_bio.aboutcontent = aboutcontent
            update_bio.whycontent = whycontent
            update_bio.visioncontent = visioncontent
            update_bio.career1  = career1 
            update_bio.career2  = career2
            update_bio.career3  = career3
            update_bio.fblk  = fblk
            update_bio.twlk  = twlk 
            update_bio.gitlk  = gitlk
            update_bio.linkedinlk  = linkedinlk
            update_bio.anylk  = anylk 
            update_bio.userpix  = url
            db.session.commit()
            flash("Bio Updated","success")
            return redirect(url_for('biodash'))
    return render_template('./admin/formelement.html', update_bio=update_bio)





@app.route('/editport/<int:id>')
def editport(id):
    contentport = portfoliotb.query.filter_by(id=id).first()
    return render_template('./admin/portfolioupdate.html',contentport=contentport)


@app.route('/updateport/<int:id>', methods=['POST'])
def updateport(id):
    update_port = portfoliotb.query.filter_by(id=id).first()
    if request.method == 'POST':
        portfoliocontent = request.form['portfoliocontent']
        portfoliotitle = request.form['portfoliotitle']
        clientname = request.form['clientname']
        portcategory = request.form['portcategory']
        portwebname = request.form['portwebname']
        dod = request.form['dod']
        portpix = request.files['portpix']
        if portpix and allowed_file(portpix.filename):
            filename=secure_filename(portpix.filename)
            portpix.save(os.path.join('./static/admin/portpix',filename))
            url = str(filename)
            update_port.portfoliocontent = portfoliocontent
            update_port.portfoliotitle = portfoliotitle
            update_port.clientname = clientname
            update_port.portcategory  = portcategory 
            update_port.portwebname  = portwebname
            update_port.dod  = dod
            update_port.portpix  = url
            db.session.commit()
            flash("Portifolio Updated","success")
            return redirect(url_for('admin'))