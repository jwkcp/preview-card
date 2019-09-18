You can create preview card(social card) very simple and easily. With Django? Fantastic!    

# preview-card

Anyone can obtain data(url, image, title, description, etc) easily from plain text for showing preview card like Twitter, Facebook newsfeed.

# Quick Start

```
from preview_card import cardview, MediaSourceType


result = cardview.get_data(plain_Text)
```

# Example

## CASE 1 - _if article url included_

**CODE:**

```
from preview_card import cardview, MediaSourceType

# Any Text you want including URL 
plain_text = "Hi, I read some article below. How do you think? https://www.nytimes.com/2019/09/17/technology/personaltech/iphone-11-review.html Is it cool or not?"

result = cardview.get_data(plain_Text)
```

**RESULT:**

```
ms_type     MediaSourceType.ARTICLE
url         https://www.nytimes.com/2019/09/17/technology/personaltech/iphone-11-review.html
image_url   https://static01.nyt.com/images/2019/09/17/business/17techfix2/17techfix2-facebookJumbo.jpg
title       IPhone 11 and 11 Pro Review: Thinking Differently in the Golden Age of Smartphones
desc        This is not your typical gadget review. That’s because it is time to rethink when to upgrade your iPhone.
error       
```

---


## CASE 2 - _if youtube url included_

**CODE**

```
from preview_card import cardview, MediaSourceType

# Any Text you want including URL 
plain_text = "Hi, I watch some video below. How do you think? https://www.youtube.com/watch?v=Jzz4AEIddzY Is it cool or not?"

result = cardview.get_data(plain_Text)
```

**RESULT**

```
ms_type     MediaSourceType.YOUTUBE
url         https://www.youtube.com/embed/Jzz4AEIddzY
image_url   
title       
desc        
error       
```
