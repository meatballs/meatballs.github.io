Title: Contact
Date: 2014-10-01 13:32
Tags: pelican
Slug: contact
Author: Owen Campbell

<form action="//formspree.io/owen.campbell@tanti.org.uk" method="POST">
  <div class="form-group">
    <label for="inputName">Name</label>
    <input class="form-control" type="text" id="inputName" placeholder="Enter name" required>
  </div>
  <div class="form-group">
    <label for="inputEmail">Email Address</label>
    <input class="form-control" type="email" id="inputEmail" placeholder="Enter email" name="_replyto" required>
  </div>
  <div class="form-group">
    <label for="inputMessage">Message</label>
    <textarea class="form-control" id="inputMessage" name="data" rows="3" placeholder="Enter message" required></textarea>
  </div>
  <input type="hidden" name="_subject" value="Website Contact" />
  <input type="text" name="_gotcha" style="display:none" />
  <input type="hidden" name="_next" value="/pages/thanks.html" />
  <button type="submit" class="btn btn-default">Send</button>
</form>
