from lxml import html
import requests
import csv

solarwindsReviewers = []
solarwindsReviews = []
solarwindsStars = []
solarwindsTitle = []

#
#
# SOLARWINDS
#
#

# loop through all the Solarwinds review pages of Spiceworks
for i in range(1,20):
    
# get page and save in tree form to navigate
    page = requests.get('https://community.spiceworks.com/products/14853-solarwinds-inc/reviews?page=' + str(i))
    tree = html.fromstring(page.content)

# store the names of reviewers on page i in reviewers[]
    reviewers = tree.xpath('//span[@data-test="extendedUserName"]/text()')
# if page does not exist, break loop
    if reviewers == []:
        break
    
    else:
# loop through reviewers and trim white space
        reviewersTrimmed = []

        for item in reviewers:
            temp = item.strip()
            reviewersTrimmed.append(temp)
            solarwindsTitle.append('Solarwinds')
            
# once white space is trimmed, add the reviewers from page i to catch all bucket[]
        solarwindsReviewers += reviewersTrimmed

    reviews = tree.xpath('//p[@itemprop="reviewBody"]/text()')
# since loop will break if reviewers is empty, there is no need to duplicate this
# add reviews to catch all pail[]
    solarwindsReviews += reviews

    stars = tree.xpath('//meta[@itemprop="ratingValue"]/@content')
# delete the first element of the array, which is always the overall rating of the technology
    stars.pop(0)
    solarwindsStars += stars
    
#
#
#   NAGIOS
#
#

# loop through all the Nagios review pages of Spiceworks
for i in range(1,20):
    
# get page and save in tree form to navigate
    page = requests.get('https://community.spiceworks.com/products/17706-nagios/reviews?page=' + str(i))
    tree = html.fromstring(page.content)

# store the names of reviewers on page i in reviewers[]
    reviewers = tree.xpath('//span[@data-test="extendedUserName"]/text()')
# if page does not exist, break loop
    if reviewers == []:
        break
    
    else:
# loop through reviewers and trim white space
        reviewersTrimmed = []

        for item in reviewers:
            temp = item.strip()
            reviewersTrimmed.append(temp)
            solarwindsTitle.append('Nagios')
            
# once white space is trimmed, add the reviewers from page i to catch all bucket[]
        solarwindsReviewers += reviewersTrimmed

    reviews = tree.xpath('//p[@itemprop="reviewBody"]/text()')
# since loop will break if reviewers is empty, there is no need to duplicate this
# add reviews to catch all pail[]
    solarwindsReviews += reviews

    stars = tree.xpath('//meta[@itemprop="ratingValue"]/@content')
# delete the first element of the array, which is always the overall rating of the technology
    stars.pop(0)
    solarwindsStars += stars
    
#
#
#   PRTG
#
#

# loop through all the Nagios review pages of Spiceworks
for i in range(1,20):
    
# get page and save in tree form to navigate
    page = requests.get('https://community.spiceworks.com/products/15779-paessler-prtg-network-monitor/reviews?page=' + str(i))
    tree = html.fromstring(page.content)

# store the names of reviewers on page i in reviewers[]
    reviewers = tree.xpath('//span[@data-test="extendedUserName"]/text()')
# if page does not exist, break loop
    if reviewers == []:
        break
    
    else:
# loop through reviewers and trim white space
        reviewersTrimmed = []

        for item in reviewers:
            temp = item.strip()
            reviewersTrimmed.append(temp)
            solarwindsTitle.append('PRTG')
            
# once white space is trimmed, add the reviewers from page i to catch all bucket[]
        solarwindsReviewers += reviewersTrimmed

    reviews = tree.xpath('//p[@itemprop="reviewBody"]/text()')
# since loop will break if reviewers is empty, there is no need to duplicate this
# add reviews to catch all pail[]
    solarwindsReviews += reviews

    stars = tree.xpath('//meta[@itemprop="ratingValue"]/@content')
# delete the first element of the array, which is always the overall rating of the technology
    stars.pop(0)
    solarwindsStars += stars
    
#
#
#   CACTI
#
#

# loop through all the Nagios review pages of Spiceworks
for i in range(1,20):
    
