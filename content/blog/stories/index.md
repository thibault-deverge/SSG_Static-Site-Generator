# 3 True (and Slightly Absurd) Tech Stories

[back home](/)

![meme](/images/meme.png)

Technology is full of brilliant ideas, but also surprising mistakes. Here are three real-world stories that show just how weird — and costly — things can get in tech.

---

## 1. The Mars Rover That Crashed Because of Units

In 1999, NASA lost the **Mars Climate Orbiter**, a \$125 million spacecraft, because of a simple unit mismatch. One team used **imperial units** (pound-seconds), while another used **metric** (newton-seconds). The result? A miscalculated trajectory that made the probe descend too low into Mars’ atmosphere, where it disintegrated.

This wasn’t a software bug — it was a human coordination bug. The failure became a classic case study in why documentation, testing, and communication matter.

> Source: [NASA's Metric Mishap](https://www.latimes.com/archives/la-xpm-1999-oct-01-mn-17288-story.html)

---

## 2. The Amazon Pricing Bot War

In 2011, two automated pricing bots on Amazon got locked in a loop. One bot was set to **price a book slightly higher than its competitor**, while the other tried to **undercut it by just a bit**.

The feedback loop led to the price of a biology book, _"The Making of a Fly"_, hitting **\$23,698,655.93** (plus shipping). The madness was only noticed when a curious user tweeted a screenshot. Needless to say, manual intervention was required.

> Source: [Amazon's \$23 Million Book](https://www.wired.com/2011/04/amazon-flies-24-million/)

---

## 3. The Developer Who Deleted His Entire Company

In 2016, a developer working on a Linux server accidentally executed the following command:

```bash
rm -rf /
```

That’s bad enough — but he also did it with **root privileges** and on a production server _without proper backups_. The command recursively deletes everything on the system, starting from the root directory. His cloud provider couldn’t help: the data was gone.

His company, which offered hosting services, lost everything in seconds. The developer wrote a blog post titled _"How I deleted my entire company"_, and it quickly went viral as a cautionary tale.

> Source: [The Developer Who Deleted His Company](https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/)

---

Even in a world of high-tech systems and automation, small mistakes — or a lack of coordination — can still lead to million-dollar failures. Let these stories be entertaining reminders that in tech, humility and backups go a long way.
