---
date: 2022-06-14 18:00:00 +0200
title: "NetworkManager settings to improve GSM connection in the PinePhone"
layout: post
categories:
  - PinePhone
---

I am so happy of my PinePhone, but there is one particular issue that
significantly decreased its usability: connection to the GSM mobile network.
Fortunately, with some simple tweaks to NetworkManager it is possible to make
this operation much faster.

<!-- more -->

The problem I experienced is that the PinePhone (PP) is rather slow in
connecting to GSM and, to a much lesser extent, WiFi, after the phone comes out
of standby. The delay for WiFi occurs more strongly in PostmarketOS, while
Arch-based distros such as dreemurrs's and Manjaro are fast enough not to cause
problems. Let me clarify that even on pmOS is not such a big problem, perhaps it
takes 6 seconds instead of 3 (that's what I feel without actually timing it),
but it is enough to be noticeable. There's an issue about that[^pmwif] so
people are aware of this and it will be fixed one day.

The situation for GSM connection is really not so good, however. As a
disclaimer, I am running the default modem firmware that shipped with the PP,
and I don't know how Biktorgj's firmware fares in this regard. Secondly, I am
using a foreign SIM card (always within the EU), thus the delay I experience may
be related to roaming.

So there are actually two issues with the modem: first, it frequently dies when
the phone wakes up from standby, which causes a 30-or-so seconds delay before it
comes up again. Second, searching for a mobile operator to connect to also takes
30 or so seconds if not more. The first issue seems to be again related to pmOS,
while I suspect the second problem is due to roaming.

We can skip the search phase by forcing the modem to connect to an operator of
our choice. To do this, we first do a scan to see all available operators,
then connect to one of our choice:

```
> # first, get the modem number
> mmcli -L
    /org/freedesktop/ModemManager1/Modem/0 [QUALCOMM INCORPORATED] QUECTEL Mobile Broadband Module
>
> # scan available networks, large timeout because it's slow (but not that slow)
> mmcli --3gpp-scan -m 0 --timeout 900

  ---------------------
  3GPP scan | networks: 26202 - Vodafone (gsm, available)
            |           26203 - o2 - de (lte, available)
            |           26201 - TDG (gsm, available)
            |           26202 - Vodafone (lte, available)
            |           26201 - TDG (lte, current)
            |           26203 - o2 - de (gsm, available)
>
> # to connecto to another operator we need to disconnect first
> mmcli -m 0 --disable && \
    mmcli -m 0 --enable && \
    mmcli -m 0 --3gpp-register-in-operator 26201
successfully disabled the modem
successfully enabled the modem
successfully registered the modem
```

I tried several and found that TDG worked best, while o2 did not let me navigate
at all. At first I put these commands in a script that I ran every other time I
unlocked the phone, but there's actually a better way to do this via nmcli:

```
> sudo nmcli connection modify coopi gsm.network-id 26201
```

This will essentially force a connection to that operator automatically without
manual intervention. The connection `coopi` is named after the APN profile in
the settings. Something that I haven't managed to test yet is what happens when
this operator is not found, e.g. when traveling. Another setting that I found
useful was the automatic connection:

```
> sudo nmcli connection modify coopi connection.autoconnect yes
```

I found this to be off some time ago, perhaps in KDE but I don't remember
exactly. And finally enable roaming (fundamental in my case):

```
> sudo nmcli connection modify coopi gsm.home-only no
```

I haven't had any more delays or problems with these three commands on Manjaro,
which I think I will be driving for some time after extensively using pmOS.


[^pmwif]: https://gitlab.com/postmarketOS/pmaports/-/issues/973