# get page and save in tree form to navigate
    page = requests.get('https://community.spiceworks.com/products/23399-cacti/reviews?page=' + str(i))
    tree = html.fromstring(page.content)

# store the names of reviewers on page i in reviewers[]
    reviewers = tree.xpath('//span[@data-test="extendedUserName"]/text()')
# if page does not exist, break loop
    if reviewers == []:
        break
    
    else:
# loop through reviewers and trim white space
        reviewersTrimmed = []

        for item in reviewers:
            temp = item.strip()
            reviewersTrimmed.append(temp)
            solarwindsTitle.append('Cacti')
            
# once white space is trimmed, add the reviewers from page i to catch all bucket[]
        solarwindsReviewers += reviewersTrimmed

    reviews = tree.xpath('//p[@itemprop="reviewBody"]/text()')
# since loop will break if reviewers is empty, there is no need to duplicate this
# add reviews to catch all pail[]
    solarwindsReviews += reviews

    stars = tree.xpath('//meta[@itemprop="ratingValue"]/@content')
# delete the first element of the array, which is always the overall rating of the technology
    stars.pop(0)
    solarwindsStars += stars
    
#
#
#   ZABBIX
#
#

# loop through all the Nagios review pages of Spiceworks
for i in range(1,20):
    
# get page and save in tree form to navigate
    page = requests.get('https://community.spiceworks.com/products/48241-zabbix/reviews?page=' + str(i))
    tree = html.fromstring(page.content)

# store the names of reviewers on page i in reviewers[]
    reviewers = tree.xpath('//span[@data-test="extendedUserName"]/text()')
# if page does not exist, break loop
    if reviewers == []:
        break
    
    else:
# loop through reviewers and trim white space
        reviewersTrimmed = []

        for item in reviewers:
            temp = item.strip()
            reviewersTrimmed.append(temp)
            solarwindsTitle.append('Zabbix')
            
# once white space is trimmed, add the reviewers from page i to catch all bucket[]
        solarwindsReviewers += reviewersTrimmed

    reviews = tree.xpath('//p[@itemprop="reviewBody"]/text()')
# since loop will break if reviewers is empty, there is no need to duplicate this
# add reviews to catch all pail[]
    solarwindsReviews += reviews

    stars = tree.xpath('//meta[@itemprop="ratingValue"]/@content')
# delete the first element of the array, which is always the overall rating of the technology
    stars.pop(0)
    solarwindsStars += stars


    
"""
#
#
#   AUVIK
#
#

    
# get page and save in tree form to navigate
page = requests.get('https://community.spiceworks.com/products/58117-auvik/reviews')
tree = html.fromstring(page.content)
print(tree)

# store the names of reviewers on page i in reviewers[]
reviewers = tree.xpath('//span[@data-test="extendedUserName"]/text()')

if reviewers != []:
    reviewersTrimmed = []

    for item in reviewers:
        temp = item.strip()
        reviewersTrimmed.append(temp)
        solarwindsTitle.append('Auvik')
            
    # once white space is trimmed, add the reviewers from page i to catch all bucket[]
    solarwindsReviewers += reviewersTrimmed

for item in reviewers:
    solarwindsTitle.append("Auvik")
solarwindsReviewers += reviewers

reviews = tree.xpath('//p[@itemprop="reviewBody"]/text()')
# since loop will break if reviewers is empty, there is no need to duplicate this
# add reviews to catch all pail[]
solarwindsReviews += reviews

stars = tree.xpath('//meta[@itemprop="ratingValue"]/@content')
# delete the first element of the array, which is always the overall rating of the technology
stars.pop(0)
solarwindsStars += stars
"""

        
    
print 'reviewers:', solarwindsReviewers
print 'reviews:', solarwindsReviews
print 'stars:', solarwindsStars
print 'title:', solarwindsTitle

print 'bucket length is', len(solarwindsReviewers)
print 'pail length is', len(solarwindsReviews)
print 'stars length is', len(solarwindsStars)
print 'titles length is', len(solarwindsTitle)

rows = zip(solarwindsTitle, solarwindsStars, solarwindsReviewers, solarwindsReviews)

with open('recording.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in rows:
        for thing in val:
            thing.encode('ascii', 'ignore')
        writer.writerow(val)
