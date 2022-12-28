print('Generating static site. INDEX')
#reads top.html
top_html = open('./templates/top.html').read()

#reads bottom.html
bottom_html = open('./templates/bottom.html').read()

#reads content index.html
content_html = open('./content/index.html').read()

print('Combining files')

#combines into new file
combined_html = top_html + content_html + bottom_html
open('./docs/index.html', 'w+').write(combined_html)

##contact
top_html = open('./templates/top.html').read()

bottom_html = open('./templates/bottom.html').read()

content_html = open('./content/contact.html').read()

combined_html = top_html + content_html + bottom_html
open('./docs/contact.html', 'w+').write(combined_html)

#portfolio
top_html = open('./templates/top.html').read()

bottom_html = open('./templates/bottom.html').read()

content_html = open('./content/portfolio.html').read()

combined_html = top_html + content_html + bottom_html
open('./docs/portfolio.html', 'w+').write(combined_html)

#services
top_html = open('./templates/top.html').read()

bottom_html = open('./templates/bottom.html').read()

content_html = open('./content/services.html').read()

combined_html = top_html + content_html + bottom_html
open('./docs/services.html', 'w+').write(combined_html)


##about
top_html = open('./templates/top.html').read()

bottom_html = open('./templates/bottom.html').read()

content_html = open('./content/about.html').read()

combined_html = top_html + content_html + bottom_html
open('./docs/about.html', 'w+').write(combined_html)

