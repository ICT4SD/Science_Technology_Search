# Science & Technology Search Engine for Sustainable Development
Build a searchable collection of science and technology knowledge useful to implement the Sustainable Development Goals.

The internet has billions of pages. This project aims to build a curated collection of content relevant to sustainable development, keeping and categorizing content from high quality sources. Such as:

- Websites, papers and publications from recognized academic institutions
- Training materials from recognized online repositories
- Projects and tools from civil society
- Websites from government offices worldwide

For example, if you were to search for "child nutrition tools" the results set would be expected to include for example:
- Courses from edx.org, coursera.com, etc.
- Papers from the World Health Organization, UNICEF, Universities, and from journals in the Directory of Open Access Journals, etc.
- Projects from the Global Innovation Exchange, the Swedish International Development Cooperation Agency, etc.
- Videos, web, and other materials from governmental websites around the world.

##Getting started

Navigating the vast amount of content abailable on the Internet is daunting, a way to get started could be to narrow the collection to include only websites belonging to this narrow list of owners:

- [National Goverments](http://www.un.org/en/member-states/index.html), this is a list maintained by the United Nations listing the Permanent Missions of the Member States of the United Nations.
- [List of non-governmental organizations in consultative status with the Economic and Social Council of the United Nations](http://www.un.org/ga/search/view_doc.asp?symbol=E/2015/INF/5), this list was obtained from [here](http://csonet.org/).
- [List of academic institutions in the United Nations Academic Impact](https://academicimpact.un.org/sites/academicimpact.un.org/files/UNAI%20MEMBERS%20LIST%20September%202016.pdf), this list was obtained from [here](https://academicimpact.un.org)

##Classification of content

In addition to being able to find content based on keywords, it would be useful to be able to narrow down search results by the type of content found. These are some ideas for classification:

- By type of media: documents, videos, images, etc.
- By category of content: training material, laws or regulations, research papers, etc.
- By language
- By target audience: for children, for universtity students, for researchers, for policymakers, for practitioners, etc.
- By topic: health, poverty, energy, climate, water, etc.

Examples
--------
[1) Sentence tagging and visualization](https://unite.un.org/ideas/content/links-sustainable-cities)  

[2) Sentence tagging and search](https://unite.un.org/ideas/content/linkssdgs-tagger)  

3) This is an example of how documents might look like in the search engine server:

    {
      "_index" : "sti_search",
      "_type" : "site",
      "_id" : "0",
      "_score" : 1.0,
      "_source" : {
        "Country Origin" : [ "India" ],
        "Entity Origin" : [ "Permanent Mission to the UN", "Ministry of Foreign Affairs" ],
        "Domain Origin" : [ ".gov.in"],
        "Title" : [ "Analysis: What this technology means for the future of the console health" ],
        "Content" : [ "Company co-founder and current board member is going to offload some of his stock. The CEO and is the companys largest individual shareholder, said Thursday that he plans to sell a new device for poverty reduction." ],
        "url" : "https://example.un.org/12345",
        "Language" : [ "English", "French" ],
        "Resource Type" : [ "News", "Projects" ],
        "Resource Format" : [ "Webpage", "Video" ],
        "SDG Goal" : [ "Health", "Poverty" ],
        "Indexed Date" : "2015-31-12"
      }

You can see a demo interactive search engine server here: (with fake content)  http://132.148.64.70:9200/_search?pretty=true&q=*:*


NOTE: Since the international community has agreed on the 17 Sustainable Development Goals for the year 2030, it would be ideal to have a categorization of content according to these goals as well. See the goals below:
<a href="http://www.un.org/sustainabledevelopment">
    <img src="https://ict4sd.github.io/img/E_2016_SDG_Poster_all_sizes_without_UN_emblem_Letter.png" alt="SDG poster">
</a>


