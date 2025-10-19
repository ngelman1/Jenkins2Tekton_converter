From: Snapshot-Content-Location:
https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html/cicd/migrating-from-jenkins-to-tekton
Subject:
=?utf-8?Q?Chapter=C2=A03.=C2=A0Migrating=20from=20Jenkins=20to=20Tekton?=
=?utf-8?Q?=20\|=20CI/CD=20\|=20OpenShift=20Container=20Platform=20\|=204.10?=
=?utf-8?Q?=20\|=20Red=20Hat=20Documentation?= Date: Wed, 13 Aug 2025
10:03:43 +0300 MIME-Version: 1.0 Content-Type: multipart/related;
type=\"text/html\";
boundary=\"\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--\"
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/html Content-ID: Content-Transfer-Encoding:
quoted-printable Content-Location:
https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html/cicd/migrating-from-jenkins-to-tekton

::: {.3D\"pzn1827950-banner dx-bg-white="" dx-relative="" dx-pl-2="" lg:="dx-pl-0" dx-py-2="" dx-flex="" dx-flex-row="" dx-justify-start="" lg:dx-justify-center="" l="g:dx-items-center" dx-border="" dx-border-gray-30\"=""}
::: {.3D\"dx-flex dx-justify-start="" dx-items-start\"=""}
![3D\"Red](3D%22https://www.redhat.com/rhdc/managed-files/rhel-logo-img=){.3D\"rh-target-pzn1827950-logo
dx-relative="" dx-mr-2="xl:dx-mr-4\"" .png\"="" width="3D\"48\""
height="3D\"48\"" hat="" summit="" and="" ansiblefest="" logo=">
            </div>
            <div class=3D" dx-flex="" dx-flex-col=""
lg:dx-flex-row\"=""}

Upgrade your innov= ation foundation with Red Hat Enterprise Linux 10

[ ]{#3D\"container\" .3D\" part="3D\"container\"" svg="" \"=""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTMwLjU2IiAxNC45NCAxOS49IjkxNSIgNC4yOTNhMSAxIDAgMSAwIDE4LjUgNS43MDdsMjcuNzkzIDE1aDIuMjA3YTEgMSAwIDAgMCAwIDJoMjUuNTg2bDE4LjUgMjY9Ii4yOTNhMSIgMSAwIDEgMCAxLjQxNCAxLjQxNGwzMC41NiAxNy4wNjFhMS41MDEgMS41MDEgMCAwIDAgMC0yLjEyMXoiPjwvcGF0aD49Cjwvc3ZnPg==)
:::

[Browse the new
features](3D%22https://www.redhat.com/en/resources/new-in-e=){nterprise-linux-10-datasheet?percmp="3DRHCTG0250000447871\""
analytics-te="xt=3D\"Browse" the="" new="" features\"=""
analytics-linktype="3D\"cta\"" analyti="cs-category=3D\"pzn1827950|Docs"
announcement="" customer=" data-analytics-state=3D"
personalized|pzn1827950|docs="" cp|rhel="" 10="" announcem="ent"
banner|rhel="" customer\"=""}
:::

![3D\"close](3D%22https://static.redhat.com/libs/redhat/rh-ic=){.3D\"dx-block\"
onfont="" latest="" svg="" web-icon-close.svg\"="" height="3D\"20\""
widt="h=3D\"20\"" banner\"=""}
:::

::: {#3D\"__nuxt\"}
::: {data="-v-b258bd1d=3D\"\""}
[Skip to
navigation](3D%22https://docs.redhat.c=){#3D\"global-skip-to-nav\"
.3D\"skip-link om="" en="" documentation=""
openshift_container_platform="" 4.10="" html="" cicd=""
migrating-f="rom-jenkins-to-tekton#pfe-navigation\""
visually-hidden\"="" d="ata-v-b258bd1d=3D\"\""}[Skip to
content](3D%22https://docs.redhat.co=){.3D\"skip-link m="" en=""
documentation="" openshift_container_platform="" 4.10="" html="" cicd=""
migrating-fr="om-jenkins-to-tekton#main-content\"" visually-hidden\"=""
data="-v-b258bd1d=3D\"\""}

Featured links

-   [](3D%22https://ww=){.3D\"upper-nav-links\" w.redhat.com="" en=""
    analytics-text="3D\"RH=" summit\"=""
    analytics-category="3D\"Featured" links\"="" v-b258bd1d="3D\"\""}\<=
    /li\>
-   [Support](3D%22https://access.redhat.com/%22){.=3D\"upper-nav-links\"
    analytics-text="3D\"Support\"" analytics-categor="y=3D\"Featured"
    links\"="" v-b258bd1d="3D\"\""}
-   [Console](3D%22https://console.redhat.com/%22){.3D\"upper-nav-links\"
    analytics-category="3D\"Featured" links\"=""
    d="ata-v-b258bd1d=3D\"\""}
-   [Developers](3D%22htt=){.3D\"upper-nav-links\" ps:=""
    developers.redhat.com="" \"="" analytics-text="=3D\"Developers\""
    analytics-category="3D\"Featured" links\"="" v-b258bd1d="=3D\"\""}
-   [Start a trial](3D%22https://www.re=){.3D\"upper-nav-links\"
    dhat.com="" en="" products="" trials\"=""
    analytics-text="=3D\"Start" a="" trial\"=""
    analytics-category="3D\"Featured" links\"="" v-b258bd="1d=3D\"\""}
-   All
    Red Hat![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1cHBlci09IiBuYXYtYXJyb3ciIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiB3aWR0aD0iM0QmcXVvdDsxMDI0JnF1b3Q7IiBoZWlnaHQ9IjNEJnF1b3Q7MTA9IiAyNCIgdmlld2JveD0iM0QmcXVvdDswIiAwIDEwMjQgMTAyNCIgYXJpYS1oaWRkZW49IjNEJnF1b3Q7dHJ1ZSZxdW90OyIgZGF0YS12LWIyNThiZDFkPSIzRCZxdW90OyZxdW90OyI+PHBhPSB0aCBkPSIzRCZxdW90O004MTAuNjQyIiA1MTEuNTU3YzAgOC45MDUtMy40NDcgMTYuNzc2LTEwLjI4NCAyMy42MTNsMzIyLjMxIDEwMTMuMjE2PSJjLTYuODM1IiA2LjgzNy0xNC43MDYgMTAuMjg0LTIzLjYxIDEwLjI4NHMtMTYuNzc2LTMuNDQ3LTIzLjYxMy0xMC4yODRsLTUxLjMwPSIzLTUxLjMwM2MtNi44MzctNi44MzctMTAuMjg0LTE0LjcwNy0xMC4yODQtMjMuNjEyczMuNDQ3LTE2Ljc3NSIgMTAuMjg0LTIzLjYxPSJMNjI2Ljk3MiIgNTExLjUgMjIzLjc4NCAxMDguMzFjLTYuODM3LTYuODM1LTEwLjI4NC0xNC43MDYtMTAuMjg0LTIzLjYxczMuNDQ3PSItMTYuNzc2IiAxMC4yODQtMjMuNjEzbDUxLjMwMy01MS4zMDNjMjgxLjkyNCAyLjk0NyAyODkuNzk0LS41IDI5OC43LS41czE2Ljc3PSI1IiAzLjQ0NyAyMy42MSAxMC4yODRsODAwLjM2IDQ4Ny44M2M2LjgzNyA2LjgzNyAxMC4yODQgMTQuNzA4IDEwLjI4NCAyMy42MTN2PSIuMTE0JnF1b3Q7IiBkYXRhLXYtYjI1OGJkMWQ9IjNEJnF1b3Q7JnF1b3Q7Ij48L3BhdGg+PC9zdmc+){.3D\"upper-=}

    ::: {#3D\"all-red-hat-con= .3D\"upper-nav-dropdown-container\" tent\"="" v-b258bd1d="3D\"\""}
    -   [For cus= tomers]{v-b258bd1d="3D\"\""}
        -   [Customer support](3D%22h=){ttps:="" access.redhat.com=""
            pzn-audience="3D\"customers\"" anal="ytics-category=3D\"All"
            red="" hat|for="" customers\"=""
            analytics-text="3D\"Custome=" r="" support\"=""
            v-b258bd1d="3D\"\""}
        -   [Subscription=
            management](3D%22https://access.redhat.com/management%22){pzn-audience="=3D\"customers\""
            analytics-category="3D\"All" red="" hat|for=""
            customers\"="" a="nalytics-text=3D\"Subscription"
            management\"="" v-b258bd1d="3D\"\""}
        -   [Support Cases](3D%22https://access.redh=){at.com=""
            support="" pzn-audience="3D\"customers\""
            analytics-catego="ry=3D\"All" red="" hat|for=""
            customers\"="" analytics-text="3D\"Support" cases\"=""
            data="-v-b258bd1d=3D\"\""}
        -   [Red Hat Ecosystem Catalog](3D%22=){https:=""
            catalog.redhat.com="" \"="" analytics-category="3D\"All"
            red="" hat|for="" cus="tomers\"" analytics-text="3D\"Red"
            hat="" ecosystem="" catalog\"="" v-b258bd1d="=3D\"\""}
        -   [Find a
            partner]{hr="ef=3D\"https://catalog.redhat.com/partners\""
            analytics-category="3D\"All" r="ed" hat|for=""
            customers\"="" analytics-text="3D\"Find" a="" partner\"=""
            v-b258bd1="d=3D\"\""}
    -   [For partners]{data="-v-b258bd1d=3D\"\""}
        -   [Partner=
            portal](3D%22https://connect.redhat.com/partner-admin/dashboard%22){d="ata-pzn-audience=3D\"partners\""
            analytics-category="3D\"All" red="" hat|for="" pa="rtners\""
            analytics-text="3D\"Partner" portal\"=""
            v-b258bd1d="3D\"\""}
        -   [Partner support](3D%22https://connect.redhat.=){com=""
            en="" pzn-audience="3D\"partners\""
            analytics-category="3D\"A=" ll="" red="" hat|for=""
            partners\"="" analytics-text="3D\"Partner" support\"=""
            v-b25="8bd1d=3D\"\""}
        -   [Become a partner](3D%22http=){s:="" connect.redhat.com=""
            pzn-audience="3D\"partners\"" analytics-cate="gory=3D\"All"
            red="" hat|for="" partners\"="" analytics-text="3D\"Become"
            a="" partner="" \"="data-v-b258bd1d=3D\"\""}
    -   [Try, buy, & sell]{v-b258bd1d="3D\"\""}
        -   [Red Hat Store](3D%22https://www.redhat.com/en/st=){ore\"=""
            analytics-category="3D\"All" red="" hat|try,="" buy,=""
            &amp;="" sell\"="" anal="ytics-text=3D\"Red" hat=""
            store\"="" v-b258bd1d="3D\"\""}
        -   [Contact
            Sales](3D%22https://www.redhat.com/en/contact%22){da="ta-analytics-category=3D\"All"
            red="" hat|try,="" buy,="" &amp;="" sell\"=""
            analytics-t="ext=3D\"Contact" sales\"=""
            v-b258bd1d="3D\"\""}
        -   [Start a
            trial](3D%22https://www.redhat.com/en/products/trials%22){red=""
            hat|try,="" buy,="" &amp;="" sell\"=""
            analytics-text="=3D\"Start" a="" trial\"=""
            v-b258bd1d="3D\"\""}
    -   [Training and certification](3D%22https://www.red=){hat.com=""
        en="" services="" training-and-certification\"=""
        analytics-category="3D\"=" all="" red="" hat|learning=""
        resources\"="" analytics-text="3D\"Training" and=""
        certifi="cation" \"="" v-b258bd1d="3D\"\""}
    -   [Hybrid cloud learning
        hub](3D%22https://cloud.redhat.com/learn%22){analytics-ca="tegory=3D\"All"
        red="" hat|learning="" resources\"=""
        analytics-text="3D\"Hybrid" clo="ud" learning="" hub\"=""
        v-b258bd1d="3D\"\""}
    -   [Red Hat
        TV](3D%22https://www.redhat.com/en/tv%22){analytics-category="=3D\"All"
        red="" hat|learning="" resources\"="" analytics-text="3D\"Red"
        hat="" tv\"="" data="-v-b258bd1d=3D\"\""}
    -   [Architecture
        center](=3D%22https://www.redhat.com/architect/portfolio/%22){analytics-category="3D="
        \"all="" red="" hat|learning="" resources\"=""
        analytics-text="3D\"Architecture" center=" data-v-b258bd1d=3D"
        \"=""}

    [Open source communities]{v-b258bd1d="3D\"\""}
    -   [Global= advocacy](3D%22https://access.redhat=){.com=""
        accelerators\"="" analytics-category="3D\"All" red=""
        hat|open="" source="" commu="nities\""
        analytics-text="3D\"Global" advocacy\"="" v-b258bd1d="3D\"\""}
    -   [How we contribute](3D%22https://www.redhat.co=){m="" en=""
        about="" our-community-contributions\"=""
        analytics-category="3D\"All" red="Hat|Open" source=""
        communities\"="" analytics-text="3D\"How" we="" contribute\"=""
        data="-v-b258bd1d=3D\"\""}
    :::

\<= /div\>
:::

::: {.3D\"pfe-navigation-content-page-container\"= v-b258bd1d="3D\"\""}
::: {#=3D\"pfe-navigation__logo-wrapper\" .3D\"pfe-navigation__logo-wrapper\" da="ta-v-b258bd1d=3D\"\""}
\<= /a\>
:::

::: 3D"pfe-navigation__burger-icon"
:::

Menu

::: {#3D\"mobile__dropdown\" .3D\"pfe-navigation__outer-menu-wrapper pfe-navigation__dropdown="-wrapper--invisible\"" part="3D\"mobile__dropdown\"" aria="-hidden=3D\"true\"" tabindex="3D\"-1\""}
::: {#3D\"pfe-navigation__outer-menu-wrapper__inner\" .3D\"pfe-navigation__outer-menu-wrapp= part="3D\"pfe-navig=" ation__outer-menu-wrapper__inner\"="" er__inner\"=""}
::: {#3D\"pfe-navigation__search-wrapper--xs\" part="3D\"pfe-navigation=" __search-wrapper--xs\"=""}
:::

-   AI

    ::: {#3D\"main-menu__dropdo= .3D\"pfe-navigation__dropdown-w= pa="rt=3D\"pfe-navigation__dropdown-wrapper\"" rapper="" pfe-navigation__dropdown-wrapper--invisible\"="" wn--ai\"="" aria-hidden="3D\"true\"" tabindex="3D\"-1\""}
    ::: {.3D\"pfe-navigation-g= rid="" pfe-navigation__dropdown\"="" v-b258bd1d="3D\"\""}
    ::: {.3D\"pfe-naviga= tion--column="" desktop-col-span-4="" tablet-col-span-all\"="" v-b258bd1d="3D\"\""}
    \<= slot name=3D\"custom-nav-ai\"\>
    :::
    :::
    :::
-   Learn

    ::: {#3D\"main-menu__dropdown--Learn\" .3D\"pfe-navigation__dropdown-wrapper part="3D\"pfe-navigation__dropdo=" wn-wrapper\"="" pfe-navigation__dropd="own-wrapper--invisible\"" aria-hidden="3D\"tr=" ue\"="" tabindex="3D\"-1\""}
    ::: {.3D\"pfe-navigation-grid pfe-navigation__dropd="own\"" v-b258bd1d="3D\"\""}
    ::: {.3D\"pfe-navigation--column desktop-col-="span-4" tablet-col-span-all\"="" v-b258bd1d="3D\"\""}
    :::
    :::
    :::
-   Documentation

    ::: {#3D\"main-menu__dropdown--Docume= .3D\"pfe-navigation__dropdown-wrapper part="3D\"pfe-=" navigation__dropdown-wrapper\"="" pfe="-navigation__dropdown-wrapper--invisible\"" ntation\"="" aria-hidden="3D\"true\"" tabindex="3D\"-1\""}
    ::: {.3D\"pfe-navigation-= grid="" pfe-navigation__dropdown\"="" v-b258bd1d="3D\"\""}
    ::: {.3D\"pfe-navig= ation--column="" desktop-col-span-4="" tablet-col-span-all\"="" v-b258bd1d="3D\"\""}
    =
    :::
    :::
    :::

=

::: {#3D\"pfe-navi= .3D\"pfe-navigation__secondary-links-wrapper\" gation__secondary-links-wrapper\"="" part="3D\"pfe-navigation__secondary-links-wr=" apper\"=""}
<div>

::: 3D"pfe-icon--fallback"
:::

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgaGVpZ2h0PSIzRCZxdW90OzIwJnF1b3Q7IiB3aWR0aD0iM0QmcXVvdDsyMCZxdW90OyI+CiAgPGZpbHRlciBjb2xvci1pbnRlcnBvbGF0aW9uLWZpbHRlcnM9IjNEJnF1b3Q7c1JHQiZxdW90OyIgeD0iM0QmcXVvdDswJnF1b3Q7IiB5PSIzRCZxdW90OzAmcXVvdDsiIGhlaWdodD0iM0QmcXVvdDsxMD0iIDAlIiB3aWR0aD0iM0QmcXVvdDsxMDAlJnF1b3Q7IiBpZD0iM0QmcXVvdDtmaWx0ZXItMzc4MDc2NDMmcXVvdDsiPgogICAgPGZlZmxvb2QgcmVzdWx0PSIzRCZxdW90O0NPTE9SJnF1b3Q7Ij48L2ZlZmxvb2Q+CiAgICA8ZmVjb21wb3NpdGUgb3BlcmF0b3I9IjNEJnF1b3Q7aW4mcXVvdDsiIGluPSIzRCZxdW90O0NPTE9SJnF1b3Q7IiBpbjI9IjNEJnF1b3Q7U291cmNlQWxwaGEmcXVvdDsiPjwvZmVjb21wbz0+CiAgPC9maWx0ZXI+CiAgPGltYWdlIHhsaW5rOmhyZWY9IjNEJnF1b3Q7aHR0cHM6Ly9hY2Nlc3MucmVkaGF0LmNvbS93ZWJhc3NldHMvYXZhbG9uL2ovbGliL3JoLT0iIGljb25mb250LXN2Z3Mgd2ViLWljb24tc2VhcmNoLnN2ZyIgd2lkdGg9IjNEJnF1b3Q7MTAwJSZxdW90OyIgaGVpZ2h0PSIzRCZxdW90OzEwMCUmcXVvdDsiIHN0eWxlPSIzRCZxdW90Oz0iIGZpbHRlcjogdXJsKCZxdW90OyNmaWx0ZXItMzc4MDc2NDMmcXVvdDspOyI+PC9pbWFnZT4KPC9zdmc+)
[Search]{#3D\"secondary-links__button--search-text\" part="3D\"secon="
dary-links__button--search-text\"=""}

::: {#3D\"p= .3D\"pfe-navigation__dropdown-wrapper pfe-navigation__dr="opdown-wrapper--search" pfe-navigation__dropdown-wrapper--invisible\"="" fe-navigation__search-wrapper--md\"="" part="3D\"pfe-navigation__search-wrapper--=" md\"="" tabindex="3D\"-1\"" aria-hidden="3D\"true\""}
=20
:::

</div>
:::
:::
:::

::: {#3D\"pfe-navigation__account-wrapper\" .3D\"pfe-navigation__account-wrapper pfe-navigation__account-wra="pper--logged-in\"" part="3D\"pfe-navigat=" ion__account-wrapper\"=""}
[](3D%22https://sso.redhat.com/aut=){#3D\"pfe-navigation__log-in-link\"
.3D\"pfe-navigation__log= h="" realms="" redhat-external="" protocol=""
openid-connect="" auth?client_id="3De50f6924-="
21d9-401d-8c6c-76104e52ab80&amp;redirect_uri="3Dhttps%3A%2F%2Fdocs.redhat.co="
m%2fen%2fdocumentation%2fopenshift_container_platform%2f4.10%2fhtml%2fcicd%="2Fmigrating-from-jenkins-to-tekton&state=3D5a6a065b-aaa1-48d8-bf04-8d65="
37e2d7fc&amp;response_mode="3Dquery&response_type=3Dcode&scope=3Dope="
nid%20email%20profile%20id.organization%20id.sub&amp;nonce="3Dbedb6684-613a-="
4957-8fcd-745df0701fe8&amp;code_challenge="3DK1hDiMWUcApOgRnukZs652qLCgn_vSk="
w2wkmk31qygo&amp;code_challenge_method="3DS256\"" -in-link\"=""
analytics-level="3D\"1\"" analytics-text="3D\"Log"
an="alytics-category=3D\"Log" in\"=""}

::: 3D"pfe-icon--fallback"
:::

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgaGVpZ2h0PSIzRCZxdW90OzIwJnF1b3Q7IiB3aWR0aD0iM0QmcXVvdDsyMCZxdW90OyI+CiAgPGZpbHRlciBjb2xvci1pbnRlcnBvbGF0aW9uLWZpbHRlcnM9IjNEJnF1b3Q7c1JHQiZxdW90OyIgeD0iM0QmcXVvdDswJnF1b3Q7IiB5PSIzRCZxdW90OzAmcXVvdDsiIGhlaWdodD0iM0QmcXVvdDsxMD0iIDAlIiB3aWR0aD0iM0QmcXVvdDsxMDAlJnF1b3Q7IiBpZD0iM0QmcXVvdDtmaWx0ZXItMDQwNTgzNTUmcXVvdDsiPgogICAgPGZlZmxvb2QgcmVzdWx0PSIzRCZxdW90O0NPTE9SJnF1b3Q7Ij48L2ZlZmxvb2Q+CiAgICA8ZmVjb21wb3NpdGUgb3BlcmF0b3I9IjNEJnF1b3Q7aW4mcXVvdDsiIGluPSIzRCZxdW90O0NPTE9SJnF1b3Q7IiBpbjI9IjNEJnF1b3Q7U291cmNlQWxwaGEmcXVvdDsiPjwvZmVjb21wbz0+CiAgPC9maWx0ZXI+CiAgPGltYWdlIHhsaW5rOmhyZWY9IjNEJnF1b3Q7aHR0cHM6Ly9hY2Nlc3MucmVkaGF0LmNvbS93ZWJhc3NldHMvYXZhbG9uL2ovbGliL3JoLT0iIGljb25mb250LXN2Z3Mgd2ViLWljb24tdXNlci5zdmciIHdpZHRoPSIzRCZxdW90OzEwMCUmcXVvdDsiIGhlaWdodD0iM0QmcXVvdDsxMDAlJnF1b3Q7IiBzdHlsZT0iM0QmcXVvdDtmaT0iIGx0ZXI6IHVybCgmcXVvdDsjZmlsdGVyLTA0MDU4MzU1JnF1b3Q7KTsiPjwvaW1hZ2U+Cjwvc3ZnPg==)Log
In

::: {#3D\"pfe-navigation__account-dropdown-wrapper\" .3D\"pfe-navigation__dropdown-wrapper part="3D\"pfe-naviga=" tion__account-dropdown-wrapper\"="" p="fe-navigation__dropdown-wrapper--account" pfe-navigation__dropdown-wrapper--="invisible\"" aria-hidden="3D\"true\"" tabindex="3D\"-1\""}
:::
:::

::: {#3D\"pfe-navigation__logo-wrapper\" .3D\"pfe-nav= igation__logo-wrapper\"="" v-b258bd1d="3D\"\""}
[![3D\"Red](3D%22https://docs.redhat.com/Logo-Red_Hat-Docum=){.=3D\"pfe-navigation__logo-image
pfe-navigation__logo-image--screen=""
pfe-navig="ation__logo-image--small\"" entation-a-reverse-rgb.svg\"=""
width="3D\"240\"" height="3D\"40\"" hat="" docu="mentation\""
v-b258bd1d="3D\"\""}](3D%22https://docs.redhat.=){.3D\"pfe-navigation__logo-link\"
com="" en\"="" v-b258bd1d="3D\"\""}
:::

-   ::: {slot="=3D\"trigger\"" v-b258bd1d="3D\"\""}
    [AI](3D%22https://docs.redhat.com/%22){.3D\"pfe-navigation__menu-link\"
    data="-v-b258bd1d=3D\"\""}
    :::

-   ::: {slot="3D\"trigger\"" v-b="258bd1d=3D\"\""}
    [Learn](3D%22https://docs.redhat.com/%22){v-b258bd1d="3D\"\""
    clas="s=3D\"pfe-navigation__menu-link\""}
    :::

::: {v-b258bd1d="3D\"\"" slot="3D\"secondary-links\"" cl="ass=3D\"hidden-at-mobile\""}
::: {#3D\"search-form-global_search\" .3D\"search-container v-7ec4cdc4="3D\"\"" v-b258bd1d="=3D\"\"" search-box=" open-search-box=3D" true\"=""}
::: {.3D\"searc= v-7ec4cdc4="3D\"\"" h-box\"=""}
::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7bTMxLjc5NSIgMzAuMjA1LTg9Ii44NS04Ljg1QTEyLjkzNiIgMTIuOTM2IDAgMCAwIDI2IDEzYzAtNy4xNjgtNS44MzEtMTMtMTMtMTNzMCA1LjgzMiAwIDEzczUuODM9IjIiIDEzIDEzIDEzYzMuMTggMCA2LjA5My0xLjE1MSA4LjM1NS0zLjA1NGw4Ljg1IDguODVhMS4xMjEgMS4xMjEgMCAwIDAgMS41OT0iMGMuNDQtLjQ0LjQ0LTEuMTUyIiAwLTEuNTkxem0xMyAyNGM2LjkzNSAyNCAyIDE5LjA2NSAyIDEzczYuOTM1IDIgMTMgMnMxMSA0Lj0iOTM1IiAxMSAxMS00LjkzNSAxMS0xMSAxMXoiPjwvcGF0aD48L3N2Zz4=)
:::

\<= rh-button data-v-7ec4cdc4=3D\"\" class=3D\"form-submit-btn\"
disabled=3D\"\" vari= ant=3D\"tertiary\"\>

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTMwLjU2IiAxNC45NCAxOS49IjkxNSIgNC4yOTNhMSAxIDAgMSAwIDE4LjUgNS43MDdsMjcuNzkzIDE1aDIuMjA3YTEgMSAwIDAgMCAwIDJoMjUuNTg2bDE4LjUgMjY9Ii4yOTNhMSIgMSAwIDEgMCAxLjQxNCAxLjQxNGwzMC41NiAxNy4wNjFhMS41MDEgMS41MDEgMCAwIDAgMC0yLjEyMXoiPjwvcGF0aD49Cjwvc3ZnPg==)
:::
:::

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTE3LjU5IiAxNiAyOC43OTY9IjQuNzk1YTEuMTI0IiAxLjEyNCAwIDEgMC0xLjU5LTEuNTlsMTYgMTQuNDA5IDQuNzk1IDMuMjA1YTEuMTI0IDEuMTI0IDAgMSAwLT0iMS41OSIgMS41OWwxNC40MDkgMTYgMy4yMDUgMjcuMjA1YTEuMTI0IDEuMTI0IDAgMSAwIDEuNTkgMS41OWwxNiAxNy41OTFsMTEuMj0iMDUiIDExLjIwNGExLjEyMSAxLjEyMSAwIDAgMCAxLjU5IDBjLjQ0LS40NC40NC0xLjE1MSAwLTEuNTlsMTcuNTkxIDE2eiI+PC9wYT0+PC9zdmc+)
:::
:::
:::

::: {.3D\"hidden-at-mobile v-b258bd1d="3D\"\"" slo="t=3D\"secondary-links\"" pfe-navigation__custom-drop="down__wrapper--full" pfe-navigation__custom-dropdown__wrapper\"=""}
::: 3D"secondary-link__icon-wrapper"
::: 3D"pfe-icon--fallback"
:::

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgaGVpZ2h0PSIzRCZxdW90OzIwJnF1b3Q7IiB3aWR0aD0iM0QmcXVvdDsyMCZxdW90OyI+CiAgPGZpbHRlciBjb2xvci1pbnRlcnBvbGF0aW9uLWZpbHRlcnM9IjNEJnF1b3Q7c1JHQiZxdW90OyIgeD0iM0QmcXVvdDswJnF1b3Q7IiB5PSIzRCZxdW90OzAmcXVvdDsiIGhlaWdodD0iM0QmcXVvdDsxMD0iIDAlIiB3aWR0aD0iM0QmcXVvdDsxMDAlJnF1b3Q7IiBpZD0iM0QmcXVvdDtmaWx0ZXItNzg2MTEzNzAmcXVvdDsiPgogICAgPGZlZmxvb2QgcmVzdWx0PSIzRCZxdW90O0NPTE9SJnF1b3Q7Ij48L2ZlZmxvb2Q+CiAgICA8ZmVjb21wb3NpdGUgb3BlcmF0b3I9IjNEJnF1b3Q7aW4mcXVvdDsiIGluPSIzRCZxdW90O0NPTE9SJnF1b3Q7IiBpbjI9IjNEJnF1b3Q7U291cmNlQWxwaGEmcXVvdDsiPjwvZmVjb21wbz0+CiAgPC9maWx0ZXI+CiAgPGltYWdlIHhsaW5rOmhyZWY9IjNEJnF1b3Q7aHR0cHM6Ly9hY2Nlc3MucmVkaGF0LmNvbS93ZWJhc3NldHMvYXZhbG9uL2ovbGliL3JoLT0iIGljb25mb250LXN2Z3Mgd2ViLWljb24tZ2xvYmUuc3ZnIiB3aWR0aD0iM0QmcXVvdDsxMDAlJnF1b3Q7IiBoZWlnaHQ9IjNEJnF1b3Q7MTAwJSZxdW90OyIgc3R5bGU9IjNEJnF1b3Q7Zj0iIGlsdGVyOiB1cmwoJnF1b3Q7I2ZpbHRlci03ODYxMTM3MCZxdW90Oyk7Ij48L2ltYWdlPgo8L3N2Zz4=)
:::

English

::: {#3D\"pfe-navigation= .3D\"pfe-navigation__dropdown-wrapper __custom-dropdown--english\"="" pfe-n="avigation__custom-dropdown--full" pfe-navigation__dropdown-wrapper--invisibl="e\"" aria-hidden="3D\"true\"" tabindex="3D\"-1\""}
::: {#3D\"dropdow= n-container\"=""}
:::

::: {.3D\"language-picker\" v-b258bd1d="3D\"\""}
### Select your language {#select-your-language da="ta-v-b258bd1d=3D\"\""}

-   [English](3D%22https://docs.redhat.com/=){v-b258bd1d="3D\"\"" en=""
    documentation="" openshift_container_platform="" 4.10="" html=""
    cicd="" migrating-from="-jenkins-to-tekton\""}
-   [Fran=C3=A7ais=](3D%22https://docs.redhat.com/fr/documentation/openshift_contai=){v-b258="bd1d=3D\"\""
    ner_platform="" 4.10="" html="" cicd=""
    migrating-from-jenkins-to-tekton\"=""}
-   [=ED=95=9C=EA=B5=AD=EC=96=B4](3D%22https://d=){v-b258bd1d="3D\"\""
    ocs.redhat.com="" ko="" documentation=""
    openshift_container_platform="" 4.10="" html=""
    cicd="/migrating-from-jenkins-to-tekton\""}
-   [=E6=97=A5=E6=9C=AC=E8=AA=9E](3D%22https://docs.redhat.co=){v-b258bd1d="3D\"\""
    m="" ja="" documentation="" openshift_container_platform="" 4.10=""
    html="" cicd="" migrating-fr="om-jenkins-to-tekton\""}
-   [=E4=B8=AD=E6=96=87
    (=E4=B8=AD=E5=9B=BD)](3D%22https://docs.redhat.com/zh-cn/docum=){v-b258bd1d="3D\"\""
    entation="" openshift_container_platform="" 4.10="" html="" cicd=""
    migrating-from-jenkins="-to-tekton\""}
-   [Deutsch](3D%22https://docs.redhat.com/de/docume=){v-b258bd1d="3D\"\""
    ntation="" openshift_container_platform="" 4.10="" html="" cicd=""
    migrating-from-jenkins-="to-tekton\""}
-   [Italiano](3D%22https://docs.redhat.com/it/documentation/openshift_container_platf=){v-b258bd1d="3D\"\"="
    orm="" 4.10="" html="" cicd=""
    migrating-from-jenkins-to-tekton\"=""}
-   [Portugu=C3=AAs](3D%22https://docs.redhat.com=){v-b258bd1d="3D\"\""
    pt-br="" documentation="" openshift_container_platform="" 4.10=""
    html="" cicd="" migrating-="from-jenkins-to-tekton\""}
-   [Es=
    pa=C3=B1ol](3D%22https://docs.redhat.com/es/documentation/opens=){==""
    v-b258bd1d="3D\"\"" hift_container_platform="" 4.10="" html=""
    cicd="" migrating-from-jenkins-to-tekton\"=""}
:::
:::
:::

<div>

::: {#3D\"wrapper\" .3D\"pfe-navigation__dropdown\"}
::: {.3D\"user= -info\"=""}
### Naomi Gelma= n {#naomi-gelma-n .3D\"user-info__full-name\"}

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgPSBoZWlnaHQ9IjNEJnF1b3Q7MTAwJSZxdW90OyIgd2lkdGg9IjNEJnF1b3Q7MTAwJSZxdW90OyIgdmlld2JveD0iM0QmcXVvdDswIiAwIDUxMiA1MTIiIGFyaWEtaGlkZGVuPSIzRCZxdW90O3RydWUmcXVvdDs9IiByb2xlPSIzRCZxdW90O2ltZyZxdW90OyIgc3R5bGU9IjNEJnF1b3Q7dmVydGljYWwtYWxpZ246IiAtMC4xMjVlbTsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3I9IiBnIDIwMDAgc3ZnIj48cGF0aCBkPSIzRCZxdW90O000OTcuOSIgMTQyLjFsLTQ2LjEgNDYuMWMtNC43IDQuNy0xMi4zIDQuNy0xNyAwbC0xMTEtPSIxMTFjLTQuNy00LjctNC43LTEyLjMiIDAtMTdsNDYuMS00Ni4xYzE4LjctMTguNyA0OS4xLTE4LjcgNjcuOSAwbDYwLjEgNjAuMWMxPSI4LjgiIDE4LjcgMTguOCA0OS4xIDAgNjcuOXptMjg0LjIgOTkuOGwyMS42IDM2Mi40LjQgNDgzLjljLTIuOSAxNi40IDExLjQgMzAuPSI2IiAyNy44IDI3LjhsMTIxLjUtMjEuMyAyNjIuNi0yNjIuNmM0LjctNC43IDQuNy0xMi4zIDAtMTdsLTExMS0xMTFjLTQuOC00LjctPSIxMi40LTQuNy0xNy4xIiAwem0xMjQuMSAzMzkuOWMtNS41LTUuNS01LjUtMTQuMyAwLTE5LjhsMTU0LTE1NGM1LjUtNS41IDE0LjMtPSI1LjUiIDE5LjggMHM1LjUgMTQuMyAwIDE5LjhsLTE1NCAxNTRjLTUuNSA1LjUtMTQuMyA1LjUtMTkuOCAwem04OCA0MjRoNDh2MzYuPSIzbC02NC41IiAxMS4zLTMxLjEtMzEuMWw1MS43IDM3Nmg4OHY0OHoiIHRyYW5zZm9ybT0iM0QmcXVvdDsmcXVvdDsiPjwvcGF0aD48L3N2Zz4=)Edit
av=
atar](3D%22https://access.redhat.com/user/edit%22){.3D\"user-info__e=
dit-avatar\"="" analytics-text="3D\"Edit" avatar\"=""}
:::

::: {.3D\"account-metadata account-metadata--mobile\"=""}
### Account info {#account-info .3D\"visually-hidden\" ==""}

::: {.3D\"account-metadata__= login-name\"=""}
Login: rh-ee-ngelman
:::

::: {.3D\"account-metadata__accou= nt-number\"=""}
Account number: 5910538
:::

::: {.3D\"account-metadata__ema= il\"=""}
ngelman@redhat.com
:::
:::

-   \<= a
    href=3D\"https://www.redhat.com/wapps/ugc/protected/personalInfo.html\"
    dat= a-analytics-text=3D\"Account details\"\>

    ::: 3D"account-link__title"
    Account details
    :::

    ::: 3D"account-link__description"
    Edit your contact info, password, location preferences, and= errata
    notifications.
    :::
-   [](3D%22https://access.redhat.com/user%22=){analytics-text="3D\"Community"
    profile\"=""}

    ::: 3D"account-link__title"
    Community profile
    :::

    ::: 3D"account-link__description"
    Fill out your public profile and control what content you f= ollow.
    :::
-   [](3D%22https://www.redhat.com/en/dashb=){oard\"=""
    analytics-text="3D\"My" red="" hat\"=""}

    ::: 3D"account-link__title"
    My Red Hat
    :::

    ::: 3D"account-link__description"
    Get a customized view of resources to help you use our prod= ucts,
    solutions, and services.
    :::
-   [](3D%22https://rol.redhat.com/rol/app/=){\"=""
    analytics-text="3D\"Training" &amp;="" certification\"=""}

    ::: 3D"account-link__title"
    Training & certification
    :::

    ::: 3D"account-link__description"
    Access your Red Hat Learning Subscription, courses, and exa= ms.
    :::
-   [](3D%22https://access.redhat.com/group=){s="" \"=""
    analytics-text="3D\"Private" groups\"=""}

    ::: 3D"account-link__title"
    Private groups
    :::

    ::: 3D"account-link__description"
    Access your invitations and private groups.
    :::
-   [](3D%22https://access.redhat.com/support/cases/%22){a="nalytics-text=3D\"Support\""}

    ::: 3D"account-link__title"
    Support cases
    :::

    ::: 3D"account-link__description"
    Manage your support tickets.
    :::

::: 3D"account-metadata"
Account info

::: {.3D\"account-metadata_= _login-name\"=""}
Login: rh-ee-ngelman
:::

::: {.3D\"account-metadata__acco= unt-number\"=""}
Account number: 5910538
:::

::: {.3D\"account-metadata__em= ail\"=""}
ngelman@redhat.com
:::

::: {.3D\"account-metadata__logout-wrapper= \"=""}
[Log=
out](3D%22https://sso.redhat.com/auth/realms/redhat-external/protocol/op=){enid-connect=""
logout?client_id="3De50f6924-21d9-401d-8c6c-76104e52ab80&po="
st_logout_redirect_uri="3Dhttps%3A%2F%2Fdocs.redhat.com%2Fen%2Fdocumentation="
%2fopenshift_container_platform%2f4.10%2fhtml%2fcicd%2fmigrating-from-jenki="ns-to-tekton&id_token_hint=3DeyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2="
lkiia6icjpvglstvlbnxp5vhitujvgcmlgu2dtufnibduzexbuymdgdnpcsu4wav9nin0.eyjle="HAiOjE3NTUwMTA3NjksImlhdCI6MTc1NTAwOTg2OSwiYXV0aF90aW1lIjoxNzU0OTk5MDMwLCJq="
dgkioiiyztvkmzyzos1iytc2ltrjzjctytmwzs1imtbmy2zhnmvly2uilcjpc3mioijodhrwczo="vL3Nzby5yZWRoYXQuY29tL2F1dGgvcmVhbG1zL3JlZGhhdC1leHRlcm5hbCIsImF1ZCI6ImU1MG="
y2oti0ltixzdktndaxzc04yzzjltc2mta0ztuyywi4mcisinn1yii6iju4mtq4oteyiiwidhlwi="joiSUQiLCJhenAiOiJlNTBmNjkyNC0yMWQ5LTQwMWQtOGM2Yy03NjEwNGU1MmFiODAiLCJzaWQi="
oii4nddlzdq5zc1jmzm2ltqyytqtoda0os1inwu2mzyxntbjmdailcjhdf9oyxnoijoir1p0uep="QSmJwVUNwQm1UdVVUVkxPZyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJvcmdhbml6YXRpb24iOn="
siywnjb3vudf9udw1izxiioii1otewntm4iiwiawqioiixmtawotewmyj9lcjuyw1lijoitmfvb="WkgR2VsbWFuIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicmgtZWUtbmdlbG1hbiIsImdpdmVuX25h="
bwuioijoyw9tasisimxvy2fszsi6imvuiiwizmftawx5x25hbwuioijhzwxtyw4ilcjlbwfpbci="6Im5nZWxtYW5AcmVkaGF0LmNvbSJ9.ZZy4aPExPJchEFdKnDx5VcpDV2Iu0STUFzz7a36xZXN5L="
tyxegnlbq3aokponv2qz61ba-jiqlxpato_v89rg43o8xquyskxlej3lxygqaop9e29_b93-wff="6eMpLf7YmlFNQ6bjhy6yeqjhSGXg19TDXobLXpvFZbwEKX9kMpUHlRzXMP35F438czvzwFZ22vv="
vmgdrnyvuzkzeg8u_nje5ewjbdove16slfzpgsgv45yar93b8tobthuqkkpvyqkq9hlhilu2zsf="lxsLUyZqn2Tx2G0KLZJaNyWGhodKuBrTgKq-546zc3RFdkP90kdGupF2zCXMgIiRZPIrYerPCx5="
v-fpu99bw2vii_thgetxhtrmnkmpwrijwynaqpdcu-wpdes1xom4llyfrwyztcpz_enqrsxd_mu="43GccaXyVMWKFaWXhPr0hB8d1XP5nAe7e8YgvJrdS2oTH26KNBEI7KS_7vcek6XXj5PaDPl3QRS="
akwc2pl1j31kcgqlvws17zrr8py7v0mg88egbyxgwgfjqhwsedasfo1z6ork6cwjdwcyvphh1mm="_3db_DDmDKf1CzVwFh9gOEjVKLStNvrNhaCaK8-qSmFnjizAYKy0DoK5hvFdBIH2oEwRthFdtwC="
exjlfs9qiwthfpwbbpmstd66xleopfc3diyaz4\"="" analytics-text="3D\"Log"
out\"=""}
:::
:::
:::

</div>

::: {slot="3D\"secondary-links\"" v="-b258bd1d=3D\"\""}
::: {.3D\"hidden-at-desktop hidden-at-tablet="" buttons\"="" da="ta-v-b258bd1d=3D\"\""}
[![3D\"Red](3D%22https://docs.redhat.com/_nuxt/Red-Hat-Summit-logo.DsUYtl=){mu.svg\"=""
width="3D\"48\"" height="3D\"25\"" hat="" summit\"=""
v-b258bd1d="=3D\"\""} Red Hat
Summit](3D%22https://www.redhat.com/en/summit%22){analyt="ics-category=3D\"More"
red="" hat\"="" analytics-text="3D\"Summit\""
v-b258bd1="d=3D\"\""}[Support](3D%22https://access.redhat.com/%22){a="nalytics-category=3D\"More"
red="" hat\"="" analytics-text="3D\"Support\""
v-b="258bd1d=3D\"\""}[Console](3D%22https://console.redhat.com/%22){analyt="ics-category=3D\"More"
red="" hat\"="" analytics-text="3D\"Console\""
v-b258bd="1d=3D\"\""}[Developers](3D%22https://developers.redhat.com/%22){analytic="s-category=3D\"More"
red="" hat\"="" analytics-text="3D\"Developers\""
v-b258b="d1d=3D\"\""}[Start a
trial](3D%22https://www.redhat.com/en/products/trials=){\"=""
analytics-category="3D\"More" red="" hat\"="" analytics-text="3D\"Start"
a="" t="rial\""
v-b258bd1d="3D\"\""}[Contact](3D%22https://www.redhat.c=){om="" en=""
contact\"="" analytics-category="3D\"More" red="" hat\"=""
analytics-text="=3D\"Contact\"" v-b258bd1d="3D\"\""}
:::

::: {.3D\"hidden-at-= desktop="" hidden-at-tablet="" mobile-lang-select\"="" v-b258bd1d="3D\"\""}
Select your languageEnglishFran=C3=
=A7ais=ED=95=9C=EA=B5=AD=EC=96=B4=E6=97=A5=E6=9C=AC=E8=AA=
=9E=E4=B8=AD=E6=96=87 (=E4=B8=AD=E5=9B=BD)Deutsch\<=
/option\>ItalianoPortugu=C3=AAsEspa=C3=B1ol=
:::
:::

::: {.3D\"hidden-at-deskto= slot="3D\"search\"" p="" hidden-at-tablet="" search-mobile\"="" v-b258bd1d="3D\"\""}
::: {#3D\"search-fo= .3D\"search-container\" rm-global_search\"="" open-search-box="3D\"true\"" ="v-b258bd1d=3D\"\"" v-7ec4cdc4="3D\"\""}
::: {.3D\"search-box\" data="-v-7ec4cdc4=3D\"\""}
::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::
:::
:::
:::

::: {.3D\"pfe-navigati= d="ata-v-b258bd1d=3D\"\"" slot="3D\"custom-nav-documentation\"" on__custom-nav-container\"=""}
::: {.3D\"grid v-b258bd1d="3D\"\"" grid-col-="lg-3" grid-col-md-3="" spacing-32\"=""}
::: {.3D\"span-md-2= v-b258bd1d="3D\"\"" span-xs-3\"=""}
## Explore popular products {#3D\"menu-item__popular-products\" v-b258bd1d="3D\"\"" cla="ss=3D\"pfe-menu-item-heading\""}

-   [[Red Hat Enterprise Linux]{.3D\"pfe-nav= v-b258bd1d="3D\"\""
    igation__custom-nav-title\"=""}[A flexible, stable= operating system
    to support hybrid cloud
    innovation.]{.3D\"pfe-navigation__custom-nav-body\"
    v="-b258bd1d=3D\"\""}](3D%22ht=){.3D\"p= v-b258bd1d="3D\"\"" tps:=""
    docs.redhat.com="" en="" documentation=""
    red_hat_enterprise_linux\"="" fe-navigation__custom-nav-link\"=""}
-   [[Red Hat OpenShift Container
    Platform]{.3D\"pfe-navigation__custom-na= v-b258bd1d="3D\"\""
    v-title\"=""}[A container platform to = build, modernize, and deploy
    applications at scale.]{.3D\"pfe-navigation__custom-nav-body\"
    v-b258b="d1d=3D\"\""}](3D%22https://docs.redhat.com/=){.3D\"pfe-navigation__cus=
    v-b258bd1d="3D\"\"" en="" documentation=""
    openshift_container_platform\"="" tom-nav-link\"=""}
-   [[Red Hat Ansible Automation Platform]{.3D\"pfe-navigation__cust=
    v-b258bd1d="3D\"\"" om-nav-title\"=""}[A foundation for imp=
    lementing enterprise-wide
    automation.]{.3D\"pfe-navigation__custom-nav-body\"
    v-b="258bd1d=3D\"\""}](3D%22https://docs.redhat.com/en=){.3D\"pfe-navigation=
    v-b258bd1d="3D\"\"" documentation=""
    red_hat_ansible_automation_platform\"="" __custom-nav-link\"=""}
-   [[Red=  Hat OpenShift Service on
    AWS]{.3D\"pfe-navigation__custom-nav-title\" v-b258bd1d="3D\"\""}[A
    fully managed service to build and m= anage your containerized
    applications on AWS.]{.=3D\"pfe-navigation__custom-nav-body\"
    v-b258bd1d="3D\"\""}](3D%22https://docs.redhat.com/en/documentation=){.3D\"pfe-navigation__custom-nav-link=
    v-b258bd1d="3D\"\"" red_hat_openshift_service_on_aws\"="" \"=""}
-   [[= Red Hat Enterprise Linux
    AI]{.3D\"pfe-navigation__custom-nav-title\"
    v-b258bd1d="3D\"\""}[Develop, test, and run Granite large langu= age
    models (LLMs) on a foundation model platform.]{.3D\"=
    v-b258bd1d="3D\"\""
    pfe-navigation__custom-nav-body\"=""}](3D%22https://docs.redhat.com/en/docum=){.3D\"pfe-navigation__custom-nav-l=
    v-b258bd1d="3D\"\"" entation="" red_hat_enterprise_linux_ai\"=""
    ink\"=""}

::: {.3D\"span-md-1 v-b258bd1d="3D\"\"" span-xs-3\"=""}
## Featured= use cases {#3D\"menu-item__use-cases\" .3D\"pfe-menu-item-heading\" v-b258bd1="d=3D\"\""}

-   [Building your RHEL AI
    environment](3D%22https://docs.redhat.com/en/documentation/red_hat_en=){.=3D\"pfe-list-link\"
    ="v-b258bd1d=3D\"\"" terprise_linux_ai="" 1.1="" html=""
    building_your_rhel_ai_environment="" index\"=""}
-   [Getting started = with Ansible Automation
    Platform](3D%22https://docs.redhat.com/en/docum=){.3D\"pfe-list-link\"
    v-b258bd1d="3D\"\"" entation=""
    red_hat_ansible_automation_platform="" 2.5="" html=""
    getting_started_with_="ansible_automation_platform/index\""}
-   [Manage your VMs with OpenShift Vir=
    tualization](3D%22https://docs.redhat.com/en/documentation/openshift_c=){.3D\"pfe-list-link\"
    v="-b258bd1d=3D\"\"" ontainer_platform="" 4.17="" html=""
    virtualization=""
    about#virt-what-you-can-do-with-="virt_about-virt\""}
-   [Identify an= d resolve issues by using Red Hat
    Insights](=3D%22https://docs.redhat.com/en/documentation/red_hat_insights/1-latest/html=){.3D\"pfe-list-link\"
    v-b258bd1d="3D\"\"" getting_started_with_red_hat_insights\"=""}
-   [Building a hybrid cloud with Red&= nbsp;Hat OpenStack Services on
    OpenShift](3D%22https://docs.redhat.com/en/documentat=){.3D\"pfe-list-link\"
    v-b258bd1d="3D\"\"" ion=""
    red_hat_openstack_services_on_openshift="" 18.0="" html-single=""
    planning_your_="deployment/index\""}
:::
:::

::: {.3D\"pfe-navigation--footer\" data="-v-b258bd1d=3D\"\""}
[Explore all
products](3D%22https://docs.redhat.com/en/=){v-b258bd1d="3D\"\""
products\"=""}
:::
:::

::: {.3D\"pfe-navigation__custom-nav-contain= v-b258bd1d="=3D\"\"" slot="3D\"custom-nav-learn\"" er\"=""}
::: {.3D\"grid v-b258bd1d="3D\"\"" grid-col-lg-4="" grid-col-md-4="" spa="cing-32\""}
::: {.3D\"span-md-2 v-b258bd1d="3D\"\"" span-xs-2\"=""}
## Curated guides {#3D\"menu-item__curated-guides\" .3D\"pfe-menu-item-head= v="-b258bd1d=3D\"\"" ing\"=""}

-   [[Get started with Red Hat]{.3D\"pf= v-b258bd1d="3D\"\""
    e-navigation__custom-nav-title\"=""}[Discover the = value of your
    Red Hat products with these learning
    paths.]{.3D\"pfe-navigation__custom-nav-body\"
    d="ata-v-b258bd1d=3D\"\""}](3D%22http://access.redhat.com/start%22){.=3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\""}
-   [[Red Hat Dev= eloper]{.3D\"pfe-navigation__custom-nav-title\"
    ="v-b258bd1d=3D\"\""}[Learn how to build flexible and reliable
    applications with Red = Hat
    solutions.]{.3D\"pfe-navigation__custom-nav= v-b258bd1d="3D\"\""
    -body\"=""}](3D%22https://develop=){.3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\"" ers.redhat.com="" learn\"=""}
-   [[Red Hat OpenShift essentials]{.3D\"pfe-navig= v-b258bd1d="3D\"\""
    ation__custom-nav-title\"=""}[Tackle common Op= enShift tasks with
    these curated resources.]{.3D\"pfe-navigation__custom-nav-body\"
    data="-v-b258bd1d=3D\"\""}](3D%22https://docs.redhat.com/en/essentials/openshift%22){.3D\"pfe=
    v-b258bd1d="=3D\"\"" -navigation__custom-nav-link\"=""}
-   [[Red Hat Hybrid Cloud Cons=
    ole]{.3D\"pfe-navigation__custom-nav-title\" v-b258bd1d="3D\"="
    \"=""}[Build, deploy, and optimize workloads across the hybrid cloud
    with Red&= nbsp;Hat.]{.3D\"pfe-navigation__custom-nav-bo=
    v-b258bd1d="3D\"\""
    dy\"=""}](3D%22https://cloud.redhat.com/getting-s=){.3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\"" tarted\"=""}
-   [[Managed OpenShift tutorials]{.3D\"pfe-navigation__custom-nav-tit=
    v-b258bd1d="3D\"\"" le\"=""}[Red Hat experts share step-by-step tut=
    orials to help maximize your cluster.]{.3D\"p= v-b258bd1d="3D\"\""
    fe-navigation__custom-nav-body\"=""}]{.3D\"pfe-navigation__custom-n=
    v-b258bd1d="3D\"\"" h="ref=3D\"https://cloud.redhat.com/experts/\""
    av-link\"=""}
:::

::: {.3D\"span-md-1 v="-b258bd1d=3D\"\"" span-xs-1\"=""}
## Hands-on {#3D= .3D\"pfe-menu-item-heading\" v-b258bd1d="3D\"\"" \"menu-item__hands-on\"=""}

-   [Red&nbs= p;Hat Hybrid Cloud learning paths[Build on your
    Red Hat=C2=AE Cloud Se= rvices expertise with these learning
    resources.]{.3D= v-b258bd1d="3D\"\""
    \"pfe-navigation__custom-nav-body\"=""}](3D%22h=){.3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\"" ttps:="" cloud.redhat.com="" learn\"=""}
-   [Interactive labs]{.3D\"pfe-navigation__custom-nav-title\"
    v-b258bd1d="3D=" \"\"=""}
    Hands-on, in= teractive lessons based on real use cases with Red Hat
    products.
-   [[Customer Port= al labs]{.3D\"pfe-navigation__custom-nav-title\"
    da="ta-v-b258bd1d=3D\"\""}[Troubleshoot issues, identify security
    problems, and more with thes= e
    labs.]{.3D\"pfe-navigation__custom-na= v-b258bd1d="3D\"\""
    v-body\"=""}](3D%22https://=){.3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\"" access.redhat.com="" labs="" \"=""}
:::

::: {.3D\"span-m= v-b258bd1d="3D\"\"" d-1="" span-xs-1\"=""}
## Tools {#3D\"menu-item__tools\" .3D\"pf= v-b258bd1d="3D\"\"" e-menu-item-heading\"=""}

-   [[Architecture Center]{.=3D\"pfe-navigation__custom-nav-title\"
    v-b258bd1d="3D\"\""}[Showcase of examp= les and partner uses for
    building with Red Hat
    solutions.]{.3D\"pfe-navigation__custom-nav-body\"
    ="v-b258bd1d=3D\"\""}](3D%22http://redhat.com/architect/portfolio/%22){.3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\"" ==""}
-   [[Training and certification]{.3D\"pfe-navigation__custom-n=
    v-b258bd1d="3D\"\"" av-title\"=""}[Gain the knowledge to get
    certified an= d stay ahead of technology
    trends.]{.=3D\"pfe-navigation__custom-nav-body\"
    v-b258bd1d="3D\"\""}](3D%22https://www.red=){.3D\"pfe-navigation__cu=
    v-b258bd1d="3D\"\"" hat.com="" en="" services=""
    training-and-certification\"="" stom-nav-link\"=""}
:::
:::
:::

::: {.3D\"grid v-b258bd1d="3D\"\"" grid-col-lg-3="" gr="id-col-md-3" spacing-32\"=""}
::: {.3D\"span-md-1 v-b258bd1d="3D\"\"" span-x="s-1\""}
## Learn AI {#3D\"menu-item__learn-ai\" .3D\"pfe-menu-= v-b258bd1d="3D\"\"" item-heading\"=""}

-   [[AI learning hub]{.3D\"p= v-b258bd1d="3D\"\""
    fe-navigation__custom-nav-title\"=""}[Explore learning materials=
    and tools, organized by the tasks you need to
    do.]{.3D\"pfe-navigation__custom-nav-body\"
    v-b258bd1="d=3D\"\""}](3D%22https://docs.redhat.com/en/learn/ai%22){v-b258bd1d="3D\"\""
    clas="s=3D\"pfe-navigation__custom-nav-link\""}
-   [[Red Hat AI Founda= tions]{.3D\"pfe-navigation__custom-nav-title\"
    v-b258="bd1d=3D\"\""}[No-cost foundational training covering AI
    essentials to using Red&nbs= p;Hat AI
    effectively.]{.3D\"pfe-navigation__custom-nav-= v-b258bd1d="3D\"\""
    body\"=""}](3D%22https://docs.redhat.com/en/=){.3D\"pfe-navigation__custom-nav-link\"
    v-b258bd1d="3D\"\"" ai-foundations\"=""}
-   AI interactive experiences[Expl= ore hands-on experiences with
    Red Hat AI including training LLMs and m=
    ore.]{.3D\"pfe-navigation__custom-nav-body\" v-b258bd1d="3D\"\""}
:::

::: {.3D\"span-md-1= v-b258bd1d="3D\"\"" span-xs-1\"=""}
## AI documentation {#3D\"menu-item__ai-documentation\" v-b258bd1d="3D\"\"" cla="ss=3D\"pfe-menu-item-heading\""}

-   [[Red Hat Enterprise Linux AI]{.3D\"pfe-navigati=
    v-b258bd1d="3D\"\"" on__custom-nav-title\"=""}[Develop, test, and r=
    un Granite large language models on a foundational
    platform.]{.3D\"pfe-navigation__custom-nav-body\"
    v-b="258bd1d=3D\"\""}](3D%22https://do=){.3D\"pfe-na=
    v-b258bd1d="3D\"\"" cs.redhat.com="" en="" documentation=""
    red_hat_enterprise_linux_ai\"="" vigation__custom-nav-link\"=""}
-   [[Red Hat OpenShift AI]{.3D\"pfe-navigation__custo=
    v-b258bd1d="3D\"\"" m-nav-title\"=""}[Run a flexible AI platform
    that can = deliver applications across
    environments.]{v-b258bd1d="3D\"\""
    cla="ss=3D\"pfe-navigation__custom-nav-body\""}](3D%22https://docs.redh=){.3D\"pfe-navigation_=
    v-b258bd1d="3D\"\"" at.com="" en="" documentation=""
    red_hat_openshift_ai="" 2025\"="" _custom-nav-link\"=""}
:::

::: {.3D\"span-md-1 da="ta-v-b258bd1d=3D\"\"" span-xs-1\"=""}
## More to ex= plore {#more-to-ex-plore .3D\"pfe-menu-item-heading\" v-b258bd1d="3D\"\"" i="d=3D\"menu-item__more-to-explore\""}

-   [[AI Consulting Se= rvices]{.3D\"pfe-navigation__custom-nav-title\"
    ="v-b258bd1d=3D\"\""}[Not sure where to start? Work with Red Hat
    experts to build you= r roadmap to
    AI.]{.3D\"pfe-navigation__custom-nav= v-b258bd1d="3D\"\""
    -body\"=""}](3D%22https://www.redhat.com/en/services/consulting/red-h=){.3D\"pfe-navigation__custom-nav-link\"
    ="v-b258bd1d=3D\"\"" at-consulting-for-ai\"=""}
:::
:::
:::

::: {#3D\"main-content\" role="main"}
::: {#3D\"breadcrumbs\" .3D\"breadcrumbs\" v-c6b48c1e="3D=" \"\"="" v-fa60319a="3D\"\""}
\<= div class=3D\"main-breadcrumbs-container\" data-v-fa60319a=3D\"\"\>

1.  [Home](3D=){\"https:="" docs.redhat.com="" \"=""
    v-fa60319a="3D\"\""}
2.  [Products](3D%22https://docs.redhat.com/en/products%22){v-fa60319a="=3D\"\""}
3.  [OpenShift Container Platform](3D%22https://=){docs.redhat.com=""
    en="" documentation="" openshift_container_platform="" \"=""
    v-fa60="319a=3D\"\""}
4.  [4.10](3D%22https://docs.redhat.com/en/documentation/openshift_container_platfo=){==""
    rm="" 4.10="" \"="" v-fa60319a="3D\"\""}
5.  [CI/CD]{hre="f=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform/="
    4.10="" html="" cicd="" \"="" v-fa60319a="3D\"\""}
6.  Chapter 3. Migrating from Jenkins to Tekton

::: {.3D\"theme-container\" v-="fa60319a=3D\"\"" v-9af16c28="3D\"\""}
[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTIzLjk0IiAxNmExIDEgMD0iMCIgMS0uOTkyLS44NzYgNi45NTcgNi45NTcgMCAwIDAtNi4wNjktNi4wNjIgMSAxIDAgMSAxIC4yNDItMS45ODUgOC45NTMgOC45NT0iMyIgMCAwIDEgNy44MTIgNy44YS45OTkuOTk5IDAgMCAxIDIzLjk0IDE2em0xNiA1YTEgMSAwIDAgMS0xLTF2MWExIDEgMCAxIDEgMj0iMHYzYTEiIDEgMCAwIDEtMSAxem0wIDI3YTEgMSAwIDAgMS0xLTF2LTNhMSAxIDAgMSAxIDIgMHYzYTEgMSAwIDAgMS0xIDF6bTQ9IjE3SDFhMSIgMSAwIDEgMSAwLTJoM2ExIDEgMCAxIDEgMCAyem0yNyAwaC0zYTEgMSAwIDEgMSAwLTJoM2ExIDEgMCAxIDEgMCAyem09IjUuMzk0IiAyNy42MDZhMSAxIDAgMCAxLS43MDctMS43MDdsMi4xMi0yLjEyYTEgMSAwIDEgMSAxLjQxNSAxLjQxM2w2LjEgMjcuMzE9IjNhLjk5Ny45OTciIDAgMCAxLS43MDcuMjkzem0yNC40ODUgOC41MTVhMSAxIDAgMCAxLS43MDctMS43MDdsMjUuOSA0LjY4NmExIDE9IjAiIDEgMSAxLjQxNSAxLjQxNWwtMi4xMjIgMi4xMmEuOTk3Ljk5NyAwIDAgMS0uNzA3LjI5NHptLTE2Ljk3IDBhLjk5Ny45OTcgMD0iMCIgMS0uNzA3LS4yOTNsNC42ODYgNi4xYTEgMSAwIDEgMSAxLjQxNS0xLjQxNWwyLjEyIDIuMTIyYTEgMSAwIDAgMS0uNzA2IDEuPSI3MDdabTE5LjA5MSIgMTkuMDkxYS45OTcuOTk3IDAgMCAxLS43MDctLjI5M2wtMi4xMi0yLjEyYTEgMSAwIDEgMSAxLjQxMy0xLjQxPSI1bDIuMTIyIiAyLjEyMWExIDEgMCAwIDEtLjcwNyAxLjcwN3ptMTYgMjQuODc1Yy00Ljg5NCAwLTguODc1LTMuOTgxLTguODc1LTguPSI4NzVhOC44NzkiIDguODc5IDAgMCAxIDUuMjI3LTguMDg4Ljg3Ni44NzYgMCAwIDEgMS4xNTMgMS4xNjMgNi45NDUgNi45NDUgMCAwPSIwLS42MyIgMi45MjVhNy4xMzMgNy4xMzMgMCAwIDAgMjAgMTkuMTI1YTYuOTQ4IDYuOTQ4IDAgMCAwIDIuOTI1LS42My44NzYuODc9IjYiIDAgMCAxIDEuMTYzIDEuMTU0YTguODggOC44OCAwIDAgMSAxNiAyNC44NzV6bS00Ljc4NS0xNC4xNTNhNy4xMzUgNy4xMzUgMD0iMCIgMCA4Ljg3NSAxNiA3LjEzMyA3LjEzMyAwIDAgMCAxNiAyMy4xMjVhNy4xMyA3LjEzIDAgMCAwIDUuMjc4LTIuMzRjLS40MTkuMD0iNi0uODQ1LjA5LTEuMjc4LjA5LTQuODk0IiAwLTguODc1LTMuOTgxLTguODc1LTguODc1IDAtLjQzMy4wMy0uODYuMDktMS4yNzh6Ij48L3BhdGg+PC9zdmc+)
:::

[]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" microns="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iPTNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMCAyMCI+PHBhdGggZD0iM0QmcXVvdDtNMTguNzEiIDUuMj0iOWEuOTk2Ljk5NiIgMCAwIDAtMS40MSAwbC03LjI5IDcuMjktNy4zLTcuMjlhLjk4Ny45ODcgMCAwIDAtMS40MS0uMDIuOTg3Ljk4Nz0iMCIgMCAwLS4wMiAxLjQxbC4wMi4wMiA3LjY1IDcuNjVjLjI5LjI5LjY4LjQ0IDEuMDYuNDRzLjc3LS4xNSAxLjA2LS40NGw3LjY1PSItNy42NWEuOTk2Ljk5NiIgMCAwIDAgMC0xLjQxeiI+PC9wYXRoPjwvc3ZnPg==)
:::
:::
:::

=

::: {.3D\"mobile-nav-wrapper\" dat="a-v-c6b48c1e=3D\"\""}
::: {#3D\"first-button\" v-c6b48c1e="3D\"\""}
[Open ]{.3D\"sr-only= \"="" v-c6b48c1e="3D\"\""}Table of contents
:::

::: {#=3D\"second-button\" v-c6b48c1e="3D\"\""}
::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTMxLjI3IiAxMy4zM2ExIDE9IjAiIDAgMC0uOTk0LS44M2wtMy4zMjktLjAwMWExMC43NzQgMTAuNzc0IDAgMCAwLS43MzUtMS43NjJsMi4zNTQtMi4zNTNjLjM0Nz0iLS4zNDkuMzk1LS44OS4xMTUtMS4yOWExNS41MjMiIDE1LjUyMyAwIDAgMC0zLjc3Ni0zLjc3NCAxLjAwNCAxLjAwNCAwIDAgMC0xLj0iMjkuMTE1bC0yLjM0NyIgMi4zNDdhMTAuNzIgMTAuNzIgMCAwIDAtMS43NjgtLjcydjEuNzI0YzAtLjQ5My0uMzQ5LS45MS0uODMtLj0iOTk0YTE1LjYzMiIgMTUuNjMyIDAgMCAwLTUuMzQyIDBjLS40OC4wODQtLjgyOC41MDEtLjgyOC45OTRsLS4wMDEgMy4zMjljLS42MT0iNC4xOTYtMS4yMS40NDItMS43NjIuNzM1TDguMzg0IiAzLjQzNGExLjAwNiAxLjAwNiAwIDAgMC0xLjI5LS4xMTVhMTUuNTIzIDE1Lj0iNTIzIiAwIDAgMCAzLjMyIDcuMDk1Yy0uMjgxLjM5OC0uMjMzLjk0LjExNSAxLjI5bDIuMzQ3IDIuMzQ2YTEwLjcyIDEwLjcyIDAgMD0iMC0uNzIiIDEuNzY5aDEuNzI0YTEgMSAwIDAgMC0uOTkzLjgyOCAxNS41OTggMTUuNTk4IDAgMCAwIDAgNS4zNDIgMSAxIDAgMCAwPSIuOTkzLjgzbDMuMzI5LjAwMWMuMTk2LjYxNC40NDIiIDEuMjA5LjczNSAxLjc2MmwtMi4zNTQgMi4zNTNjLS4zNDcuMzQ5LS4zOTU9Ii44OS0uMTE1IiAxLjI5YTE1LjUyMyAxNS41MjMgMCAwIDAgMy43NzYgMy43NzRjLjM5Ny4yODIuOTQxLjIzMyAxLjI5LS4xMTVsMi49IjM0Ny0yLjM0N2ExMC43MiIgMTAuNzIgMCAwIDAgMS43NjguNzJ2My4zMzhjMCAuNDkzLjM0OS45MS44My45OTRhMTUuNjIgMTUuNjI9IjAiIDAgMCA1LjM0MiAwYy40OC0uMDg0LjgyOC0uNTAxLjgyOC0uOTk0bC4wMDEtMy4zMjlhMTAuNzc0IDEwLjc3NCAwIDAgMCAxLj0iNzYyLS43MzVsMi4zNTMiIDIuMzU0Yy4zNDkuMzQ2Ljg5LjM5NCAxLjI5LjExNWExNS41MjMgMTUuNTIzIDAgMCAwIDMuNzc0LTMuNz0iNzZjLjI4MS0uMzk4LjIzMy0uOTQtLjExNC0xLjI5bC0yLjM0OC0yLjM0NmExMC43MiIgMTAuNzIgMCAwIDAgLjcyLTEuNzdoMy4zMz0iOGExIiAxIDAgMCAwIC45OTMtLjgyNyAxNS41OTggMTUuNTk4IDAgMCAwIDAtNS4zNDJ6bTE2IDIwYy0yLjIwNiAwLTQtMS43OTQtND0iLTRzMS43OTQtNCIgNC00IDQgMS43OTQgNCA0LTEuNzk0IDQtNCA0eiI+PC9wYXRoPjwvc3ZnPg==)
:::

[Open = page settings]{.3D\"sr-only\" v-c6b48c1e="3D\"\""}
:::
:::

::: {#3D\"mobile-nav-content-wrap= .3D\"hidden\" per\"="" role="3D\"navigation\"" tabindex="3D\"0\"" v-c6b48c1e="3D=" \"\"=""}
::: {#3D\"toc-mobile\" .3D\"hidden\" aria-labelledby="3D\"toc-btn\"" data="-v-c6b48c1e=3D\"\""}
::: {#3D\"product-container-mobile\" .3D\"product-cont= ainer\"="" v-c6b48c1e="3D\"\""}
# OpenShift Container Platform {#openshift-container-platform .3D\"product-title\" v-c6b48c1e="3D\"=" \"=""}

::: {.3D\"product-version\" v-c6="b48c1e=3D\"\""}
Version4.194.184.174= .164.154.144.134.124.114.104.94.84.7\<=
/option\>4.64.54.44.34.24.13.113.103.93.73.63.53.43.33.23.13.02

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
=20
:::

This documentation may not be available for all versions.

[View the product page for all
versions](3D%22https://docs.redhat.com/en/=){.3D\"popover-body-link\"
documentation="" openshift_container_platform\"=""
dat="a-v-c6b48c1e=3D\"\""}
:::

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::
:::
:::

::: {.3D\"to= c-filter-mobile\"="" v-c6b48c1e="3D\"\""}
[]{#3D\"text\" part="3D\"text\"" ="v-c6b48c1e=3D\"\""}
:::

::: {#3D\"toc-wra= .3D\"span-xs-12 pper-mobile\"="" span-sm-4="" span-md-3\"="" lang="3D\"en\"" v-c6="b48c1e=3D\"\""}
:::

\<= !\-\-\--\>
:::

::: {#3D\"page-content-options-mobile\" .3D\"hidden\" aria-l="abelledby=3D\"settings-btn\"" v-c6b48c1e="3D\"\""}
::: {.3D\"page-layout-o= ptions\"="" v-c6b48c1e="3D\"\""}
FormatMulti-pageSingle-pageView fu= ll doc as PDF
:::
:::

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTE2IiAyNC43OTJjLS4zODQ9IjAtLjc2OC0uMTQ2LTEuMDYtLjQzOUwxLjI5MyIgMTAuNzA3YTEgMSAwIDEgMSAxLjQxNC0xLjQxNGwxNiAyMi41ODYgMjkuMjkzPSI5LjI5M2ExIiAxIDAgMSAxIDEuNDE0IDEuNDE0bDE3LjA2MSAyNC4zNTRhMS40OTQgMS40OTQgMCAwIDEtMS4wNi40Mzh6Ij48L3BhPT48L3N2Zz4=)
:::

Jump to section

::: {#3D\"details-content\"}
:::

::: {.3D\"grid conte="nt-wrapper\"" v-c6b48c1e="3D\"\""}
::: {#3D\"toc-container\" .3D\"toc-container\" visible="3D\"true\"" ="v-c6b48c1e=3D\"\""}
::: {#3D\"toc-focus-container\" .3D\"toc-focus-containe= r\"="" v-c6b48c1e="3D\"\""}
::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTIyIiAzMWEuOTk3Ljk5Nz0iMCIgMCAxLS43MDctLjI5M2w3LjY0NyAxNy4wNjFhMS41MDEgMS41MDEgMCAwIDEgMC0yLjEyMmwyMS4yOTMgMS4yOTNhMSAxIDAgMT0iMSIgMS40MTQgMS40MTRsOS40MTQgMTZsMTMuMjkzIDEzLjI5M2ExIDEgMCAwIDEgMjIgMzF6Ij48L3BhdGg+PC9zdmc+)
:::
:::

::: {#3D\"product-container-deskto= .3D\"product-container\" p\"="" v-c6b48c1e="3D\"\""}
# OpenShift Container Platform {#openshift-container-platform-1 .3D\"product-ti= tle\"="" v-c6b48c1e="3D\"\""}

::: {.3D\"pr= oduct-version\"="" v-c6b48c1e="3D\"\""}
Version4.194.184.174.164.154.144.134.124.11\<=
/option\>4.104.94.84.74.6\<= option value=3D\"4.5\"
data-v-c6b48c1e=3D\"\"\>4.54.44.34.24.13.11= 3.103.93.73.63.5\<=
/option\>3.43.33.23.13.02

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
=20
:::

This documentation may not be available for all versions.

[View the product page for all
versions](3D%22https://docs.redhat.com/en/=){.3D\"popover-body-link\"
documentation="" openshift_container_platform\"=""
dat="a-v-c6b48c1e=3D\"\""}
:::

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTE2IiAxNWExIDEgMCAwIDA9Ii0xIiAxdjdhMSAxIDAgMSAwIDIgMHYtN2ExIDEgMCAwIDAtMS0xeiI+PC9wYXRoPjxwYXRoIGQ9IjNEJnF1b3Q7TTE2IiAwYzcuMTc4IDAgMCA3PSIuMTc4IiAwIDE2czcuMTc4IDE2IDE2IDE2IDE2LTcuMTc4IDE2LTE2czI0LjgyMiAwIDE2IDB6bTAgMzBjOC4yOCAzMCAyIDIzLjcyPSIyIiAxNnM4LjI4IDIgMTYgMnMxNCA2LjI4IDE0IDE0LTYuMjggMTQtMTQgMTR6Ij48L3BhdGg+PGNpcmNsZSBjeD0iM0QmcXVvdDsxNiZxdW90OyIgY3k9Ij0zRCZxdW90OzEwJnF1b3Q7IiByPSIzRCZxdW90OzEuNSZxdW90OyI+PC9jaXJjbGU+PC9zdmc+)
:::
:::
:::

::: {#3D\"toc-f= .3D\"toc-filter\" ilter\"="" v-c6b48c1e="3D\"\""}
[[ ]{#3D\"search-icon\" part="3D\"search-icon\""
da="ta-v-c6b48c1e=3D\"\""}]{#3D\"text\" part="3D\"=" text\"=""
v-c6b48c1e="3D\"\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjUiIDEuMjVoLTI3Yy09Ii42OSIgMC0xLjI1LjU2LTEuMjUgMS4yNXY3YzAgLjIuMDguMzkuMjIuNTNsMTAuNzggMTAuNzh2MTIuMDczYzAgLjM3OC4xNjkuNzM9IjIuNDYzLjk3YTEuMjQ2IiAxLjI0NiAwIDAgMCAxLjA0Ny4yNTNsNC45OTktMS4wNjRjLjU3NC0uMTIxLjk5LS42MzUuOTktMS4yMjM9IlYxOC4zMTFMMzAuNTMiIDcuNTNhLjc1Ljc1IDAgMCAwIC4yMi0uNTN2Mi41YzAtLjY5LS41Ni0xLjI1LTEuMjUtMS4yNXoiPjwvcGE9Pjwvc3ZnPg==)
:::
:::

About

1.  A= bout
    1.  [About](3D%22https://docs.redhat.com/en/doc=){#3D\"chapte=
        .3D\"link sub="-chapter-title" chapter-landing-page\"=""
        umentation="" openshift_container_platform="" 4.10="" html=""
        about="" index\"="" r-landing--about-index\"=""
        v-c61ac788="3D\"\""}
    2.  [OpenShift Container Platform 4.10 Documenta=
        tion](3D%22https://docs.redhat.com/en/documentation/openshift_con=){#3D\"sub-link-to-about-welc=
        .3D\"link sub-ch="apter-title\"" tainer_platform="" 4.10=""
        html="" about="" welcome-index\"="" ome-index\"=""
        v-c61ac788="3D\"\""}
    3.  [Learn more about OpenShift Container
        Platform](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-about-learn_more_about_openshift\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" about=""
        learn_more_abo="ut_openshift\"" v-c6="1ac788=3D\"\""}

2.  \<= summary class=3D\"heading sub-chapter-title\"
    id=3D\"null\--summary\" data-v-c61= ac788=3D\"\"\>Getting started
    1.  [Getting
        started](3D%22https://=){#3D\"chapter-landing--getting_started-index\"
        .3D\"link sub-chapter-title="" chapter-landing-page\"=""
        docs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        get="ting_started/index\"" v-c6="1ac788=3D\"\""}
    2.  [Kubernetes
        overview](3D%22ht=){#3D\"sub-link-to-getting_started-k=
        .3D\"link sub-chapter-title\"="" tps:="" docs.redhat.com=""
        en="" documentation="" openshift_container_platform="" 4.10=""
        ht="ml/getting_started/kubernetes-overview\""
        ubernetes-overview\"="" v-c61ac788="3D\"\""}
    3.  [Op= enShift Container Platform
        overview](3D%22https://docs.redhat.com/en/documentation/ope=){#=3D\"sub-link-to-getting_started-openshift-overview\"
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" getting_started=""
        openshift-overview\"="" v-c61ac788="3D\"\""}
    4.  [Creating and building = an application using the web
        console]{#3D\"sub-link-to-getting= .3D\"link
        sub-chapter-title\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" getting_started="" openshift-web-console\"=""
        _started-openshift-web-console\"="" v-c61ac788="3D\"\""}
    5.  [Creating and building an application = using the
        CLI]{#3D\"sub-link-to-getting_starte= .3D\"link
        sub-chapter-title\"=""
        h="ref=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfor="
        m="" 4.10="" html="" getting_started="" openshift-cli\"=""
        d-openshift-cli\"="" v-c61ac788="3D\"\""}

3.  1.  [Release
        notes](3D%22https://docs.redhat.com/en/documentation/openshift_con=){#3D\"chapter-landing--relea=
        .3D\"link sub-chapter-title="" chapter-l="anding-page\""
        tainer_platform="" 4.10="" html="" release_notes="" index\"=""
        se_notes-index\"="" v-c61ac788="3D\"\""}
    2.  [OpenShift= Container Platform 4.10 release
        notes](3D%22https://docs.redhat.com/en/documentation/openshift_con=){#3D\"sub-l=
        .3D\"link sub-ch="apter-title\"" tainer_platform="" 4.10=""
        html="" release_notes="" ocp-4-10-release-notes\"=""
        ink-to-release_notes-ocp-4-10-release-notes\"=""
        v-c61ac788="3D\"\""}

4.  Architec= ture
    1.  [Architecture](3D%22https://docs.redhat.com/en/doc=){#3D=
        .3D\"link sub="-chapter-title" chapter-landing-page\"=""
        umentation="" openshift_container_platform="" 4.10="" html=""
        architecture="" index\"=""
        \"chapter-landing--architecture-index\"="" v-c61ac788="3D\"\""}=
    2.  Architecture overview
    3.  [OpenShift Container Platform
        architecture](3D%22=){#3D\"sub-link-to-architecture-architecture=
        .3D\"link sub-chapter-title\"="" https:="" docs.redhat.com=""
        en="" documentation="" openshift_container_platform="" 4.10=""
        =="" html="" architecture="" architecture\"="" \"=""
        v-c61ac788="3D\"\""}
    4.  [Installation and
        update](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-architecture-architecture-installation\"
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html="" architecture=""
        architecture-installa="tion\"" v-c61a="c788=3D\"\""}
    5.  [Red Hat OpenShift Cluster
        Manager](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-architecture-ocm-=
        .3D\"link sub-chapter-title\"="" .10="" html="" architecture=""
        ocm-overview-ocp\"="" overview-ocp\"="" v-c61ac788="3D\"\""}
    6.  [Control pl= ane
        architecture](3D%22https://docs.redhat.com/en/documenta=){#=3D\"sub-link-to-architecture-control-plane\"
        cl="ass=3D\"link" sub-chapter-title\"="" tion=""
        openshift_container_platform="" 4.10="" html="" architecture=""
        control-plane\"="" v-c61ac788="3D\"\""}
    7.  [Understanding OpenShift Container Platf= orm
        development](3D%22https://docs.=){#3D\"sub-link-to-architecture-understandin=
        .3D\"link sub-chapter-title\"="" redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        architec="ture/understanding-development\"" g-development\"=""
        v-c61ac788="3D\"\""}
    8.  [Red Hat Enterprise Linux CoreOS
        (RHCOS)](3D%22https://docs.r=){#3D\"sub-link-to-architecture-architecture-rhcos\"
        .3D\"link sub-chapter-title\"="" edhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        architect="ure/architecture-rhcos\"" =="" v-c61ac788="3D\"\""}
    9.  [Admission=
        plugins](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"=
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" architecture=""
        admission-plug-ins\"=""
        sub-link-to-architecture-admission-plug-ins\"=""
        v-c61ac788="3D\"\""}

5.  Security and compliance
    1.  [Security and =
        compliance](3D%22https://docs.redhat.com/en/documentation/openshif=){#3D\"chapter=
        .3D\"link sub-chapter-title="" chap="ter-landing-page\""
        t_container_platform="" 4.10="" html=""
        security_and_compliance="" index\"=""
        -landing--security_and_compliance-index\"=""
        v-c61ac788="3D\"\""}
    2.  [OpenShift Contain= er Platform security and
        compliance](3D%22https://docs.redhat=){#3D\"sub-link-to-security_and_comp=
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        security_and_c="ompliance/security-compliance-overview\""
        liance-security-compliance-overview\"="" v-c61ac788="3D\"\""}
    3.  [Containe= r security]{#3D\"sub-link-to-= .3D\"link
        sub-chapter-title\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" security_and_compliance=""
        container-security-1\"=""
        security_and_compliance-container-security-1\"=""
        v-c61ac788="3D\"\""}
    4.  Configuring certificates\<= /a\>
    5.  [Certificate type= s and
        descriptions](3D%22https://docs.redhat.com/en/doc=){#3D\"sub-link-to-security_and_complianc=
        .3D\"link sub-chapter-title\"="" umentation=""
        openshift_container_platform="" 4.10="" html=""
        security_and_compliance=""
        c="ertificate-types-and-descriptions\""
        e-certificate-types-and-descriptions\"="" v-c61ac788="3D\"\""}
    6.  [Compliance
        Operator](3D%22https://doc=){#3D\"sub-link-to-security_and_compl=
        .3D\"link sub-chapter-title\"="" s.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        securi="ty_and_compliance/compliance-operator\""
        iance-compliance-operator\"="" v-c61ac788="3D\"\""}
    7.  [File Integrity
        Operator](3D%22https://docs.redhat.com/en/documentat=){#3D\"sub-link-to-security_and_compliance-file-integrity-o=
        cla="ss=3D\"link" sub-chapter-title\"="" ion=""
        openshift_container_platform="" 4.10="" html=""
        security_and_compliance="" file-int="egrity-operator\""
        perator\"="" v-c61ac788="3D\"\""}
    8.  [cert-manager Operat= or for Red Hat
        OpenShift](3D%22https://docs.redhat.com/en/documentation/openshift_=){#3D\"sub-link-to-security_and_compliance-cert-manag=
        .3D\"link sub="-chapter-title\"" container_platform="" 4.10=""
        html="" security_and_compliance=""
        cert-manager-operator-="for-red-hat-openshift\""
        er-operator-for-red-hat-openshift\"="" v-c61ac788="3D\"\""}
    9.  [Viewing audit
        logs](3D%22https=){#3D\"sub-link-to-security_and_comp= .3D\"link
        sub-chapter-title\"="" :="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        =="" security_and_compliance="" audit-log-view\"=""
        liance-audit-log-view\"="" v-c61ac788="3D\"\""}
    10. [Configuring the audit log
        policy](3D%22https://docs.redhat.com/en/documentation/o=){#3D\"sub-link-to-security_and_compliance-audit-log-policy-conf=
        .3D= \"link="" sub-chapter-title\"=""
        penshift_container_platform="" 4.10="" html=""
        security_and_compliance="" audit-log-pol="icy-config\"" ig\"=""
        v-c61ac788="3D\"\""}
    11. [Configuring TLS security
        profiles](3D%22https://docs.redhat.com/en/documentation/opensh=){#3D\"sub-link-to-security_and_compliance-tls-security-profiles\"
        .3D\"link= sub-chapter-title\"="" ift_container_platform=""
        4.10="" html="" security_and_compliance=""
        tls-security-profi="les\"" ="v-c61ac788=3D\"\""}
    12. [Allowing JavaScript-based access to the API = server from
        additional
        hosts](3D%22htt=){#=3D\"sub-link-to-security_and_compliance-allowing-javascript-based-access-ap=
        .3D\"link sub-chapter-title\"="" ps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        htm="l/security_and_compliance/allowing-javascript-based-access-api-server\""
        i-server\"="" v-c61ac788="3D\"\""}
    13. [Encrypting etcd data](3D%22h=){#3D\"sub-link-to-security_and=
        .3D\"link sub-chapter-title\"="" ttps:="" docs.redhat.com=""
        en="" documentation="" openshift_container_platform="" 4.10=""
        h="tml/security_and_compliance/encrypting-etcd\""
        _compliance-encrypting-etcd\"="" v-c61ac788="3D\"\""}\<= /li\>
    14. [Scanning pods for
        vulnerabilities](3D%22https://docs.redhat.com/en/documen=){#3D\"sub-link-to-security_and_compliance-pod-vulnerabil=
        .3D\"link =="" sub-chapter-title\"="" tation=""
        openshift_container_platform="" 4.10="" html=""
        security_and_compliance="" pod-v="ulnerability-scan\""
        ity-scan\"="" v-c61ac788="3D\"\""}
    15. [Network-Bound Disk Encryp= tion
        (NBDE)](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-security_and_compliance-network=
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html=""
        security_and_compliance=""
        network-bo="und-disk-encryption-nbde\""
        -bound-disk-encryption-nbde\"="" v-c61ac788="3D\"\""}

6.  Install

7.  Installing
    1.  [Installing]{#3D\"chapter-landing--installing-index\" .3D\"link
        sub-chapter-title="" chapter-landing-page\"=""
        h="ref=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfor="
        m="" 4.10="" html="" installing="" index\"=""
        data="-v-c61ac788=3D\"\""}
    2.  [OpenShift Container Platform ins= tallation
        overview](3D%22ht=){#3D\"sub-link-to-installing-ocp-i= .3D\"link
        sub-chapter-title\"="" tps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        ht="ml/installing/ocp-installation-overview\""
        nstallation-overview\"="" v-c61ac788="3D\"\""}
    3.  [Selecting a cluster installation method and prepari= ng it for
        users](3D%22https://doc=){#3D\"sub-link-to-installing-installing-preparin=
        .3D\"link sub-chapter-title\"="" s.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        instal="ling/installing-preparing\"" g\"="" v-c61ac788="3D\"\""}
    4.  [Disconnected installatio= n
        mirroring](3D%22https://docs.r=){#3D\"sub-link-to-installing-disconn=
        .3D\"link sub-chapter-title\"="" edhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        installin="g/disconnected-installation-mirroring\""
        ected-installation-mirroring\"="" v-c61ac788="3D\"\""}
    5.  [Installing on
        Alibaba](3D%22https://docs.redha=){#3D\"sub-link-to-installing-installing-on-alibaba\"
        .3D\"link sub-chapter-title\"="" t.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        in="stalling-on-alibaba\"" da="ta-v-c61ac788=3D\"\""}
    6.  [Installing on
        AWS](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link-to-installing=
        .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
        installing="" installing-on-aws\"="" -installing-on-aws\"=""
        v-c61ac788="3D\"\""}
    7.  [Installing on=
        Azure](3D%22https://docs.redhat.com/en/documentation/opens=){#3D\"sub=
        .3D\"lin= k="" sub-chapter-title\"="" hift_container_platform=""
        4.10="" html="" installing="" installing-on-azure\"=""
        -link-to-installing-installing-on-azure\"=""
        v-c61ac788="3D\"\""}
    8.  [Installing on Azure Stack
        Hub](3D%22https://docs.redhat.com=){#3D\"sub-link-to-installing-installing-on-azure-st=
        .3D\"link sub-chapter-title\"="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        install="ing-on-azure-stack-hub\"" ack-hub\"=""
        v-c61ac788="3D\"\""}
    9.  [Installing on GC=
        P](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub-=
        .3D\"li= nk="" sub-chapter-title\"=""
        shift_container_platform="" 4.10="" html="" installing=""
        installing-on-gcp\"="" link-to-installing-installing-on-gcp\"=""
        v-c61ac788="3D\"\""}
    10. [Installing on IBM Cloud
        VPC](3D%22https://docs.redhat.com/en/d=){#3D\"sub-link-to-installing-installing-on-ibm-cloud-vpc\"
        .3D\"link sub-chapter-title\"="" ocumentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        installing-o="n-ibm-cloud-vpc\"" =="" v-c61ac788="3D\"\""}
    11. [Installi= ng on-premise with Assisted
        Installer](3D%22https://docs.redha=){#3D\"sub-link-to-installing-i=
        .3D\"link sub-chapter-title\"="" t.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        in="stalling-on-premise-with-assisted-installer\""
        nstalling-on-premise-with-assisted-installer\"=""
        v-c61ac788="3D\"\""}
    12. [Installing on a si= ngle node]{#3D\"sub-link-to-inst= .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
        rm="" 4.10="" html="" installing=""
        installing-on-a-single-node\"=""
        alling-installing-on-a-single-node\"="" v-c61ac788="3D\"\""}
    13. [Deploying installer-provisioned clusters on bare
        metal](3D%22https://docs.redhat.=){#3D\"sub-link-to-insta=
        .3D\"link sub-chapter-title\"="" com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        depl="oying-installer-provisioned-clusters-on-bare-metal\""
        lling-deploying-installer-provisioned-clusters-on-bare-metal\"=""
        v-c61ac7="88=3D\"\""}
    14. Installing IBM Cloud Bare Metal (Classic)
    15. \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/installing/installing-with-=
        z-vm-on-ibm-z-and-linuxone\"
        id=3D\"sub-link-to-installing-installing-with-z-=
        vm-on-ibm-z-and-linuxone\" data-v-c61ac788=3D\"\"\>Installing
        with z/VM on IBM = Z and LinuxONE
    16. [Ins= talling with RHEL KVM on IBM Z and
        LinuxONE](3D%22https://docs.re=){#3D\"sub-link-to-installi=
        .3D\"link sub-chapter-title\"="" dhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        installing="/installing-with-rhel-kvm-on-ibm-z-and-linuxone\""
        ng-installing-with-rhel-kvm-on-ibm-z-and-linuxone\"=""
        v-c61ac788="3D\"\""}
    17. [Installing on IBM Po=
        wer](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"sub-link-to-in=
        .3D\"link sub-chapter-t="itle\"" platform="" 4.10="" html=""
        installing="" installing-on-ibm-power\"=""
        stalling-installing-on-ibm-power\"="" v-c61ac788="3D\"\""}
    18. [Installing on
        OpenStack](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-installing-installing-on-openstack\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        installin="g-on-openstack\"" ="v-c61ac788=3D\"\""}
    19. [Installing on
        RHV](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link-to-installing=
        .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
        installing="" installing-on-rhv\"="" -installing-on-rhv\"=""
        v-c61ac788="3D\"\""}
    20. [Installin= g on
        vSphere](3D%22https://docs.redhat.com/en/documentation/opens=){#3D\"s=
        .3D\"lin= k="" sub-chapter-title\"="" hift_container_platform=""
        4.10="" html="" installing="" installing-on-vsphere\"=""
        ub-link-to-installing-installing-on-vsphere\"=""
        v-c61ac788="3D\"\""}
    21. [Installing on
        VMC](3D%22https://docs.redh=){#3D\"sub-link-to-installing-installing-on-vmc\"
        .3D\"link sub-chapter-title\"="" at.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        installing="" i="nstalling-on-vmc\"" v-c6="1ac788=3D\"\""}
    22. Installing on any platform
    23. = [Installation
        configuration](3D%22https://docs.redhat.com/en/docu=){#3D\"sub-link-to-installing-installation-configuration\"
        .3D\"link sub-chapter-title\"="" mentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        installation-co="nfiguration\"" ="v-c61ac788=3D\"\""}
    24. [Validating an i=
        nstallation](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){#3D\"sub-link-to-=
        .3D\"link sub-chapter-ti="tle\"" latform="" 4.10="" html=""
        installing="" validating-an-installation\"=""
        installing-validating-an-installation\"="" v-c61ac788="3D\"\""}
    25. [Troubleshooting installation
        issues](3D%22https://docs.redha=){#3D\"sub-link-to-installing-installing-troublesh=
        .3D\"link sub-chapter-title\"="" t.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" installing=""
        in="stalling-troubleshooting\"" ooting\"="" v-c61ac788="3D\"\""}
    26. [Support for FI= PS
        cryptography](3D%22https://docs.redhat.com/en/documentatio=){#3D\"=
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html="" installing=""
        installing-fips\"="" sub-link-to-installing-installing-fips\"=""
        v-c61ac788="3D\"\""}

8.  Updating clusters
    1.  [Updating
        clusters](3D%22https://docs.redhat.com/en/documentation/openshift_contai=){#3D\"chapter-landing--upda=
        .3D\"link sub-chapter-title="" chapter-land="ing-page\""
        ner_platform="" 4.10="" html="" updating_clusters="" index\"=""
        ting_clusters-index\"="" v-c61ac788="3D\"\""}
    2.  [Updating clusters
        overview](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub-link-to-updating_clusters-updating-clusters-overview\"
        .3D\"li= nk="" sub-chapter-title\"=""
        shift_container_platform="" 4.10="" html="" updating_clusters=""
        updating-clusters-over="view\"" ="v-c61ac788=3D\"\""}
    3.  [Understanding cluster version condition
        types](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){#3D\"sub-link-to-updating_clusters-unders=
        .3D\"link sub-chapter-ti="tle\"" latform="" 4.10="" html=""
        updating_clusters=""
        understanding-clusterversion-conditiont="ypes_updating-clusters-overview\""
        tanding-clusterversion-conditiontypes_updating-clusters-overview\"=""
        v-c6="1ac788=3D\"\""}
    4.  [Understanding OpenShift
        updates](3D%22https://docs.redhat.com/en/documentation/opensh=){#3D\"sub-link-to-updating_clusters-understanding-openshift-upda=
        .3D\"link= sub-chapter-title\"="" ift_container_platform=""
        4.10="" html="" updating_clusters=""
        understanding-openshift-="updates-1\"" tes-1\"=""
        v-c61ac788="3D\"\""}
    5.  [Understanding update channels and=
        releases](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub-link-to-updating_clusters-understanding-upgrad=
        .3D\"li= nk="" sub-chapter-title\"=""
        shift_container_platform="" 4.10="" html="" updating_clusters=""
        understanding-upgrade-="channels-releases\""
        e-channels-releases\"="" v-c61ac788="3D\"\""}
    6.  [Understa= nding OpenShift Container Platform update
        duration](3D%22https://docs.redhat.=){#3D\"sub-link-to-updating_clus=
        .3D\"link sub-chapter-title\"="" com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        updating_cluste="rs/understanding-openshift-update-duration\""
        ters-understanding-openshift-update-duration\"=""
        v-c61ac788="3D\"\""}
    7.  [Preparing to perform an EUS-to-EUS
        update](3D%22https://docs.redhat.com/en/documentation/openshift_con=){#=3D\"sub-link-to-updating_clusters-preparing-eus-eus-upgrade\"
        .3D\"link sub-ch="apter-title\"" tainer_platform="" 4.10=""
        html="" updating_clusters="" preparing-eus-eus-upgrade\"=""
        v-c61ac78="8=3D\"\""}
    8.  [Updating a cluster using the web =
        console](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-updating_clusters-updating-c=
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        updating_clusters="" up="dating-cluster-within-minor\""
        luster-within-minor\"="" v-c61ac788="3D\"\""}
    9.  [Updating a cluster using the
        CLI](3D%22https://docs.redhat.co=){#3D\"sub-link-to-updating_clusters-updating-cluster=
        .3D\"link sub-chapter-title\"="" m="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        updating_clusters="/updating-cluster-cli\"" -cli\"=""
        v-c61ac788="3D\"\""}
    10. [Performing a canary rollout upd=
        ate](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub-link-to-updating_clusters-update-using-custom=
        .3D\"li= nk="" sub-chapter-title\"=""
        shift_container_platform="" 4.10="" html="" updating_clusters=""
        update-using-custom-ma="chine-config-pools\""
        -machine-config-pools\"="" v-c61ac788="3D\"\""}
    11. [Updating a cluster that includes = RHEL compute
        machines](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-updating_clusters-updating-c=
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        updating_clusters="" up="dating-cluster-rhel-compute\""
        luster-rhel-compute\"="" v-c61ac788="3D\"\""}
    12. [Updating a cluster in a disconnected
        environment](3D%22https://=){#3D\"sub-= .3D\"link
        sub-chapter-title\"="" docs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        upd="ating_clusters/updating-a-cluster-in-a-disconnected-environment\""
        link-to-updating_clusters-updating-a-cluster-in-a-disconnected-environment\"="data-v-c61ac788=3D\"\""}\<=
        /li\>
    13. [Updating h= ardware on nodes running on
        vSphere](3D%22https://docs.redhat.com/en/documen=){#3D\"sub-link-to-updating_clusters-upd=
        .3D\"link =="" sub-chapter-title\"="" tation=""
        openshift_container_platform="" 4.10="" html=""
        updating_clusters=""
        updating-ha="rdware-on-nodes-running-on-vsphere\""
        ating-hardware-on-nodes-running-on-vsphere\"=""
        v-c61ac788="3D\"\""}

    =

Configure

1.  Authentication a= nd authorization
    1.  [Authentication and
        authorization](3D%22https://docs.redha=){#3D\"chapter-landing--authentication_and_author=
        .=3D\"link sub-chapter-title="" chapter-landing-page\"=""
        t.com="" en="" documentation="" openshift_container_platform=""
        4.10="" html="" authenticatio="n_and_authorization/index\""
        ization-index\"="" v-c61ac788="3D\"\""}
    2.  [Overview of authentication and
        authorization](3D%22https://docs.redhat.com/en/documenta=){#3D\"sub-link-to-authenticatio=
        cl="ass=3D\"link" sub-chapter-title\"="" tion=""
        openshift_container_platform="" 4.10="" html=""
        authentication_and_authorizatio="n/overview-of-authentication-authorization\""
        n_and_authorization-overview-of-authentication-authorization\"=""
        v-c61ac7="88=3D\"\""}
    3.  Configuring the i= nternal OAuth server
    4.  [Configuring OAuth clients](3D%22https://d=){#3D\"sub-link-to-a=
        .3D\"link sub-chapter-title\"="" ocs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        auth="entication_and_authorization/configuring-oauth-clients\""
        uthentication_and_authorization-configuring-oauth-clients\"=""
        v-c61ac788="=3D\"\""}
    5.  [Managing user-owned OAuth access
        tokens](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#=3D\"sub-link-to-authentication_and_authorization-managing-oauth-access-toke=
        .3D\"link sub-chapter-title\"="" .10="" html=""
        authentication_and_authorization=""
        managing-oauth-access-tokens\"="" ns\"="" v-c61ac788="3D\"\""}
    6.  [Understanding= identity provider
        configuration](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-authentication_and_author=
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html=""
        authentication_and_authorization=""
        u="nderstanding-identity-provider\""
        ization-understanding-identity-provider\"=""
        v-c61ac788="3D\"\""}
    7.  [Configuring identity
        providers](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){.3D\"link
        sub-chapter-title\"="" .10="" html=""
        authentication_and_authorization=""
        configuring-identity-providers\"=""
        i="d=3D\"sub-link-to-authentication_and_authorization-configuring-identity-prov="
        iders\"="" v-c61ac788="3D\"\""}
    8.  [Using RBAC to define and apply
        permissions](3D%22https://docs.redhat.com/en/documentation/opens=){#3D\"sub-link-to-authentication_and_authorization-using-rbac\"
        .3D\"lin= k="" sub-chapter-title\"="" hift_container_platform=""
        4.10="" html="" authentication_and_authorization=""
        using-rb="ac\"" v-c="61ac788=3D\"\""}
    9.  [Removing the kubeadmin
        user](3D%22https://docs.redhat.com/en/documentation/openshif=){#3D\"sub-link-to-authentication_and_authorization-removing-kubead=
        .3D\"link s="ub-chapter-title\"" t_container_platform="" 4.10=""
        html="" authentication_and_authorization=""
        removing-ku="beadmin\"" min\"="" v-c61ac788="3D\"\""}
    10. [U= nderstanding and creating service
        accounts](3D%22https://docs.redhat.com/en/documentation/openshift_=){#3D\"sub-link-to-authentication_and_author=
        .3D\"link sub="-chapter-title\"" container_platform="" 4.10=""
        html="" authentication_and_authorization=""
        understanding="-and-creating-service-accounts\""
        ization-understanding-and-creating-service-accounts\"=""
        v-c61ac788="3D\"\""}
    11. [Using service accounts in
        applications](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){.3D\"link
        sub-chapter-ti="tle\"" latform="" 4.10="" html=""
        authentication_and_authorization=""
        using-service-accounts\"="id=3D\"sub-link-to-authentication_and_authorization-using-service-accounts\""
        =="" v-c61ac788="3D\"\""}
    12. [Using= a service account as an OAuth
        client](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub-link-to-authentication_and_autho=
        .3D\"li= nk="" sub-chapter-title\"=""
        shift_container_platform="" 4.10="" html=""
        authentication_and_authorization=""
        using-s="ervice-accounts-as-oauth-client\""
        rization-using-service-accounts-as-oauth-client\"=""
        v-c61ac788="3D\"\""}
    13. [= Scoping tokens]{#3D\"sub-lin= .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
        rm="" 4.10="" html="" authentication_and_authorization=""
        tokens-scoping\"=""
        k-to-authentication_and_authorization-tokens-scoping\"=""
        v-c61ac788="3D\"\""}
    14. [Using bound service account
        tokens](3D%22https://docs.re=){#3D\"sub-link-to-auth= .3D\"link
        sub-chapter-title\"="" dhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        authentica="tion_and_authorization/bound-service-account-tokens\""
        entication_and_authorization-bound-service-account-tokens\"=""
        v-c61ac788="=3D\"\""}
    15. Managing security context constraints
    16. = [Impersonating t= he system:admin
        user](3D%22https://docs.redhat.com/en/docu=){#3D\"sub-link-to-authentication_and_aut=
        .3D\"link sub-chapter-title\"="" mentation=""
        openshift_container_platform="" 4.10="" html=""
        authentication_and_authori="zation/impersonating-system-admin\""
        horization-impersonating-system-admin\"="" v-c61ac788="3D\"\""}
    17. Syncing LDAP groups
    18. = [Managing cloud provider
        credentials](3D%22https://docs.redhat.com/en/docu=){#3D\"sub-link-to-authenticatio=
        .3D\"link sub-chapter-title\"="" mentation=""
        openshift_container_platform="" 4.10="" html=""
        authentication_and_authori="zation/managing-cloud-provider-credentials\""
        n_and_authorization-managing-cloud-provider-credentials\"=""
        v-c61ac788="3D=" \"\"=""}
2.  Networki= ng
    1.  [Networking](3D%22https://docs.redhat.com/en/docum=){#3D\"cha=
        .3D\"link sub-c="hapter-title" chapter-landing-page\"=""
        entation="" openshift_container_platform="" 4.10="" html=""
        networking="" index\"="" pter-landing--networking-index\"=""
        v-c61ac788="3D\"\""}
    2.  [Understanding
        networking](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-networking-understanding-networking\"
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html="" networking=""
        understanding-networkin="g\"" v-c61ac788="=3D\"\""}
    3.  [Accessing hosts](3D=){#3D\"sub-link-to-networking-accessing-ho=
        .3D\"link sub-chapter-title\"="" \"https:="" docs.redhat.com=""
        en="" documentation="" openshift_container_platform=""
        4.10="/html/networking/accessing-hosts\"" sts\"=""
        v-c61ac788="3D\"\""}
    4.  [Networking= Operators
        overview](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link-t=
        .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
        networking="" networking-operators-overview\"=""
        o-networking-networking-operators-overview\"=""
        v-c61ac788="3D\"\""}
    5.  [Cluster Network Operator in OpenShift Cont= ainer
        Platform](3D%22https://do=){#3D\"sub-link-to-networking-cluster-networ=
        .3D\"link sub-chapter-title\"="" cs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        netwo="rking/cluster-network-operator\"" k-operator\"=""
        v-c61ac788="3D\"\""}
    6.  [DNS Operator in OpenShift Container
        Platform](3D%22https://docs.re=){#3D\"sub-link-to-networking-dns-operator\"
        .3D\"link sub-chapter-title\"="" dhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        networking="/dns-operator\"" v-c61ac788="=3D\"\""}
    7.  [Ingress Operator in O= penShift Container
        Platform](3D%22https://docs.redhat.com/en/documentation/openshift_con=){#3D\"sub-link-to=
        .3D\"link sub-ch="apter-title\"" tainer_platform="" 4.10=""
        html="" networking="" configuring-ingress\"=""
        -networking-configuring-ingress\"="" v-c61ac788="3D\"\""}
    8.  [Configuring the Ingress Controller endpoint publishin= g
        strategy](3D%22ht=){#3D\"s= .3D\"link sub-chapter-title\"=""
        tps:="" docs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10=""
        ht="ml/networking/nw-ingress-controller-endpoint-publishing-strategies\""
        ub-link-to-networking-nw-ingress-controller-endpoint-publishing-strategies\"="data-v-c61ac788=3D\"\""}
    9.  [Verifying connectivity to an
        endpoint=](3D%22https://docs.redhat=){#3D\"sub-link-to-networking-verifying-connec=
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        ver="ifying-connectivity-endpoint\"" tivity-endpoint\"=""
        v-c61ac788="3D\"\""}
    10. [Changing the MTU for the cluster
        network](3D%22https://docs.redhat.com/en/do=){#3D\"sub-link-to-networking-changing-cluster-network-mtu\"=
        .3D\"link sub-chapter-title\"="" cumentation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        changing-clus="ter-network-mtu\"" v-c61ac788="3D\"\""}
    11. [Configuring the node port service
        range](3D%22https://docs.redhat.com/en/documentation/o=){#3D\"sub-link-to-networking-configuring-node-port-service-range=
        .3D= \"link="" sub-chapter-title\"=""
        penshift_container_platform="" 4.10="" html="" networking=""
        configuring-node-port-serv="ice-range\"" \"=""
        v-c61ac788="3D\"\""}
    12. [Con= figuring IP
        failover](3D%22https://docs.redhat.com/en/documentation/o=){#=3D\"sub-link-to-networking-configuring-ipfailover\"
        .3D= \"link="" sub-chapter-title\"=""
        penshift_container_platform="" 4.10="" html="" networking=""
        configuring-ipfailover\"="" v-c61ac788="3D\"\""}
    13. [Using the Stream Control Transmission Protocol (SCTP) on a bare
        metal=
        cluster](3D%22https://d=){#3D\"sub-link-to-networking-using-sctp\"
        .3D\"link sub-chapter-title\"="" ocs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        netw="orking/using-sctp\"" v-c61ac788="=3D\"\""}
    14. [Using PT= P
        hardware](3D%22https://docs.redhat.c=){#3D\"sub-link-to-networking-using-ptp\"
        .3D\"link sub-chapter-title\"="" om="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        using="-ptp\"" v-c61ac788="3D\"\""}
    15. [External DNS
        Operator](3D%22https://docs.redhat=){#3D\"sub-link-to-networking-external-dns-operator-1\"=
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        ext="ernal-dns-operator-1\"" v-c61ac788="3D\"\""}
    16. [Network
        policy](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"sub-link-to-networking-=
        .3D\"link sub-chapter-t="itle\"" platform="" 4.10="" html=""
        networking="" network-policy\"="" v-c61ac788="3D\"\""}
    17. [Hardwar= e
        networks](3D%22https://docs.redhat.com/en/documenta=){cl="ass=3D\"link"
        sub-chapter-title\"="" tion="" openshift_container_platform=""
        4.10="" html="" networking="" hardware-networks\"=""
        i="d=3D\"sub-link-to-networking-hardware-networks\""
        v-c61ac788="3D\"\""}
    18. [OpenShift SDN d= efault CNI network
        provider](3D%22https://docs.redhat=){#3D\"sub-link-to-networking-opens=
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        ope="nshift-sdn-default-cni-network-provider\""
        hift-sdn-default-cni-network-provider\"="" v-c61ac788="3D\"\""}
    19. [OVN-Kubernetes default CNI network
        provider](3D%22ht=){#3D\"sub-link-t= .3D\"link
        sub-chapter-title\"="" tps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        ht="ml/networking/ovn-kubernetes-default-cni-network-provider\""
        o-networking-ovn-kubernetes-default-cni-network-provider\"=""
        v-c61ac788="=3D\"\""}
    20. [Configuring ingress cluster
        traffic](3D%22https://docs.redhat.com/en/document=){#3D\"sub-link-to-networking-configuring-ingress-cluster-=
        c="lass=3D\"link" sub-chapter-title\"="" ation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        configuring-ingress="-cluster-traffic\"" traffic\"=""
        v-c61ac788="3D\"\""}
    21. [Kuberne= tes
        NMState](3D%22https://docs.redhat.com/en/documentatio=){#=3D\"sub-link-to-networking-kubernetes-nmstate\"
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html="" networking=""
        kubernetes-nmstate\"="" v-c61ac788="3D\"\""}
    22. [Configuring the cluster-wide
        proxy](3D%22https://docs.redha=){#3D\"sub-link-to-networking-enable-cluster-wide-p=
        .3D\"link sub-chapter-title\"="" t.com="" documentation=""
        openshift_container_platform="" 4.10="" html="" networking=""
        en="able-cluster-wide-proxy\"" roxy\"="" v-c61ac788="3D\"\""}
    23. [= Configuring a custom
        PKI](3D%22https://docs.redhat.com/en/documentation/op=){.3D\"=
        link="" sub-chapter-title\"="" enshift_container_platform=""
        4.10="" html="" networking="" configuring-a-custom-pki\"=""
        i="d=3D\"sub-link-to-networking-configuring-a-custom-pki\""
        v-c61ac788="3D\"\""}
    24. [Load balancing on
        RHOSP](3D%22https=){#3D\"sub-link-to-networking-load-bala=
        .3D\"link sub-chapter-title\"="" :="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        =="" networking="" load-balancing-openstack\"=""
        ncing-openstack\"="" v-c61ac788="3D\"\""}
    25. [Load balancing with
        MetalLB](3D%22https://docs.redhat.com/en/documentation/op=){.3D\"=
        link="" sub-chapter-title\"="" enshift_container_platform=""
        4.10="" html="" networking=""
        load-balancing-with-metallb=" id=3D"
        sub-link-to-networking-load-balancing-with-metallb\"=""
        v-c61ac788="=3D\"\""}
    26. [Associating secondary int= erfaces metrics to network
        attachments](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-networking-associating-secondary-interfaces-met=
        .3D\"link sub-chapter-title\"="" .10="" html="" networking=""
        associating-secondary-interfaces-metrics-to-network-att="achments\""
        rics-to-network-attachments\"="" v-c61ac788="3D\"\""}
    27. [Network Observability]{#3D\"sub-link-to-networkin= .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platf="
        orm="" 4.10="" html="" networking="" network-observability\"=""
        g-network-observability\"="" v-c61ac788="3D\"\""}
3.  Registry
    1.  [Registry](3D%22http=){#3D\"chapter-landing--registry-index\"
        .3D\"link sub-chapter-title="" chapter-landing-page\"="" s:=""
        docs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="/registry/index\""
        v-c61ac788="3D\"=" \"=""}
    2.  [OpenShift image registry
        overview](3D%22https://docs.redhat=){#3D\"sub-link-to-registry-registry-overview-1\"
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" registry=""
        regis="try-overview-1\"" v-c61a="c788=3D\"\""}
    3.  [Image Regist= ry Operator in OpenShift Container
        Platform](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"sub-link-t=
        .3D\"link sub-chapter-t="itle\"" platform="" 4.10="" html=""
        registry="" configuring-registry-operator\"=""
        o-registry-configuring-registry-operator\"=""
        v-c61ac788="3D\"\""}
    4.  [Setting up and configuring the
        registry](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"=
        .3D\"link sub-chapter-t="itle\"" platform="" 4.10="" html=""
        registry="" setting-up-and-configuring-the-registry\"=""
        sub-link-to-registry-setting-up-and-configuring-the-registry\"=""
        v-c61ac7="88=3D\"\""}
    5.  [Exposing the
        registry](3D%22https://docs.redhat.com/en/do=){#3D\"sub-link-to-registry-securing-exposing-registry\"
        .3D\"link sub-chapter-title\"="" cumentation=""
        openshift_container_platform="" 4.10="" html="" registry=""
        securing-exposi="ng-registry\"" v-="c61ac788=3D\"\""}

    =
4.  Post-instal= lation configuration
    1.  [Post-installation
        configuration](3D%22https://docs.r=){#3D\"chapter-landing--post-installation_conf=
        c="lass=3D\"link" sub-chapter-title="" chapter-landing-page\"=""
        edhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        post-inst="allation_configuration/index\"" iguration-index\"=""
        v-c61ac788="3D\"\""}
    2.  [Pos= t-installation configuration
        overview](3D%22https://docs.redhat.com/en/document=){#3D\"sub-link-to-post-installation_=
        c="lass=3D\"link" sub-chapter-title\"="" ation=""
        openshift_container_platform="" 4.10="" html=""
        post-installation_configuratio="n/post-install-configuration-overview\""
        configuration-post-install-configuration-overview\"=""
        v-c61ac788="3D\"\""}
    3.  [Configuring a private cluster]{.3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
        rm="" 4.10="" html="" post-installation_configuration=""
        configuring-private-cluster\"=""
        i="d=3D\"sub-link-to-post-installation_configuration-configuring-private-cluste="
        r\"="" v-c61ac788="3D\"\""}
    4.  [Bare metal conf=
        iguration](3D%22https://docs.redhat.com/en/documentation/openshift_=){#3D\"sub-link-to-post-installation_configuration-=
        .3D\"link sub="-chapter-title\"" container_platform="" 4.10=""
        html="" post-installation_configuration=""
        post-install-b="are-metal-configuration\""
        post-install-bare-metal-configuration\"="" v-c61ac788="3D\"\""}
    5.  [Post-installation machine configuration
        tasks](3D%22https://docs.redhat.=){#3D\"sub-link-t= .3D\"link
        sub-chapter-title\"="" com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        post-installati="on_configuration/post-install-machine-configuration-tasks\""
        o-post-installation_configuration-post-install-machine-configuration-tasks\"="data-v-c61ac788=3D\"\""}
    6.  [Post-installation clust= er
        tasks](3D%22https://docs.redhat.com/en/documentat=){#3D\"sub-link-to-post-installation_configurati=
        cla="ss=3D\"link" sub-chapter-title\"="" ion=""
        openshift_container_platform="" 4.10="" html=""
        post-installation_configuration="" ==""
        post-install-cluster-tasks\"=""
        on-post-install-cluster-tasks\"="" v-c61ac788="3D\"\""}
    7.  [Post-installa= tion node
        tasks](3D%22https://docs.redhat.c=){#3D\"sub-link-to-post-installatio=
        .3D\"link sub-chapter-title\"="" om="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        post-installatio="n_configuration/post-install-node-tasks\""
        n_configuration-post-install-node-tasks\"=""
        v-c61ac788="3D\"\""}
    8.  [Post-installation network
        configuration](3D%22https://docs.r=){#3D\"sub-link-t= .3D\"link
        sub-chapter-title\"="" edhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        post-inst="allation_configuration/post-install-network-configuration\""
        o-post-installation_configuration-post-install-network-configuration\"=""
        ="v-c61ac788=3D\"\""}
    9.  [Post-installation s= torage
        configuration](3D%22https://docs.redhat.com/en/documentation/openshif=){#3D\"sub-link-to-post-installation_configuration-p=
        .3D\"link s="ub-chapter-title\"" t_container_platform="" 4.10=""
        html="" post-installation_configuration=""
        post-install="-storage-configuration\""
        ost-install-storage-configuration\"="" v-c61ac788="3D\"\""}
    10. [Preparing for users](3D%22https://d=){#3D\"sub-lin= .3D\"link
        sub-chapter-title\"="" ocs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        post="-installation_configuration/post-install-preparing-for-users\""
        k-to-post-installation_configuration-post-install-preparing-for-users\"=""
        data="-v-c61ac788=3D\"\""}
    11. [Configuring alert notifications]{.3D\"link
        sub-chapter-title\"=""
        h="ref=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfor="
        m="" 4.10="" html="" post-installation_configuration=""
        configuring-alert-notifications=" id=3D"
        sub-link-to-post-installation_configuration-configuring-alert-notif="ications\""
        v-c61ac788="3D\"\""}
    12. [Converting a connected cluster= to a disconnected
        cluster](3D%22https://docs.redhat.com/en/documentation/o=){#3D\"sub-link-to-post-installation_configuration-con=
        .3D= \"link="" sub-chapter-title\"=""
        penshift_container_platform="" 4.10="" html=""
        post-installation_configuration=""
        conne="cted-to-disconnected\"" nected-to-disconnected\"=""
        v-c61ac788="3D\"\""}
    13. [Configuring additional d= evices in an IBM Z or LinuxONE
        environment](3D%22htt=){#3D\"sub-link-to-post-installation_configuration-post-install-confi=
        .3D\"link sub-chapter-title\"="" ps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        htm="l/post-installation_configuration/post-install-configure-additional-devices="
        -ibmz\"="" gure-additional-devices-ibmz\"=""
        v-c61ac788="3D\"\""}
5.  St= orage
    1.  [Storage](3D%22https://docs.redhat.com/en/=){#3D\"c= .3D\"link
        =="" sub-chapter-title="" chapter-landing-page\"=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        storage="" index\"="" hapter-landing--storage-index\"=""
        v-c61ac788="3D\"\""}
    2.  [OpenShift Container Plat= form storage
        overview](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub-link=
        .3D\"li= nk="" sub-chapter-title\"=""
        shift_container_platform="" 4.10="" html="" storage=""
        storage-overview\"="" -to-storage-storage-overview\"=""
        v-c61ac788="3D\"\""}
    3.  Understanding ephemeral storage\<= /a\>
    4.  [Understanding persistent
        storage](3D%22https://docs.redhat.com/en/doc=){#3D\"sub-link-to-storage-understanding-persistent-storage=
        .3D\"link sub-chapter-title\"="" umentation=""
        openshift_container_platform="" 4.10="" html="" storage=""
        understanding-per="sistent-storage\"" \"="" v-c61ac788="3D\"\""}
    5.  [Configuring persistent
        storage](3D%22https://docs.redhat.com/en/documentation/openshif=){#=3D\"sub-link-to-storage-configuring-persistent-storage\"
        .3D\"link s="ub-chapter-title\"" t_container_platform="" 4.10=""
        html="" storage="" configuring-persistent-storage\"=""
        v-c61ac788="3D\"=" \"=""}
    6.  [Using Co= ntainer Storage Interface
        (CSI)](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-s=
        .3D\"link sub-chapter-title\"="" .10="" html="" storage=""
        using-container-storage-interface-csi\"=""
        torage-using-container-storage-interface-csi\"=""
        v-c61ac788="3D\"\""}
    7.  [Expanding persistent volum=
        es](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-storage-ex=
        .3D\"link sub-chapter-title\"="" .10="" html="" storage=""
        expanding-persistent-volumes\"=""
        panding-persistent-volumes\"="" v-c61ac788="3D\"\""}
    8.  [Dynamic
        provisioning](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-storage-dynamic-provisioning\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" storage=""
        dynamic-prov="isioning\"" v-c61ac788="=3D\"\""}

Migr= ate

1.  Migrating from version 3 to = 4
    1.  [Migrating from version 3 to
        4](3D%22https://docs.redhat.com/en/docume=){#3D\"chapter-landing--migrating_from_version_3_to_4-index\"
        .3D\"link sub-ch="apter-title" chapter-landing-page\"=""
        ntation="" openshift_container_platform="" 4.10="" html=""
        migrating_from_version_3_to_="4/index\"" v="-c61ac788=3D\"\""}
    2.  [Migration from OpenShift C= ontainer Platform 3 to 4
        overview](3D%22https://docs.redhat.com/en/documentation/openshift_container=){#3D\"sub-link-to-migrating_from_version_3_to_4-migration-fr=
        .3D\"link sub-chapter-="title\"" _platform="" 4.10="" html=""
        migrating_from_version_3_to_4=""
        migration-from-version-3-="to-4-overview\""
        om-version-3-to-4-overview\"="" v-c61ac788="3D\"\""}
    3.  About migrating from OpenShift Container Platform 3 to 4
    4.  \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/migrating_from_version_3_to=
        \_4/planning-migration-3-4\"
        id=3D\"sub-link-to-migrating_from_version_3_to_4-=
        planning-migration-3-4\" data-v-c61ac788=3D\"\"\>Differences
        between OpenShift = Container Platform 3 and 4
    5.  [Network considerations](3D%22htt=){#3D\"sub-link= .3D\"link
        sub-chapter-title\"="" ps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        htm="l/migrating_from_version_3_to_4/planning-considerations-3-4\""
        -to-migrating_from_version_3_to_4-planning-considerations-3-4\"=""
        v-c61ac="788=3D\"\""}
    6.  [About the Mi= gration Toolkit for
        Containers](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-mig=
        .3D\"link sub-chapter-title\"="" .10="" html=""
        migrating_from_version_3_to_4="" about-mtc-3-4\"=""
        rating_from_version_3_to_4-about-mtc-3-4\"=""
        v-c61ac788="3D\"\""}
    7.  [Installing th= e Migration Toolkit for
        Containers](3D=){#3D\"sub-link-to-migra= .3D\"link
        sub-chapter-title\"="" \"https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform=""
        4.10="/html/migrating_from_version_3_to_4/installing-3-4\""
        ting_from_version_3_to_4-installing-3-4\"=""
        v-c61ac788="3D\"\""}
    8.  [Installing the Migration Toolkit for Containers in a restricte=
        d network environment]{#3D\"su= .3D\"link sub-chapter-title\"=""
        hre="f=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform/="
        4.10="" html="" migrating_from_version_3_to_4=""
        installing-restricted-3-4\"=""
        b-link-to-migrating_from_version_3_to_4-installing-restricted-3-4\"=""
        v-c="61ac788=3D\"\""}
    9.  [Upgrading the Migration = Toolkit for
        Containers](3D%22https://=){#3D\"sub-link-to-migrating_from_=
        .3D\"link sub-chapter-title\"="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        mig="rating_from_version_3_to_4/upgrading-3-4\""
        version_3_to_4-upgrading-3-4\"="" v-c61ac788="3D\"\""}
    10. [Premigration checklists](3D%22https:/=){#3D\"sub-link-to-=
        .3D\"link sub-chapter-title\"="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        mi="grating_from_version_3_to_4/premigration-checklists-3-4\""
        migrating_from_version_3_to_4-premigration-checklists-3-4\"=""
        v-c61ac788="=3D\"\""}
    11. [Migrating your applications](3D%22=){#3D\"sub-li= .3D\"link
        sub-chapter-title\"="" https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" ==""
        html="" migrating_from_version_3_to_4=""
        migrating-applications-3-4\"=""
        nk-to-migrating_from_version_3_to_4-migrating-applications-3-4\"=""
        v-c61a="c788=3D\"\""}
    12. [Advanced migration options]{.3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
        rm="" 4.10="" html="" migrating_from_version_3_to_4=""
        advanced-migration-options-3-4\"="id=3D\"sub-link-to-migrating_from_version_3_to_4-advanced-migration-options-="
        3-4\"="" v-c61ac788="3D\"\""}

    \<= /li\>
2.  Migration To= olkit for Containers
    1.  Migration Toolkit for Containers
    2.  \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/migration_toolkit_for_conta=
        iners/about-mtc\"
        id=3D\"sub-link-to-migration_toolkit_for_containers-about-m=
        tc\" data-v-c61ac788=3D\"\"\>About the Migration Toolkit for
        Containers
    3.  [Migration Toolkit for Containers releas= e
        notes](3D%22https://docs.redhat.com/en/documentat=){#3D\"sub-link-to-migration_toolkit_for_containers-mtc-=
        cla="ss=3D\"link" sub-chapter-title\"="" ion=""
        openshift_container_platform="" 4.10="" html=""
        migration_toolkit_for_containers="/mtc-release-notes\""
        release-notes\"="" v-c61ac788="3D\"\""}
    4.  [Installing the Migration Toolk= it for
        Containers](3D%22https://docs.redhat.co=){#3D\"sub-link-to-migration_toolkit_for_con=
        .3D\"link sub-chapter-title\"="" m="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        migration_toolkit="_for_containers/installing-mtc\""
        tainers-installing-mtc\"="" v-c61ac788="3D\"\""}
    5.  [Installing the Migration Toolkit for Containers in a restricted
        network e=
        nvironment](3D%22https://docs=){#3D\"sub-link-to-migr= .3D\"link
        sub-chapter-title\"="" .redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        migrati="on_toolkit_for_containers/installing-mtc-restricted\""
        ation_toolkit_for_containers-installing-mtc-restricted\"=""
        v-c61ac788="3D\"=" \"=""}
    6.  [Upgrading the Migration Toolk= it for
        Containers](3D%22https://docs.redhat=){#3D\"sub-link-to-migration_toolkit_for_c=
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        migration_tool="kit_for_containers/upgrading-mtc\""
        ontainers-upgrading-mtc\"="" v-c61ac788="3D\"\""}
    7.  [Premigration
        checklists](3D%22https://docs=){#3D\"sub-link-to-mi= .3D\"link
        sub-chapter-title\"="" .redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        migrati="on_toolkit_for_containers/premigration-checklists-mtc\""
        gration_toolkit_for_containers-premigration-checklists-mtc\"=""
        v-c61ac788="=3D\"\""}
    8.  [Network considerations](3D%22=){#3D\"sub= .3D\"link
        sub-chapter-title\"="" https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" ==""
        html="" migration_toolkit_for_containers=""
        network-considerations-mtc\"=""
        -link-to-migration_toolkit_for_containers-network-considerations-mtc\"=""
        ="v-c61ac788=3D\"\""}
    9.  [Migrating your
        applications]{#3D\"sub-link-to-migration_toolkit_for_containers-migrating-applicati=
        .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platf="
        orm="" 4.10="" html="" migration_toolkit_for_containers=""
        migrating-applications-with-="mtc\"" ons-with-mtc\"=""
        v-c61ac788="3D\"\""}
    10. [Advanced migration=
        options](3D%22https://docs.redhat.com/en/documentation/o=){#3D\"sub-link-to-migration_toolkit_for_contain=
        .3D= \"link="" sub-chapter-title\"=""
        penshift_container_platform="" 4.10="" html=""
        migration_toolkit_for_containers=""
        adva="nced-migration-options-mtc\""
        ers-advanced-migration-options-mtc\"="" v-c61ac788="3D\"\""}
    11. [Troubleshooting](3D%22https://docs.redhat.c=){#3D\"sub-link-to-migration_toolkit_f=
        .3D\"link sub-chapter-title\"="" om="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        migration_toolki="t_for_containers/troubleshooting-mtc\""
        or_containers-troubleshooting-mtc\"="" v-c61ac788="3D\"\""}=

Manage

Backup and restore

1.  [Backup and
    restore](3D=){#3D\"chapter-landing--backup_and_restore-i= .3D\"link
    sub-chapter-title="" chapter-landing-page\"="" \"https:=""
    docs.redhat.com="" en="" documentation=""
    openshift_container_platform=""
    4.10="/html/backup_and_restore/index\"" ndex\"=""
    v-c61ac788="3D\"\""}
2.  [Ba= ckup and
    restore](3D%22https://docs.redhat.com/en/documentation/openshift_containe=){#3D\"sub-=
    .3D\"link sub-chapter="-title\"" r_platform="" 4.10="" html=""
    backup_and_restore="" backup-restore-overview\"=""
    link-to-backup_and_restore-backup-restore-overview\"=""
    v-c61ac788="3D\"\""}
3.  [Shutting down the cluster g=
    racefully](3D%22https://docs.=){#3D\"sub-link-to-backup_and_restore-=
    .3D\"link sub-chapter-title\"="" redhat.com="" en=""
    documentation="" openshift_container_platform="" 4.10="" html=""
    backup_a="nd_restore/graceful-shutdown-cluster\""
    graceful-shutdown-cluster\"="" v-c61ac788="3D\"\""}
4.  Restarting the cluster gracefully
5.  \<= a class=3D\"link sub-chapter-title\"
    href=3D\"https://docs.redhat.com/en/docum=
    entation/openshift_container_platform/4.10/html/backup_and_restore/applicat=
    ion-backup-and-restore\"
    id=3D\"sub-link-to-backup_and_restore-application-ba=
    ckup-and-restore\" data-v-c61ac788=3D\"\"\>Application backup and
    restore
6.  Control plane backup and restore

Machine management

1.  [Machine management]{#3D\"chapter-landing--machine_man= .3D\"link
    sub-chapter-title="" chapter-landing-page=" href=3D" https:=""
    docs.redhat.com="" en="" documentation=""
    openshift_container_plat="form/4.10/html/machine_management/index\""
    agement-index\"="" v-c61ac788="3D\"\""}
2.  [Overview of machine
    management](3D%22https://docs.redhat.com/en/documentation/openshift=){#3D\"sub-link-to-machine_management-overview-of-machine-management\"
    .3D\"link su="b-chapter-title\"" _container_platform="" 4.10=""
    html="" machine_management="" overview-of-machine-manage="ment\""
    =="" v-c61ac788="3D\"\""}
3.  [Manually scaling a= machine
    set](3D%22https://=){#3D\"sub-link-to-machine_mana= .3D\"link
    sub-chapter-title\"="" docs.redhat.com="" en="" documentation=""
    openshift_container_platform="" 4.10="" html=""
    mac="hine_management/manually-scaling-machineset\""
    gement-manually-scaling-machineset\"="" v-c61ac788="3D\"\""}
4.  [Modifying a machine
    set](3D%22https://docs.redh=){#3D\"sub-link-to-machine_management-modifying=
    .3D\"link sub-chapter-title\"="" at.com="" en="" documentation=""
    openshift_container_platform="" 4.10="" html=""
    machine_mana="gement/modifying-machineset\"" -machineset\"=""
    v-c61ac788="3D\"\""}
5.  [Dele= ting a
    machine](3D%22https://docs.redhat.com/en/documentation/opensh=){#3D=
    .3D\"link= sub-chapter-title\"="" ift_container_platform="" 4.10=""
    html="" machine_management="" deleting-machine\"=""
    \"sub-link-to-machine_management-deleting-machine\"=""
    v-c61ac788="3D\"\""}
6.  [Applying autoscaling to an OpenShift Co= ntainer Platform
    cluster](3D%22https://docs.re=){#3D\"sub-link-to-machine_management-applyin=
    .3D\"link sub-chapter-title\"="" dhat.com="" en="" documentation=""
    openshift_container_platform="" 4.10="" html=""
    machine_ma="nagement/applying-autoscaling\"" g-autoscaling\"=""
    v-c61ac788="3D\"\""}
7.  [Creating infrastructure machine
    sets](3D%22https=){#3D\"sub-link-to-m= .3D\"link
    sub-chapter-title\"="" :="" docs.redhat.com="" en=""
    documentation="" openshift_container_platform="" 4.10="" html=""
    =="" machine_management="" creating-infrastructure-machinesets\"=""
    achine_management-creating-infrastructure-machinesets\"=""
    v-c61ac788="3D\"\"="}
8.  [Adding RHEL comput= e machines to an OpenShift Container Platform
    cluster]{#3D\"sub-link-to-mach= .3D\"link
    sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
    rm="" 4.10="" html="" machine_management="" adding-rhel-compute\"=""
    ine_management-adding-rhel-compute\"="" v-c61ac788="3D\"\""}
9.  [Adding= more RHEL compute machines to an OpenShift Container
    Platform
    cluster](3D%22https://docs.redhat.com/en/documentation/openshift_=){#3D\"su=
    .3D\"link sub="-chapter-title\"" container_platform="" 4.10=""
    html="" machine_management="" more-rhel-compute\"=""
    b-link-to-machine_management-more-rhel-compute\"=""
    v-c61ac788="3D\"\""}\<= /li\>
10. [= Managing user-provisioned infrastructure
    manually](3D%22https://docs.redhat.com/en/documen=){#3D\"sub-link-to-machine_manageme=
    .3D\"link =="" sub-chapter-title\"="" tation=""
    openshift_container_platform="" 4.10="" html=""
    machine_management=""
    managing-u="ser-provisioned-infrastructure-manually\""
    nt-managing-user-provisioned-infrastructure-manually\"=""
    v-c61ac788="3D\"\""}
11. Web console
    1.  [Web co=
        nsole](3D%22https://docs.redha=){#3D\"chapter-landing--web_console-index\"
        .=3D\"link sub-chapter-title="" chapter-landing-page\"=""
        t.com="" en="" documentation="" openshift_container_platform=""
        4.10="" html="" web_console="" i="ndex\"" v-c61ac788="3D\"\""}
    2.  [Web Console
        Overview](3D%22https://docs.redhat.com/=){#3D\"sub-link-to-web_console-web-console-overview\"
        .3D\"link sub-chapter-title\"="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" web_console=""
        web-con="sole-overview\"" v-c="61ac788=3D\"\""}
    3.  [Accessing the web
        console](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-web_console-web-console=
        .3D\"link sub-chapter-title\"="" .10="" html="" web_console=""
        web-console\"="" \"="" v-c61ac788="3D\"\""}
    4.  [Adding user
        preferences](3D%22https://docs.redha=){#3D\"sub-link-to-web_console-adding-user-preferenc=
        .3D\"link sub-chapter-title\"="" t.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" web_console=""
        a="dding-user-preferences\"" es\"="" v-c61ac788="3D\"\""}
    5.  [Customizing the= web console in OpenShift Container
        Platform](3D%22https://docs.redhat.com/en/documentation/openshift_contain=){#3D\"sub-link-t=
        .3D\"link sub-chapte="r-title\"" er_platform="" 4.10="" html=""
        web_console="" customizing-web-console\"=""
        o-web_console-customizing-web-console\"="" v-c61ac788="3D\"\""}
    6.  [Adding a dynamic plugin to the Op= enShift Container Platform
        web
        console](3D%22https://docs.redhat.com/en/documentation/openshift_container=){#3D\"sub-link-to-web_cons=
        .3D\"link sub-chapter-="title\"" _platform="" 4.10="" html=""
        web_console="" dynamic-plugins\"="" ole-dynamic-plugins\"=""
        v-c61ac788="3D\"\""}
    7.  [Web terminal]{#3D\"sub-link-to-web_console-web-t= .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platf="
        orm="" 4.10="" html="" web_console="" web-terminal\"=""
        erminal\"="" v-c61ac788="3D\"\""}
    8.  [Disabling the web conso= le in OpenShift Container
        Platform](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){#3D\"sub-link-to-web_=
        .3D\"link sub-chapter-ti="tle\"" latform="" 4.10="" html=""
        web_console="" disabling-web-console\"=""
        console-disabling-web-console\"="" v-c61ac788="3D\"\""}
    9.  [Creating quic= k start tutorials in the web
        console]{#3D\"sub-link-to-web= .3D\"link sub-chapter-title\"=""
        hre="f=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform/="
        4.10="" html="" web_console=""
        creating-quick-start-tutorials\"=""
        _console-creating-quick-start-tutorials\"=""
        v-c61ac788="3D\"\""}

Reference

1.  CLI tools
    1.  [CLI
        tools](3D%22https://docs.redhat.com/en/documentation/=){#3D\"chapter-landi=
        .3D\"link sub-chapter-ti="tle" chapter-landing-page\"=""
        openshift_container_platform="" 4.10="" html="" cli_tools=""
        index\"="" ng--cli_tools-index\"="" v-c61ac788="3D\"\""}
    2.  [OpenShift CLI
        (oc)](3D%22https:=){#3D\"sub-link-to-cli_tools-openshift-cli-oc\"
        .3D\"link sub-chapter-title\"="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        c="li_tools/openshift-cli-oc\"" da="ta-v-c61ac788=3D\"\""}
    3.  [Important update on odo]{#3D\"sub-link-to-cli_tools-devel=
        .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
        rm="" 4.10="" html="" cli_tools="" developer-cli-odo\"=""
        oper-cli-odo\"="" v-c61ac788="3D\"\""}
    4.  [Knative CLI for use with Open= Shift
        Serverless](3D%22https://docs.redhat.com/en/documentation/opens=){#3D\"sub-link-to=
        .3D\"lin= k="" sub-chapter-title\"="" hift_container_platform=""
        4.10="" html="" cli_tools="" kn-cli-tools\"=""
        -cli_tools-kn-cli-tools\"="" v-c61ac788="3D\"\""}
    5.  [Pipelines CLI
        (tkn)](3D%22https://docs.=){#3D\"sub-link-to-cli_tools-pipelines-cli-tkn\"
        .3D\"link sub-chapter-title\"="" redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        cli_tool="s/pipelines-cli-tkn\"" v-="c61ac788=3D\"\""}
    6.  [opm
        CLI](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-cli_tools-opm-cli\"
        .3D\"link sub-chapter-title\"="" .10="" html="" cli_tools=""
        opm-cli\"="" v-c61="ac788=3D\"\""}
    7.  [Operator
        SDK](3D%22https://doc=){#3D\"sub-link-to-cli_tools-operator-sdk\"
        .3D\"link sub-chapter-title\"="" s.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        cli_to="ols/operator-sdk\"" v-c61ac788="=3D\"\""}

D= evelop

1.  Building applications
    1.  [Buil= ding
        applications](3D%22https://docs.redhat.com/en/documentati=){#=3D\"chapter-landing--building_applications-index\"
        .3D\"link sub-chapter="-title" chapter-landing-page\"="" on=""
        openshift_container_platform="" 4.10="" html=""
        building_applications="" index\"="" v-c61ac788="3D\"\""}
    2.  [Building a= pplications
        overview](3D%22https://docs=){#3D\"sub-link-to-building_a=
        .3D\"link sub-chapter-title\"="" .redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        buildin="g_applications/building-applications-overview\""
        pplications-building-applications-overview\"=""
        v-c61ac788="3D\"\""}
    3.  [Projects](3D%22https://d=){#3D\"sub-link-to-building_applications-project=
        .3D\"link sub-chapter-title\"="" ocs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        buil="ding_applications/projects\"" s\"="" v-c61ac788="3D\"\""}
    4.  [Creating app=
        lications](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-bui=
        .3D\"link sub-chapter-title\"="" .10="" html=""
        building_applications="" creating-applications\"=""
        lding_applications-creating-applications\"=""
        v-c61ac788="3D\"\""}
    5.  [Viewing application composition using the T= opology
        view](3D%22https://docs.redhat.=){#3D\"sub-l= .3D\"link
        sub-chapter-title\"="" com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        building_applic="ations/odc-viewing-application-composition-using-topology-view\""
        ink-to-building_applications-odc-viewing-application-composition-using-topo="logy-view\""
        v-c61ac788="3D\"\""}
    6.  Exporting applications\<= /a\>
    7.  [Connecting applica= tions to
        services](3D%22https://docs.redhat.com/en/doc=){#3D\"sub-link-to-building_applications-c=
        .3D\"link sub-chapter-title\"="" umentation=""
        openshift_container_platform="" 4.10="" html=""
        building_applications=""
        con="necting-applications-to-services\""
        onnecting-applications-to-services\"="" v-c61ac788="3D\"\""}
    8.  [Working with Helm char=
        ts](3D%22https://docs=){#3D\"sub-link-to-building_applica=
        .3D\"link sub-chapter-title\"="" .redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        buildin="g_applications/working-with-helm-charts\""
        tions-working-with-helm-charts\"="" v-c61ac788="3D\"\""}
    9.  [Deployments](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-building_applications-deployments\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        building_application="s/deployments\"" v-="c61ac788=3D\"\""}
    10. [Quotas](3D%22http=){#3D\"sub-link-to-building_applications-quot=
        .3D\"link sub-chapter-title\"="" s:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        html="/building_applications/quotas\"" as\"=""
        v-c61ac788="3D\"\""}
    11. [Using config maps with applicati=
        ons](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-building_appl=
        .3D\"link sub-chapter-title\"="" .10="" html=""
        building_applications="" config-maps\"=""
        ications-config-maps\"="" v-c61ac788="3D\"\""}
    12. [Monitoring= project and application metrics using the Developer
        perspective](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-building_applications-odc-monitoring-project-and-appli=
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        building_application="s/odc-monitoring-project-and-application-metrics-using-developer-perspectiv="
        e\"="" cation-metrics-using-developer-perspective\"=""
        v-c61ac788="3D\"\""}
    13. [Monitoring application health by using health
        checks](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-building_applications-application-health\"
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html=""
        building_applications="" application-="health\""
        v-="c61ac788=3D\"\""}
    14. [Editing
        applications](3D%22https://docs.redhat.com/en/documentati=){#3D\"sub-link-to-building_applications-odc-editing-applicat=
        clas="s=3D\"link" sub-chapter-title\"="" on=""
        openshift_container_platform="" 4.10="" html=""
        building_applications="" odc-editing="-applications\"" ions\"=""
        v-c61ac788="3D\"\""}
    15. [Idling applications](3D%22htt=){#3D\"sub-link-to-building_app=
        .3D\"link sub-chapter-title\"="" ps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        htm="l/building_applications/idling-applications\""
        lications-idling-applications\"="" v-c61ac788="3D\"\""}=
    16. Deleting applications
    17. [Using the Red Hat
        Marketplace](3D%22https://docs.redhat.com/en/documentation/openshif=){.3D\"link
        s="ub-chapter-title\"" t_container_platform="" 4.10="" html=""
        building_applications="" red-hat-marketplace\"=""
        i="d=3D\"sub-link-to-building_applications-red-hat-marketplace\""
        v-c61ac788="=3D\"\""}

    =
2.  Serverless\<= /summary\>
    1.  [About Serverl=
        ess](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"su=
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" serverless=""
        about-serverless-1\"=""
        b-link-to-serverless-about-serverless-1\"=""
        v-c61ac788="3D\"\""}
3.  CI/CD
    1.  [CI/CD](3D%22https://docs.redhat.com/en/documentation/openshift_container=){#3D\"chapter-landing--cicd-index\"
        .3D\"link sub-chapter-title="" chapter-landing="-page\""
        _platform="" 4.10="" html="" cicd="" index\"=""
        v-c="61ac788=3D\"\""}
    2.  [= OpenShift Container Platform CI/CD
        overview](3D%22https://doc=){#3D\"sub-link-to-cicd-ci-cd-overview\"
        .3D\"link sub-chapter-title\"="" s.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        cicd="" c="i-cd-overview\"" v-c61ac788="3D\"\""}
    3.  [Builds](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"sub-link-to-cicd-builds\"
        .3D\"link sub-chapter-t="itle\"" platform="" 4.10="" html=""
        cicd="" builds\"="" v-c61ac="788=3D\"\""}
    4.  Migrating from Jenkins to Tekton
    5.  \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/cicd/pipelines\"
        id=3D\"sub-l= ink-to-cicd-pipelines\"
        data-v-c61ac788=3D\"\"\>Pipelines
    6.  [GitOps](3D%22https://docs.redhat.com/en/documentation/openshift_=){#3D\"sub-link-to-cicd-gitops\"
        .3D\"link sub="-chapter-title\"" container_platform="" 4.10=""
        html="" cicd="" gitops\"="" da="ta-v-c61ac788=3D\"\""}
4.  Images
    1.  [Images](3D%22https://docs.redhat.com/en/documentation/openshi=){#3D\"chapter-landing--images=
        .3D\"link sub-chapter-title="" cha="pter-landing-page\""
        ft_container_platform="" 4.10="" html="" images="" index\"=""
        -index\"="" v-c61ac788="3D\"\""}
    2.  [Overview of images]{#3D\"sub-link-to-images-overview-of-=
        .3D\"link sub-chapter-title\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" images="" overview-of-images\"="" images\"=""
        v-c61ac788="3D\"\""}
    3.  [Using the Cluster Samples Operato= r with an alternate
        registry](3D%22htt=){#3D\"sub-link-to-images-samples-op=
        .3D\"link sub-chapter-title\"="" ps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        htm="l/images/samples-operator-alt-registry\""
        erator-alt-registry\"="" v-c61ac788="3D\"\""}
    4.  [Creating
        images](3D%22h=){#3D\"sub-link-to-images-creating-images\"
        .3D\"link sub-chapter-title\"="" ttps:="" docs.redhat.com=""
        en="" documentation="" openshift_container_platform="" 4.10=""
        h="tml/images/creating-images\"" ="v-c61ac788=3D\"\""}
    5.  [Managing
        images](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-images-managing-images\"
        .3D\"link sub-chapter-title\"="" .10="" html="" images=""
        managing-images\"="" =="" v-c61ac788="3D\"\""}
    6.  [Managing image streams]{#3D\"sub-link-to-images-managin=
        .3D\"link sub-chapter-title\"=""
        h="ref=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfor="
        m="" 4.10="" html="" images="" managing-image-streams\"=""
        g-image-streams\"="" v-c61ac788="3D\"\""}
    7.  [Using image streams with Kubernetes
        resources](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"sub-link-to-images-using-imagestreams-with-kube-resources\"
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" images=""
        using-imagestreams-with-kube-res="ources\""
        da="ta-v-c61ac788=3D\"\""}
    8.  Triggering updates on image stream changes
    9.  \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/images/image-configuration\"=
        id=3D\"sub-link-to-images-image-configuration\"
        data-v-c61ac788=3D\"\"\>Image c= onfiguration resources
    10. [Using
        templates](3D%22https:/=){#3D\"sub-link-to-images-using-templates\"
        .3D\"link sub-chapter-title\"="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        im="ages/using-templates\"" v-c61a="c788=3D\"\""}
    11. [Using Ruby on
        Rails](3D%22http=){#3D\"sub-link-to-images-templates-u=
        .3D\"link sub-chapter-title\"="" s:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        html="/images/templates-using-ruby-on-rails\""
        sing-ruby-on-rails\"="" v-c61ac788="3D\"\""}
    12. [Using
        images](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"sub-link-to-=
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" images=""
        using-images\"="" images-using-images\"="" v-c61ac788="3D\"\""}
5.  Nodes
    1.  [Nodes](3D%22https://docs.redhat.c=){#=3D\"chapter-landing--nodes-index\"
        .3D= \"link="" sub-chapter-title="" chapter-landing-page\"=""
        om="" en="" documentation="" openshift_container_platform=""
        4.10="" html="" nodes="" index\"="" v-c61ac788="3D\"\""}
    2.  [Overview of
        nodes](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"sub-link=
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" nodes=""
        overview-of-nodes\"="" -to-nodes-overview-of-nodes\"=""
        v-c61ac788="3D\"\""}
    3.  Working with pods\<= /a\>
    4.  [Automatically scaling pods with the Custom Metrics Auto= scaler
        Operator](3D%22https://docs.redhat.com/en/doc=){#3D\"sub-link-to-node=
        .3D\"link sub-chapter-title\"="" umentation=""
        openshift_container_platform="" 4.10="" html="" nodes=""
        automatically-scali="ng-pods-with-the-custom-metrics-autoscaler-operator\""
        s-automatically-scaling-pods-with-the-custom-metrics-autoscaler-operator\"=""
        d="ata-v-c61ac788=3D\"\""}
    5.  [Controllin= g pod placement onto nodes
        (scheduling)](3D%22https://docs.r=){#3D\"sub-link-to-nodes-contr=
        .3D\"link sub-chapter-title\"="" edhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        nodes="" con="trolling-pod-placement-onto-nodes-scheduling\""
        olling-pod-placement-onto-nodes-scheduling\"=""
        v-c61ac788="3D\"\""}
    6.  Using Jobs and DaemonSets
    7.  \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/nodes/working-with-nodes\"
        i= d=3D\"sub-link-to-nodes-working-with-nodes\"
        data-v-c61ac788=3D\"\"\>Working wit= h nodes
    8.  [Working with
        containers](3D%22https://docs.redhat.co=){#3D\"sub-link-to-nodes-working-with-containers\"
        .3D\"link sub-chapter-title\"="" m="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" nodes=""
        working-wit="h-containers\"" v-c61ac="788=3D\"\""}
    9.  [Working with
        clusters](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-nodes-working-with-=
        .3D\"link sub-chapter-title\"="" .10="" html="" nodes=""
        working-with-clusters\"="" clusters\"="" v-c61ac788="3D\"\""}
6.  Sandboxed Containers Support for OpenShift
    1.  [Sandboxed Containers Support for
        OpenShift](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"=
        .3D\"link sub-chapter-title="" chapter-landing-="page\""
        platform="" 4.10="" html=""
        sandboxed_containers_support_for_openshift="" index\"=""
        chapter-landing--sandboxed_containers_support_for_openshift-index\"=""
        v-c="61ac788=3D\"\""}
    2.  [{sandboxed-containers-first} {sandboxed-containers-version} re=
        lease
        notes](3D%22https://docs.redhat.com/en/documentation/openshif=){#3D\"sub-link-to-sandboxed_contain=
        .3D\"link t_container_platform="" 4.10="" html=""
        sandboxed_containers_support_for_openshift=""
        s="andboxed-containers-4-10-release-notes\""
        ers_support_for_openshift-sandboxed-containers-4-10-release-notes\"=""
        v-c="61ac788=3D\"\""}
    3.  [Understanding OpenShift sandboxed contain=
        ers](3D%22https://docs.redha=){#3D\"sub= .3D\"link
        sub-chapter-title\"="" t.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        sandboxed_con="tainers_support_for_openshift/understanding-sandboxed-containers\""
        -link-to-sandboxed_containers_support_for_openshift-understanding-sandboxed="-containers\""
        v-c61ac788="3D\"\""}
    4.  [Deploying OpenShift sandboxed contai= ners
        workloads](3D%22https://docs.redhat.com/e=){#3D\"sub-= .3D\"link
        sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        sandboxed_containers="_support_for_openshift/deploying-sandboxed-containers-workloads\""
        link-to-sandboxed_containers_support_for_openshift-deploying-sandboxed-cont="ainers-workloads\""
        v-c61ac788="3D\"\""}
    5.  Monitoring OpenShift sandboxed containers
    6.  \<= a class=3D\"link sub-chapter-title\"
        href=3D\"https://docs.redhat.com/en/docum=
        entation/openshift_container_platform/4.10/html/sandboxed_containers_suppor=
        t_for_openshift/uninstalling-sandboxed-containers\"
        id=3D\"sub-link-to-sandbo=
        xed_containers_support_for_openshift-uninstalling-sandboxed-containers\"
        dat= a-v-c61ac788=3D\"\"\>Uninstalling OpenShift sandboxed
        containers
    7.  [Upgrading OpenShift sandboxed
        containers](3D%22https://docs.redhat.com/en/documentation/op=){#3D\"sub-link-to-sandboxed_containers=
        .3D\"= link="" sub-chapter-title\"=""
        enshift_container_platform="" 4.10="" html=""
        sandboxed_containers_support_for_opens="hift/upgrading-sandboxed-containers\""
        _support_for_openshift-upgrading-sandboxed-containers\"=""
        v-c61ac788="3D\"\"="}
    8.  [Collect= ing OpenShift sandboxed containers
        data](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link-to-sandboxed_containers_support_for_o=
        .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
        sandboxed_containers_support_for_openshift=""
        troubleshooting="-sandboxed-containers\""
        penshift-troubleshooting-sandboxed-containers\"=""
        v-c61ac788="3D\"\""}
7.  Operato= rs
    1.  [Operators](3D%22https://docs.redhat.com/en/docum=){#3D\"chap=
        .3D\"link sub-c="hapter-title" chapter-landing-page\"=""
        entation="" openshift_container_platform="" 4.10="" html=""
        operators="" index\"="" ter-landing--operators-index\"=""
        v-c61ac788="3D\"\""}
    2.  [Operators overv=
        iew](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"sub=
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html="" operators=""
        operators-overview\"=""
        -link-to-operators-operators-overview\"="" v-c61ac788="3D\"\""}
    3.  [Understanding
        Operators](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-operators-understanding-operators\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" operators=""
        understand="ing-operators\"" v-="c61ac788=3D\"\""}
    4.  [User tasks]{#3D\"sub-link-to-operators-user-tasks\" .3D\"link
        sub-chapter-title\"="href=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfo="
        rm="" 4.10="" html="" operators="" user-tasks\"="" ==""
        v-c61ac788="3D\"\""}
    5.  [Administrator
        tasks](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-operators-adminis=
        .3D\"link sub-chapter-title\"="" .10="" html="" operators=""
        administrator-tasks\"="" trator-tasks\"="" v-c61ac788="3D\"\""}
    6.  [Developing Operat=
        ors](3D%22https://docs.redhat.com/en/documentation/openshift=){#3D\"sub-lin=
        .3D\"link su="b-chapter-title\"" _container_platform="" 4.10=""
        html="" operators="" developing-operators\"=""
        k-to-operators-developing-operators\"="" v-c61ac788="3D\"\""}
    7.  [Cluster Operators
        reference](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-operators-cluster-operators-ref\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" operators=""
        cluster-op="erators-ref\"" v-c61a="c788=3D\"\""}
8.  =
    Specializ= ed hardware and driver enablement
    1.  [= Specialized hardware and driver
        enablement](3D=){#3D\"chapter-landi= .3D\"link
        sub-chapter-title="" chapter-landing-page\"="" \"https:=""
        docs.redhat.com="" en="" documentation=""
        openshift_container_platform=""
        4.10="/html/specialized_hardware_and_driver_enablement/index\""
        ng--specialized_hardware_and_driver_enablement-index\"=""
        v-c61ac788="3D\"\""}
    2.  [About specialized hardware a= nd driver
        enablement](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){#3D\"sub-link-to-specialized_hardware_and_driver_enablement-a=
        .3D\"link sub-chapter-ti="tle\"" latform="" 4.10="" html=""
        specialized_hardware_and_driver_enablement=""
        about-hardware="-enablement\"" bout-hardware-enablement\"=""
        v-c61ac788="3D\"\""}
    3.  [Driver Toolkit](3D%22https://d=){#3D\"sub-link-to-sp= .3D\"link
        sub-chapter-title\"="" ocs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        spec="ialized_hardware_and_driver_enablement/driver-toolkit\""
        ecialized_hardware_and_driver_enablement-driver-toolkit\"=""
        v-c61ac788="3D=" \"\"=""}
    4.  [Special Resource Operator](3D%22https://docs=){#3D\"sub-li=
        .3D\"link sub-chapter-title\"="" .redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        special="ized_hardware_and_driver_enablement/special-resource-operator\""
        nk-to-specialized_hardware_and_driver_enablement-special-resource-operator\"="data-v-c61ac788=3D\"\""}

\<= details id=3D\"toc\--undefined\" data-v-2b26994c=3D\"\"\>

Monitor

1.  1.  [Logging](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){#3D\"chapter-landing--logging-index\"
        .3D\"link sub-chapter-title="" chapter-landing-p="age\""
        latform="" 4.10="" html="" logging="" index\"=""
        data="-v-c61ac788=3D\"\""}
    2.  [Release notes for
        Logging](3D%22https=){#3D\"sub-link-to-logging-release-notes\"
        .3D\"link sub-chapter-title\"="" :="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        =="" logging="" release-notes\"="" v-c61a="c788=3D\"\""}
    3.  [Support]{#3D\"sub-link-to-logging-support\" .3D\"link
        sub-chapter-title\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" logging="" support\"="" v-c61ac="788=3D\"\""}
    4.  [Lo= gging
        5.6](3D%22https://docs.=){#3D\"sub-link-to-logging-logging-5-6\"
        .3D\"link sub-chapter-title\"="" redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        logging="" =="" logging-5-6\"="" v-c61ac788="3D\"\""}
    5.  [Logging 5=
        .5](3D%22https://docs.redhat.=){#3D\"sub-link-to-logging-logging-5-5\"
        .3D\"link sub-chapter-title\"="" com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" logging="-5-5\""
        v-c61ac788="3D\"\""}
    6.  [Unders= tanding the logging subsystem for Red Hat
        OpenShift](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-logging-cluster-logging\"
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        cluster-logg="ing\"" v-c61ac788="3D\"\""}
    7.  [Conf= iguring your Logging
        deployment](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-lin=
        .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
        logging="" configuring-your-logging-deployment\"=""
        k-to-logging-configuring-your-logging-deployment\"=""
        v-c61ac788="3D\"\""}
    8.  [Logging using
        LokiStack](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-logging-cluster-lo=
        .3D\"link sub-chapter-title\"="" .10="" html="" logging=""
        cluster-logging-loki\"="" gging-loki\"="" v-c61ac788="3D\"\""}
    9.  [Viewing logs for a =
        resource](3D%22https://docs.redhat.com/en/documentation/openshi=){#3D\"sub-lin=
        .3D\"link =="" sub-chapter-title\"="" ft_container_platform=""
        4.10="" html="" logging="" vewing-resource-logs\"=""
        k-to-logging-vewing-resource-logs\"="" v-c61ac788="3D\"\""}
    10. [Viewing cluster logs by using
        Kibana](3D%22https://docs.redhat.c=){#3D\"sub-link-to-logging-cluster-logging-visuali=
        .3D\"link sub-chapter-title\"="" om="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        cluster-="logging-visualizer-using\"" zer-using\"=""
        v-c61ac788="3D\"\""}
    11. [Forwarding logs to external third-party logging
        systems](3D%22https://docs.redhat.com/en/documenta=){#3D\"sub-link-to-logging-cluster-logging-external\"
        cl="ass=3D\"link" sub-chapter-title\"="" tion=""
        openshift_container_platform="" 4.10="" html="" logging=""
        cluster-logging-externa="l\"" v-c61ac788="3D\"\"="}
    12. [Enabling JSON
        logging](3D%22https://docs.redhat.com/en/documentation/openshi=){#3D\"sub-link-to-logging-cluster-logging-enabling-json-logging\"
        .3D\"link =="" sub-chapter-title\"="" ft_container_platform=""
        4.10="" html="" logging=""
        cluster-logging-enabling-json-loggi="ng\"" v="-c61ac788=3D\"\""}
    13. [Collecting and storing Ku= bernetes
        events]{#3D\"sub-link-to-logging-= .3D\"link
        sub-chapter-title\"=""
        h="ref=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfor="
        m="" 4.10="" html="" logging="" cluster-logging-eventrouter\"=""
        v-c61ac788="3D\"\""}
    14. [Updating OpenShift
        Logging](3D%22https://docs.r=){#3D\"sub-link-to-logging-cluster-logging-upgradi=
        .3D\"link sub-chapter-title\"="" edhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        logging="" c="luster-logging-upgrading\"" ng\"=""
        v-c61ac788="3D\"\""}
    15. [Troubleshooting
        Logging](3D%22https://docs.re=){#3D\"sub-link-to-logging-troubleshooting-logging\"
        .3D\"link sub-chapter-title\"="" dhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        logging="" tr="oubleshooting-logging\""
        d="ata-v-c61ac788=3D\"\""}
    16. [Uninstalling OpenShift=
        Logging](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){#3D\"sub-link-to-log=
        .3D\"link sub-chapter-t="itle\"" platform="" 4.10="" html=""
        logging="" cluster-logging-uninstall\"=""
        ging-cluster-logging-uninstall\"="" v-c61ac788="3D\"\""}
    17. [Log Record
        Fields](3D%22https://docs.redhat.c=){#3D\"sub-link-to-logging-cluster-logging-exported=
        .3D\"link sub-chapter-title\"="" om="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        cluster-="logging-exported-fields\"" -fields\"=""
        v-c61ac788="3D\"\""}
    18. [structured](3D%22h=){#3D\"sub-link-to-logging-structured\"
        .3D\"link sub-chapter-title\"="" ttps:="" docs.redhat.com=""
        en="" documentation="" openshift_container_platform="" 4.10=""
        h="tml/logging/structured\"" v-c61ac7="88=3D\"\""}
    19. [\@tim=
        estamp](3D%22https://doc=){#3D\"sub-link-to-logging-timestamp\"
        .3D\"link sub-chapter-title\"="" s.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        loggin="g/timestamp\"" v-c61ac788="3D\"\""}
    20. [hostname](3D%22https://docs.redhat.com=){.3D\"link
        sub-chapter-title\"="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        hostname\"="id=3D\"sub-link-to-logging-hostname\""
        v-c61ac788="3D\"\""}
    21. [ipaddr4](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to=
        .=3D\"link sub-chapter-title\"="" n=""
        openshift_container_platform="" 4.10="" html="" logging=""
        ipaddr4\"="" -logging-ipaddr4\"="" v-c61ac788="3D\"\""}
    22. [ipaddr6](3D%22https://docs.redhat.com/en/documentation/openshift_contain=){#3D\"sub-link-to-logging-ipaddr6\"
        .3D\"link sub-chapte="r-title\"" er_platform="" 4.10="" html=""
        logging="" ipaddr6\"="" d="ata-v-c61ac788=3D\"\""}
    23. [lev= el](3D%22ht=){#3D\"sub-link-to-logging-level\" .3D\"link
        sub-chapter-title\"="" tps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        ht="ml/logging/level\"" v-c61ac788="3D\"\""}
    24. [pid](3D%22https://docs.redhat.com/e=){#3D\"s= .3D\"link
        sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        pid\"="" ub-link-to-logging-pid\"="" v-c61ac788="3D\"\""}
    25. [tag= s](3D%22=){#3D\"sub-link-to-logging-tags\" .3D\"link
        sub-chapter-title\"="" https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" ==""
        html="" logging="" tags\"="" v-c61ac788="3D\"\""}
    26. [file](3D%22https://docs.redhat.com/en/d=){#3D\"sub= .3D\"link
        sub-chapter-title\"="" ocumentation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        file\"="" -link-to-logging-file\"="" v-c61ac788="3D\"\""}
    27. [kubernetes](3D%22htt=){#3D\"sub-link-to-logging-cluster-logging-exported-fields-kubern=
        .3D\"link sub-chapter-title\"="" ps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        htm="l/logging/cluster-logging-exported-fields-kubernetes_cluster-logging-export="
        ed-fields\"="" etes_cluster-logging-exported-fields\"=""
        v-c61ac788="3D\"\""}
    28. [OpenShift](3D%22https://docs.redhat.com/en/document=){#3D\"sub-l=
        c="lass=3D\"link" sub-chapter-title\"="" ation=""
        openshift_container_platform="" 4.10="" html="" logging=""
        openshift\"="" ink-to-logging-openshift\"=""
        v-c61ac788="3D\"\""}

2.  Monitoring
    1.  [Moni=
        toring](3D%22https://docs.r=){#3D\"chapter-landing--monitoring-index\"
        c="lass=3D\"link" sub-chapter-title="" chapter-landing-page\"=""
        edhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        monitorin="g/index\"" v-c61ac788="3D\"\""}
    2.  [Monitoring
        overview](3D%22https://docs.redhat.com=){#3D\"sub-link-to-monitoring-monitoring-overview\"
        .3D\"link sub-chapter-title\"="" en="" documentation=""
        openshift_container_platform="" 4.10="" html="" monitoring=""
        monitor="ing-overview\"" v-c61a="c788=3D\"\""}
    3.  [Configuring the = monitoring
        stack](3D%22=){#3D\"sub-link-to-monitor= .3D\"link
        sub-chapter-title\"="" https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" ==""
        html="" monitoring="" configuring-the-monitoring-stack\"=""
        ing-configuring-the-monitoring-stack\"="" v-c61ac788="3D\"\""}
    4.  [Configuring = external alertmanager
        instances](3D%22https://docs.=){#3D\"sub-link-to-monitoring-monitoring-configuring-external-alertm=
        .3D\"link sub-chapter-title\"="" redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" html=""
        monitori="ng/monitoring-configuring-external-alertmanagers_configuring-the-monitoring="
        -stack\"="" anagers_configuring-the-monitoring-stack\"=""
        v-c61ac788="3D\"\""}
    5.  [Setting audit log levels for the Prometheus
        Adapter](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-monitoring-setting-audit-l=
        .3D\"link sub-chapter-title\"="" .10="" html="" monitoring=""
        setting-audit-log-levels-for-the-prometheus-adapter_con="figuring-the-monitoring-stack\""
        og-levels-for-the-prometheus-adapter_configuring-the-monitoring-stack\"=""
        data="-v-c61ac788=3D\"\""}
    6.  [Enabling monitoring for us= er-defined
        projects](3D%22https://docs.redhat.com/en/documenta=){#3D\"sub-link-to-monitoring-enabling-monitoring=
        cl="ass=3D\"link" sub-chapter-title\"="" tion=""
        openshift_container_platform="" 4.10="" html="" monitoring=""
        enabling-monitoring-="for-user-defined-projects\""
        -for-user-defined-projects\"="" v-c61ac788="3D\"\""}
    7.  [Enabling alert routing for user-defined
        projects](3D%22https://do=){#3D\"sub-link-to-m= .3D\"link
        sub-chapter-title\"="" cs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        monit="oring/enabling-alert-routing-for-user-defined-projects\""
        onitoring-enabling-alert-routing-for-user-defined-projects\"=""
        v-c61ac788="=3D\"\""}
    8.  [Managing
        metrics](3D%22https://docs.redhat.com/en/documentation/openshift=){#3D\"sub-link-t=
        .3D\"link su="b-chapter-title\"" _container_platform="" 4.10=""
        html="" monitoring="" managing-metrics\"=""
        o-monitoring-managing-metrics\"="" v-c61ac788="3D\"\""}
    9.  [Managing metrics
        targets](3D%22https://docs.redhat.com/en/documenta=){#3D\"sub-link-to-monitoring-managing-metrics-targets\"
        cl="ass=3D\"link" sub-chapter-title\"="" tion=""
        openshift_container_platform="" 4.10="" html="" monitoring=""
        managing-metrics-tar="gets\"" v-c61ac78="8=3D\"\""}
    10. [Managing
        alerts](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-monitoring-managing-=
        .3D\"link sub-chapter-title\"="" .10="" html="" monitoring=""
        managing-alerts\"="" alerts\"="" v-c61ac788="3D\"\""}
    11. [Rev= iewing monitoring
        dashboards](3D%22https://docs.redhat.com/en/documentation/openshift_container=){#3D\"sub-l=
        .3D\"link sub-chapter-="title\"" _platform="" 4.10="" html=""
        monitoring="" reviewing-monitoring-dashboards\"=""
        ink-to-monitoring-reviewing-monitoring-dashboards\"=""
        v-c61ac788="3D\"\""}
    12. Monitoring bare-metal events with the Bare Metal Event Relay\<=
        /a\>
    13. [Accessing third-part= y monitoring UIs and
        APIs](3D%22https://docs.redhat.com/en/doc=){#3D\"sub-link-to-monitoring-accessing-thi=
        .3D\"link sub-chapter-title\"="" umentation=""
        openshift_container_platform="" 4.10="" html="" monitoring=""
        accessing-thir="d-party-monitoring-uis-and-apis\""
        rd-party-monitoring-uis-and-apis\"="" v-c61ac788="3D\"\""}
    14. [Troubleshooting mo= nitoring
        issues](3D%22http=){#3D\"sub-link-to-monitoring= .3D\"link
        sub-chapter-title\"="" s:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        html="/monitoring/troubleshooting-monitoring-issues\""
        -troubleshooting-monitoring-issues\"="" v-c61ac788="3D\"\""}
    15. [ConfigMap reference for Cluster Monitoring
        Operator](3D%22https://docs.r=){#3D\"sub-link-to-mo= .3D\"link
        sub-chapter-title\"="" edhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        monitorin="g/configmap-reference-for-cluster-monitoring-operator\""
        nitoring-configmap-reference-for-cluster-monitoring-operator\"=""
        v-c61ac7="88=3D\"\""}

3.  Scalability and performance
    1.  [Scalability and performan= ce]{#3D\"chapter-landing--scalab=
        .3D\"link sub-chapter-title="" chapter-landing-page\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" scalability_and_performance="" index\"=""
        ility_and_performance-index\"="" v-c61ac788="3D\"\""}
    2.  [Recommended host pr=
        actices](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-scalability_and_perfo=
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        scalability_and_perf="ormance/recommended-host-practices\""
        rmance-recommended-host-practices\"="" v-c61ac788="3D\"\""}
    3.  [Reco= mmended host practices for IBM Z & LinuxONE
        environments](3D%22https://docs.redhat.co=){#3D\"sub-link-to-scalability_=
        .3D\"link sub-chapter-title\"="" m="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        scalability_and_p="erformance/ibm-z-recommended-host-practices\""
        and_performance-ibm-z-recommended-host-practices\"=""
        v-c61ac788="3D\"\""}
    4.  [Recommended clus= ter scaling
        practices](3D%22https://docs.redhat.com/en/documentation/ope=){#3D\"sub-link-to-scalability_and_performance-r=
        .3D\"l= ink="" sub-chapter-title\"=""
        nshift_container_platform="" 4.10="" html=""
        scalability_and_performance=""
        recommended="-cluster-scaling-practices\""
        ecommended-cluster-scaling-practices\"="" v-c61ac788="3D\"\""}
    5.  [Us= ing the Node Tuning
        Operator](3D%22https://=){#3D\"sub-link-to-scal= .3D\"link
        sub-chapter-title\"="" docs.redhat.com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        sca="lability_and_performance/using-node-tuning-operator\""
        ability_and_performance-using-node-tuning-operator\"=""
        v-c61ac788="3D\"\""}
    6.  [Using CPU Man= ager and Topology
        Manager](3D%22h=){#3D\"sub-link-to-scalab= .3D\"link
        sub-chapter-title\"="" ttps:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        h="tml/scalability_and_performance/using-cpu-manager\""
        ility_and_performance-using-cpu-manager\"=""
        v-c61ac788="3D\"\""}
    7.  [= Scheduling NUMA-aware
        workloads](3D%22http=){#3D\"sub-link-to-s= .3D\"link
        sub-chapter-title\"="" s:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10=""
        html="/scalability_and_performance/cnf-numa-aware-scheduling\""
        calability_and_performance-cnf-numa-aware-scheduling\"=""
        v-c61ac788="3D\"\""}
    8.  [Scaling the Cluster Monitoring
        Operator](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){.3D\"link
        sub-chapter-title\"="" .10="" html=""
        scalability_and_performance=""
        scaling-cluster-monitoring-operator\"=""
        i="d=3D\"sub-link-to-scalability_and_performance-scaling-cluster-monitoring-ope="
        rator\"="" v-c61ac788="3D\"\""}
    9.  [Planning your environment according to object maxi=
        mums](3D%22https://docs.redhat.com/en/documentat=){#3D\"sub-link-to-scala=
        cla="ss=3D\"link" sub-chapter-title\"="" ion=""
        openshift_container_platform="" 4.10="" html=""
        scalability_and_performance=""
        plan="ning-your-environment-according-to-object-maximums\""
        bility_and_performance-planning-your-environment-according-to-object-maximu="ms\""
        v-c61ac788="3D\"\""}
    10. [Optimizing
        storage](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-scalability_and_performance-o=
        .3D\"link sub-chapter-title\"="" n="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        scalability_and_perf="ormance/optimizing-storage\""
        ptimizing-storage\"="" v-c61ac788="3D\"\""}
    11. [Optimizing
        routing](3D%22https://docs.redhat.com/en/documentation/opens=){#3D\"sub-link-to-scalability_and_performance-routing-optimization=
        .3D\"lin= k="" sub-chapter-title\"="" hift_container_platform=""
        4.10="" html="" scalability_and_performance=""
        routing-optim="ization\"" \"="" v-c61ac788="3D\"\""}
    12. [Optimizing
        networking](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"s=
        .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
        scalability_and_performance="" optimizing-networking\"=""
        ub-link-to-scalability_and_performance-optimizing-networking\"=""
        v-c61ac7="88=3D\"\""}
    13. [Managing bare metal hosts](3D%22=){#3D\"sub-link-= .3D\"link
        sub-chapter-title\"="" https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform="" 4.10="" ==""
        html="" scalability_and_performance=""
        managing-bare-metal-hosts\"=""
        to-scalability_and_performance-managing-bare-metal-hosts\"=""
        v-c61ac788="=3D\"\""}
    14. [What huge pages do and how th= ey are consumed by
        applications](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-scalability_and_performance-what-huge-pages-do-an=
        .3D\"link sub-chapter-title\"="" .10="" html=""
        scalability_and_performance=""
        what-huge-pages-do-and-how-they-are-co="nsumed\""
        d-how-they-are-consumed\"="" v-c61ac788="3D\"\""}
    15. [Performance A= ddon Operator for low latency
        nodes](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-scalability_and_performance-cnf-performan=
        .3D\"link sub-chapter-title\"="" .10="" html=""
        scalability_and_performance=""
        cnf-performance-addon-operator-for-low="-latency-nodes\""
        ce-addon-operator-for-low-latency-nodes\"=""
        v-c61ac788="3D\"\""}
    16. [Performing late= ncy tests for platform
        verification]{#3D\"sub-link-to-scalability_and_performance-cnf-performin=
        .3D\"link sub-chapter-title\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" scalability_and_performance=""
        cnf-performing-platform-verification="-latency-tests\""
        g-platform-verification-latency-tests\"="" v-c61ac788="3D\"\""}
    17. [Topology Aware Lifecycle Manager for cluster updates]{#3D\"=
        .3D\"link sub-chapter-title\"=""
        hr="ef=3D\"https://docs.redhat.com/en/documentation/openshift_container_platform="
        4.10="" html="" scalability_and_performance=""
        cnf-talm-for-cluster-updates\"=""
        sub-link-to-scalability_and_performance-cnf-talm-for-cluster-updates\"=""
        ="v-c61ac788=3D\"\""}
    18. [Creating a performan= ce
        profile](3D%22https://docs.redhat.com/en/documenta=){#3D\"sub-link-to-scalability_and_performance=
        cl="ass=3D\"link" sub-chapter-title\"="" tion=""
        openshift_container_platform="" 4.10="" html=""
        scalability_and_performance=""
        cnf="-create-performance-profiles\""
        -cnf-create-performance-profiles\"="" v-c61ac788="3D\"\""}
    19. [Workload partiti= oning on single-node
        OpenShift](3D%22https://docs.redhat=){#3D\"sub-link-to-scalability_and_performance-sno-du-enabling-workload-p=
        .3D\"link sub-chapter-title\"="" .com="" en="" documentation=""
        openshift_container_platform="" 4.10="" html=""
        scalability_an="d_performance/sno-du-enabling-workload-partitioning-on-single-node-openshif="
        t\"="" artitioning-on-single-node-openshift\"=""
        v-c61ac788="3D\"\""}
    20. [Clusters at the network far edge](3D=){#3D\"s= .3D\"link
        sub-chapter-title\"="" \"https:="" docs.redhat.com="" en=""
        documentation="" openshift_container_platform=""
        4.10="/html/scalability_and_performance/clusters-at-the-network-far-edge\""
        ub-link-to-scalability_and_performance-clusters-at-the-network-far-edge\"=""
        da="ta-v-c61ac788=3D\"\""}
    21. Support
        1.  [Support](3D%22https://docs.redhat.c=){.3D= \"link=""
            sub-chapter-title="" chapter-landing-page\"="" om="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html="" support="" index\"=""
            i="d=3D\"chapter-landing--support-index\""
            v-c61ac788="3D\"\""}
        2.  Support overview
        3.  = [Managing your cluster
            resources](3D%22https://docs.redhat.com/en/docu=){#3D\"sub-link-to-support-managing-cluster-resources\"
            .3D\"link sub-chapter-title\"="" mentation=""
            openshift_container_platform="" 4.10="" html="" support=""
            managing-cluster-r="esources\"" v-c61a="c788=3D\"\""}
        4.  [Getting
            support](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link-to-support-getting=
            .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
            support="" getting-support\"="" -support\"=""
            v-c61ac788="3D\"\""}
        5.  [Remote health monitoring with connected
            clusters=](3D%22https://docs.redhat.com/en/documentation/openshift_contain=){#3D\"sub-link-to-support-remote-health-monitoring-with-connected-clus=
            .3D\"link sub-chapte="r-title\"" er_platform="" 4.10=""
            html="" support=""
            remote-health-monitoring-with-connected-clust="ers\""
            ters\"="" v-c61ac788="3D\"\""}
        6.  [Gathering data about your
            cluster](3D%22https://docs.redhat.com/en/do=){#3D\"sub-link-to-support-gathering-cluster-data\"
            .3D\"link sub-chapter-title\"="" cumentation=""
            openshift_container_platform="" 4.10="" html="" support=""
            gathering-cluste="r-data\"" v-c61ac788="=3D\"\""}
        7.  [Summar= izing cluster
            specifications](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link=
            .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
            support="" summarizing-cluster-specifications\"=""
            -to-support-summarizing-cluster-specifications\"=""
            v-c61ac788="3D\"\""}
        8.  [Troubleshooting](3D%22h=){#3D\"sub-link-to-support-troubleshooting\"
            .3D\"link sub-chapter-title\"="" ttps:="" docs.redhat.com=""
            en="" documentation="" openshift_container_platform=""
            4.10="" h="tml/support/troubleshooting\""
            dat="a-v-c61ac788=3D\"\""}

4.  Integration
    1.  Virtualization
        1.  [Virtualization](3D%22https://docs.redhat.com/en/documentati=){#3D\"chapt=
            .3D\"link sub-chapter="-title" chapter-landing-page\"=""
            on="" openshift_container_platform="" 4.10="" html=""
            virtualization="" index\"=""
            er-landing--virtualization-index\"="" v-c61ac788="3D\"\""}
        2.  [About OpenS= hift
            Virtualization](3D%22https://docs.redhat.com/en/document=){#=3D\"sub-link-to-virtualization-about-virt\"
            c="lass=3D\"link" sub-chapter-title\"="" ation=""
            openshift_container_platform="" 4.10="" html=""
            virtualization="" about-virt\"="" v-c61ac788="3D\"\""}
        3.  [Getting started with OpenShift
            Virtualization](3D%22https://do=){#3D\"sub-link-to-=
            .3D\"link sub-chapter-title\"="" cs.redhat.com="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html=""
            virtu="alization/getting-started-with-openshift-virtualization\""
            virtualization-getting-started-with-openshift-virtualization\"=""
            v-c61ac7="88=3D\"\""}
        4.  [Op= enShift Virtualization release
            notes](3D%22https://docs.redhat.com/en/documentation/openshift_=){#3D\"=
            .3D\"link sub="-chapter-title\"" container_platform=""
            4.10="" html="" virtualization=""
            virt-4-10-release-notes\"=""
            sub-link-to-virtualization-virt-4-10-release-notes\"=""
            v-c61ac788="3D\"\""}
        5.  [Installing]{#3D\"sub-link-to-virtualization-ins= .3D\"link
            sub-chapter-title\"=""
            h="ref=3D\"https://docs.redhat.com/en/documentation/openshift_container_platfor="
            m="" 4.10="" html="" virtualization="" installing\"=""
            talling\"="" v-c61ac788="3D\"\""}
        6.  [Updating OpenShift
            Virtualization](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"su=
            .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
            virtualization="" updating-openshift-virtualization\"=""
            b-link-to-virtualization-updating-openshift-virtualization\"=""
            v-c61ac788="=3D\"\""}
        7.  [Additional securi= ty privileges granted for
            kubevirt-controller and
            virt-launcher](3D%22https://docs.redhat.com/en/documentation/openshift_container_pl=){#3D\"sub-link-to-virtualization-virt-additional-security=
            .3D\"link sub-chapter-tit="le\"" atform="" 4.10="" html=""
            virtualization=""
            virt-additional-security-privileges-control="ler-and-launcher\""
            -privileges-controller-and-launcher\"=""
            v-c61ac788="3D\"\""}
        8.  [Using the CLI
            tools](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-virtualization-virt-using-the-cli-tools\"
            .=3D\"link sub-chapter-title\"="" n=""
            openshift_container_platform="" 4.10="" html=""
            virtualization="" virt-using-the-cli-="tools\""
            v-c6="1ac788=3D\"\""}
        9.  [Virtual
            machines](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-virtualization-=
            .3D\"link sub-chapter-title\"="" .10="" html=""
            virtualization="" virtual-machines\"="" v-c61ac788="3D\"\""}
        10. [Virtual machine
            templates](3D%22https://docs.redhat.com/en/documentation/openshif=){#=3D\"sub-link-to-virtualization-virtual-machine-templates\"
            .3D\"link s="ub-chapter-title\"" t_container_platform=""
            4.10="" html="" virtualization=""
            virtual-machine-templates\"="" v-c61ac788="=3D\"\""}
        11. [Live
            migration](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){#3D\"sub-link-to-virtualization-li=
            .3D\"link sub-chapter-title\"="" .10="" html=""
            virtualization="" live-migration\"="" ve-migration\"=""
            v-c61ac788="3D\"\""}
        12. = Node networking
        13. [Logging, events, and monitor=
            ing](3D%22https://docs.r=){#3D\"sub-link-to-virtualization-loggi=
            .3D\"link sub-chapter-title\"="" edhat.com="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html="" virtualiz="ation/logging-events-and-monitoring\""
            ng-events-and-monitoring\"="" v-c61ac788="3D\"\""}
        14. [Backup and
            restore](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-virtualization-backup-and-restore\"
            .3D\"link sub-chapter-title\"="" n="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            virtualization="" backu="p-and-restore\""
            v-="c61ac788=3D\"\""}
    2.  Distributed tr= acing
        1.  [Distributed
            tracing](3D%22https://docs.redhat.com/en/=){#3D\"chapter-landing--distributed_tracing-index\"
            .3D\"link =="" sub-chapter-title=""
            chapter-landing-page\"="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            distributed_tracing="" in="dex\"" v-c61ac788="3D\"\"="}
        2.  [Distributed traci= ng release
            notes](3D%22https://d=){#3D\"sub-link-to-distributed_=
            .3D\"link sub-chapter-title\"="" ocs.redhat.com="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html="" dist="ributed_tracing/distr-tracing-release-notes\""
            tracing-distr-tracing-release-notes\"=""
            v-c61ac788="3D\"\""}
        3.  [Distributed= tracing
            architecture](3D%22https://docs.=){#3D\"sub-link-to-distributed=
            .3D\"link sub-chapter-title\"="" redhat.com="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html=""
            distribu="ted_tracing/distributed-tracing-architecture\""
            _tracing-distributed-tracing-architecture\"=""
            v-c61ac788="3D\"\""}
        4.  [Distri= buted tracing
            installation](3D%22https://=){#3D\"sub-link-to-distri=
            .3D\"link sub-chapter-title\"="" docs.redhat.com="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html=""
            dis="tributed_tracing/distributed-tracing-installation\""
            buted_tracing-distributed-tracing-installation\"=""
            v-c61ac788="3D\"\""}
    3.  Service Mesh
        1.  [Service
            Mesh](3D%22https://docs.redhat.com/en/documentation/o=){#3D\"chapter-lan=
            .3D\"link sub-chapter-tit="le" chapter-landing-page\"=""
            penshift_container_platform="" 4.10="" html=""
            service_mesh="" index\"="" ding--service_mesh-index\"=""
            v-c61ac788="3D\"\""}
        2.  [Service Mesh 2=
            .x](3D%22https://docs.redhat.com/en/documentation/open=){#3D\"sub=
            .3D\"li= nk="" sub-chapter-title\"=""
            shift_container_platform="" 4.10="" html="" service_mesh=""
            service-mesh-2-x\"=""
            -link-to-service_mesh-service-mesh-2-x\"=""
            v-c61ac788="3D\"\""}
        3.  [Service Mesh
            1.x](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-service_mesh-service-mesh-1-x\"
            .3D\"link sub-chapter-title\"="" n="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            service_mesh="" service="-mesh-1-x\"" v-c61ac788="=3D\"\""}
    4.  Windows Container Suppor= t for OpenShift
        1.  [Windows Container Support= for
            OpenShift](3D%22https://docs.redha=){#3D\"chapter-landing--windows_container_=
            .=3D\"link sub-chapter-title="" chapter-landing-page\"=""
            t.com="" en="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            windows_conta="iner_support_for_openshift/index\""
            support_for_openshift-index\"="" v-c61ac788="3D\"\""}
        2.  Red Hat OpenShift support for Windows Containers overview
        3.  \<= a class=3D\"link sub-chapter-title\"
            href=3D\"https://docs.redhat.com/en/docum=
            entation/openshift_container_platform/4.10/html/windows_container_support_f=
            or_openshift/windows-containers-release-notes-5-x\"
            id=3D\"sub-link-to-window=
            s_container_support_for_openshift-windows-containers-release-notes-5-x\"
            dat= a-v-c61ac788=3D\"\"\>Red Hat OpenShift support for
            Windows Containers release = notes
        4.  [Understanding Windows container workloa=
            ds](3D%22https://docs.redhat.com/=){#3D\"sub-l= .3D\"link
            sub-chapter-title\"="" en="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            windows_container_s="upport_for_openshift/understanding-windows-container-workloads\""
            ink-to-windows_container_support_for_openshift-understanding-windows-contai="ner-workloads\""
            v-c61ac788="3D\"\""}
        5.  [Enabling Windows container
            workloads](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to=
            .3D\"link sub-chapter-title\"="" n="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            windows_container_su="pport_for_openshift/enabling-windows-container-workloads\""
            -windows_container_support_for_openshift-enabling-windows-container-workloa="ds\""
            v-c61ac788="3D\"\""}
        6.  [Creatin= g Windows machine
            sets](3D%22https://docs.redhat.com/en/documentation/op=){#3D\"sub-link-to-windows_container_suppor=
            .3D\"= link="" sub-chapter-title\"=""
            enshift_container_platform="" 4.10="" html=""
            windows_container_support_for_openshif="t/creating-windows-machine-sets\""
            t_for_openshift-creating-windows-machine-sets\"=""
            v-c61ac788="3D\"\""}
        7.  [Scheduling Windows container
            workloads](3D%22https:/=){#3D\"s= .3D\"link
            sub-chapter-title\"="" docs.redhat.com="" en=""
            documentation="" openshift_container_platform="" 4.10=""
            html=""
            wi="ndows_container_support_for_openshift/scheduling-windows-workloads\""
            ub-link-to-windows_container_support_for_openshift-scheduling-windows-workl="oads\""
            v-c61ac788="3D\"\""}
        8.  [Windows node upgrad=
            es](3D%22https://docs.redhat.com/en/documentatio=){#3D\"sub-link-to-windows_container_support_fo=
            .=3D\"link sub-chapter-title\"="" n=""
            openshift_container_platform="" 4.10="" html=""
            windows_container_support_for_open="shift/windows-node-upgrades\""
            r_openshift-windows-node-upgrades\"="" v-c61ac788="3D\"\""}
        9.  [Using= Bring-Your-Own-Host (BYOH) Windows instances as
            nodes](3D%22https://docs.redhat.com/e=){#3D\"sub-link-to-windows_contai=
            .3D\"link sub-chapter-title\"="" n="" documentation=""
            openshift_container_platform="" 4.10="" html=""
            windows_container_su="pport_for_openshift/byoh-windows-instance\""
            ner_support_for_openshift-byoh-windows-instance\"=""
            v-c61ac788="3D\"\""}
        10. [Removing Windows
            nodes](3D%22https://docs.redhat.com/en/documentation/openshift=){#3D\"sub-link-to-windows_container_support_for_openshif=
            .3D\"link su="b-chapter-title\"" _container_platform=""
            4.10="" html="" windows_container_support_for_openshift=""
            remov="ing-windows-nodes\"" t-removing-windows-nodes\"=""
            v-c61ac788="3D\"\""}
        11. [Disabling Windows container
            workloads](3D%22https://docs.redhat.com/en/document=){#3D\"sub-link-to-windows_=
            c="lass=3D\"link" sub-chapter-title\"="" ation=""
            openshift_container_platform="" 4.10="" html=""
            windows_container_support_for_="openshift/disabling-windows-container-workloads\""
            container_support_for_openshift-disabling-windows-container-workloads\"=""
            data="-v-c61ac788=3D\"\""}

5.  [Lega= l
    Notice](3D%22https://docs.red=){#3D\"chapter-landing--cicd-legal-notice\"
    .3D\"link\" hat.com="" en="" documentation=""
    openshift_container_platform="" 4.10="" html="" cicd=""
    legal-="notice\"" v-2b26994c="3D\"\""}
:::

::: {.=3D\"content span-12="" span-xs-12="" span-lg-10="" span-3xl-8\"="" v-c6b48c1e="3D\"\""}
=

FormatMulti-pageSingle-pageView full doc as PDF

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTE2IiAyNC43OTJjLS4zODQ9IjAtLjc2OC0uMTQ2LTEuMDYtLjQzOUwxLjI5MyIgMTAuNzA3YTEgMSAwIDEgMSAxLjQxNC0xLjQxNGwxNiAyMi41ODYgMjkuMjkzPSI5LjI5M2ExIiAxIDAgMSAxIDEuNDE0IDEuNDE0bDE3LjA2MSAyNC4zNTRhMS40OTQgMS40OTQgMCAwIDEtMS4wNi40Mzh6Ij48L3BhPT48L3N2Zz4=)
:::

Jump to section

::: {#3D\"details-content\"}
:::

::: {#3D\"left-column\"}
::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTMxLjQzMyIgMjcuNzUgMTc9Ii4yODgiIDMuMjVhMS41MDYgMS41MDYgMCAwIDAtMS4yOTgtLjc1aC0uMDAxYy0uNTMzIDAtMS4wMzEuMjg3LTEuMjk5Ljc0OXYuMDA9IjFMLjU0NCIgMjcuNzVhMS40OTcgMS40OTcgMCAwIDAgMCAxLjVjLjI2Ny40NjMuNzY1Ljc1IDEuMjk5Ljc1aDI4LjI5YTEuNTA0IDE9Ii41MDQiIDAgMCAwIDEuNS0xLjVjMC0uMjYtLjA2OC0uNTE5LS4yMDEtLjc1em0xNC43NSAxMWExLjI1IDEuMjUgMCAxIDEgMi41IDA9InY3YTEuMjUiIDEuMjUgMCAxIDEtMi41IDB2LTd6bTE2IDI2LjVhMS41IDEuNSAwIDEgMSAwLTMgMS41IDEuNSAwIDAgMSAwIDN6Ij49CjwvcGF0aD48L3N2Zz4=)
:::
:::

::: {#3D\"middle-column\"}
<div>

::: {#3D\"header\"}
:::

::: {#3D\"header-actions\"}
[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" microns="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iPTNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMCAyMCI+PHBhdGggZD0iM0QmcXVvdDtNMTcuOCIgMTYuMj0iMTEuNTkiIDEwbDYuMjEtNi4yMWMuNDItLjQ2LjM5LTEuMTctLjA3LTEuNTktLjQzLS40LTEuMDktLjQtMS41MiAwbC02LjIgNi4yPSItNi4yMi02LjE5Yy0uNDQtLjQ0LTEuMTUtLjQ0LTEuNTkiIDAtLjQ0LjQ0LS40NCAxLjE1IDAgMS41OWw2LjIgNi4yMS02LjIgNi4yPSJjLS40Mi40Ni0uMzkiIDEuMTcuMDcgMS41OS40My40IDEuMDkuNCAxLjUyIDBsMTAgMTEuNTlsNi4yIDYuMmMuNDQuNDQgMS4xNS40PSI0IiAxLjU5IDAgLjQ0LS40NS40NC0xLjE2IDAtMS42eiI+PC9wYXRoPjwvc3ZnPg==)
:::

[]{aria-hidden="3D\"false\""}
:::

</div>

::: {#3D\"description\"}
:::
:::

This documentation is for a release that = is no longer maintained

See documentation for the latest supported versi= on
[3](3D%22https://docs.redhat.com/en/documentation/openshift_container_=){platform=""
3.11\"=""} or the latest supported version
[4](3D%22https://doc=){s.redhat.com="" en="" documentation=""
openshift_container_platform="" latest\"=""}.

::: {.3D\"docs-content-container\" lang="3D\"en\"" =="" v-c6b48c1e="3D\"\""}
# Chapter 3. Migrating from Je= nkins to Tekton {#chapter-3.-migrating-from-je-nkins-to-tekton .3D= data-id="3D\"content_chapter\"" \"chapter-title\"="" v-c6b48c1e="3D\"\""}

------------------------------------------------------------------------

::: {#3D\"= .section .3D\"chapter\" migrating-from-jenkins-to-tekton\"=""}
::: {#3D\"migratin= .section .3D\"section\" g-from-jenkins-to-tekton_setting-up-trusted-ca\"=""}
::: 3D"titlepage"
<div>

## [3.1. Migrating from Jenkins to Tekton](3D%22https://docs.redhat.com/en/documenta=){.3D\"anc= tion="" openshift_container_platform="" 4.10="" html="" cicd="" migrating-from-jenkins-to-="tekton#migrating-from-jenkins-to-tekton_setting-up-trusted-ca\"" hor-heading="" test-horse\"=""} {#migrating-from-jenkins-to-tekton .3D\"title\"}

::: {#3D\"container\" .3D\"center style="3D\"--_floating-content-translate:" -22.468="75px" -73px;\"="" top="" initialized\"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\"light\" role="3D\"status\""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>
:::

Jenkins and Tekton are extensively used to automate the process of buil=
ding, testing, and deploying applications and projects. However, Tekton
is = a cloud-native CI/CD solution that works seamlessly with Kubernetes
and Ope= nShift Container Platform. This document helps you migrate your
Jenkins CI/= CD workflows to Tekton.

::: {#3D\"jt-comparison-of-jenkins-and-tekton= .section .3D\"section\" -concepts_migrating-from-jenkins-to-tekton\"=""}
::: 3D"titlepage"
<div>

\<= div\>

### [3.1.1. Comparison of Jenkin= s and Tekton concepts](3D%22https://docs.redhat.com/en/documentation=){.3D\"anchor-heading openshift_container_platform="" 4.10="" html="" cicd="" migrating-from-jenkins-to-tekt="on#jt-comparison-of-jenkins-and-tekton-concepts_migrating-from-jenkins-to-t=" ekton\"="" test-horse\"=""} {#comparison-of-jenkin-s-and-tekton-concepts .3D\"title\"}

::: {#3D\"container\" .3D\"center style="3D\"--_floating-content-translate:" -22.046="875px" -68px;\"="" top="" initialized\"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\"light\" role="3D\"status\""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>
:::

This section summarizes the basic terms used in Jenkins and Tekton, an=
d compares the equivalent terms.

::: {#3D\"jenkins-terminology\" .section .3D\"section\"}
::: {.3D= \"titlepage\"=""}
<div>

<div>

#### [3.1.1.1. Jenkins terminology](3D%22https://docs.redhat.co=){.3D\"anchor-heading m="" en="" documentation="" openshift_container_platform="" 4.10="" html="" cicd="" migrating-fr="om-jenkins-to-tekton#jenkins-terminology\"" test-hors="e\""} {#jenkins-terminology .3D\"title\"}

::: {#3D\"container\" .3D\"center style="3D\"--_floating-content-translate:" -21.625="px" -64px;\"="" top="" initialized\"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\"light\" role="3D\"status\""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

Jenkins offers declarative and scripted pipelines that are extensible=
using shared libraries and plugins. Some basic terms in Jenkins are as
fol= lows:

::: 3D"itemizedlist"
-   [**Pipeline**]{.3D\"strong strong\"=""}: Aut= omates the entire
    process of building, testing, and deploying applications,= using the
    [Groovy](3D%22https://groovy-lang.org/%22){.3D\"link\"} s= yntax.
-   [**Node**]{.3D\"strong strong\"=""}: A machi= ne capable of either
    orchestrating or executing a scripted pipeline.
-   [**Stage**]{.3D\"strong strong\"=""}: A conc= eptually distinct
    subset of tasks performed in a pipeline. Plugins or user =
    interfaces often use this block to display status or progress of
    tasks.
-   [**Step**]{.3D\"strong strong\"=""}: A singl= e task that specifies
    the exact action to be taken, either by using a comma= nd or a
    script.
:::

::: {#3D\"tekton-te= .section .3D\"section\" rminology\"=""}
::: 3D"titlepage"
<div>

<div>

#### [3.1.1.2. Tekton terminology](=3D%22https://docs.redhat.com/en/documentation/openshift_container_platform/4=){.3D= .10="" html="" cicd="" migrating-from-jenkins-to-tekton#tekton-terminology\"="" \"anchor-heading="" test-horse\"=""} {#tekton-terminology .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

Tekton uses the [YAML](3D%22https://yaml.org/%22){.3D\"link\"}= syntax
for declarative pipelines and consists of tasks. Some basic terms i= n
Tekton are as follows:

::: 3D"itemizedlist"
-   [**Pipeline**]{.3D\"strong strong\"=""}: A s= et of tasks in a
    series, in parallel, or both.

-   [**Task**]{.3D\"strong strong\"=""}: A seque= nce of steps as
    commands, binaries, or scripts.

-   [**PipelineRun**]{.3D\"strong strong\"=""}: = Execution of a
    pipeline with one or more tasks.

-   [**TaskRun**]{.3D\"strong strong\"=""}: Exec= ution of a task with
    one or more steps.

    ::: {#3D\"left-column\"}
    ::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
    ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTE2IiAwYzcuMTc4IDAgMD0iNy4xNzgiIDAgMTZzNy4xNzggMTYgMTYgMTYgMTYtNy4xNzggMTYtMTZzMjQuODIyIDAgMTYgMHptMS4yNSAyM2ExLjI1IDEuMjUgMD0iMSIgMS0yLjUgMHYtOGExLjI1IDEuMjUgMCAxIDEgMi41IDB2OHptMTYgOS41YTEuNSAxLjUgMCAxIDEgMC0zIDEuNSAxLjUgMCAwPSIxIiAwIDN6Ij48L3BhdGg+PC9zdmc+)
    :::
    :::

    ::: {#3D\"middle-column\"}
    <div>

    ::: {#3D\"header\"}
    :::

    </div>

    ::: {#3D\"description\"}
    :::
    :::

    ::: {.3D\"admonition_header\" slot="3D\"header\""}
    Note
    :::

    \<= div\>

    You can initiate a PipelineRun or a TaskRun with a set of inputs s=
    uch as parameters and workspaces, and the execution results in a set
    of out= puts and artifacts.

-   [**Workspace**]{.3D\"strong strong\"=""}: In= Tekton, workspaces are
    conceptual blocks that serve the following purposes= :

    ::: 3D"itemizedlist"
    -   Storage of inputs, outputs, and build artifacts.
    -   Common space to share data among tasks.
    -   Mount points for credentials held in secrets, configurations
        held= in config maps, and common tools shared by an
        organization.
    :::

    ::: {#3D\"left-column\"}
    ::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
    ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTE2IiAwYzcuMTc4IDAgMD0iNy4xNzgiIDAgMTZzNy4xNzggMTYgMTYgMTYgMTYtNy4xNzggMTYtMTZzMjQuODIyIDAgMTYgMHptMS4yNSAyM2ExLjI1IDEuMjUgMD0iMSIgMS0yLjUgMHYtOGExLjI1IDEuMjUgMCAxIDEgMi41IDB2OHptMTYgOS41YTEuNSAxLjUgMCAxIDEgMC0zIDEuNSAxLjUgMCAwPSIxIiAwIDN6Ij48L3BhdGg+PC9zdmc+)
    :::
    :::

    ::: {#3D\"middle-column\"}
    <div>

    ::: {#3D\"header\"}
    :::

    </div>

    ::: {#3D\"description\"}
    :::
    :::

    ::: {.3D\"admonition_header\" slot="3D\"header\""}
    Note
    :::

    \<= div\>

    In Jenkins, there is no direct equivalent of Tekton workspaces. Yo=
    u can think of the control node as a workspace, as it stores the
    cloned cod= e repository, build history, and artifacts. In
    situations where a job is as= signed to a different node, the cloned
    code and the generated artifacts are= stored in that node, but the
    build history is maintained by the control no= de.
:::

::: {#3D\"mapping-of-concepts\" .section .3D\"se= ction\"=""}
::: 3D"titlepage"
<div>

<div>

#### [3.1.1.3. Mapping of = concepts](3D%22https://docs.redhat.com/en/documentation/openshift=){.3D\"anchor-heading _container_platform="" 4.10="" html="" cicd="" migrating-from-jenkins-to-tekton#mapping="-of-concepts\"" test-horse\"=""} {#mapping-of-concepts cl="ass=3D\"title\""}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

The building blocks of Jenkins and Tekton are not equivalent, and a c=
omparison does not provide a technically accurate mapping. The following
te= rms and concepts in Jenkins and Tekton correlate in general:

::: {#3D\"wrapper\" st="yle=3D\"background-color:" light-dark(var(--rh-color-surface-lightest,="" #fffff="f),var(--rh-color-surface-darker," #1f1f1f));\"=""}
=20 =20 =20
:::

![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSIzRCZxdW90O25vbmUmcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMjg9IjI4JnF1b3Q7Ij4KICAgIDxwYXRoIGZpbGw9IjNEJnF1b3Q7I0YwRUZFRiZxdW90OyIgZD0iM0QmcXVvdDtNMCIgMGgyOHYyOGgweiI+PC9wYXRoPgogICAgPGcgY2xpcC1wYXRoPSIzRCZxdW90O3VybCgjYSkmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xMi4yNSIgMTVoLTMuNWEuNzUuNzUgMCAwIDAtLjUzMSAxLjI4MWwxLjAyOC45NjktMy4xIDMuMTAzPSJhLjUwMi41MDIiIDAgMCAwIDAgLjcwNmwuNzk0Ljc5NGEuNTAyLjUwMiAwIDAgMCAuNzA2IDBsMy4xMDMtMy4xMDMuOTcyIDEuMDMxPSJBLjc0OS43NDkiIDAgMCAwIDEzIDE5LjI1di0zLjVhLjc0OC43NDggMCAwIDAtLjc1LS43NXptMy41LTJoMy41YS43NTEuNzUxIDA9IjAiIDAgLjUzMS0xLjI4MWwtMS4wMzEtLjk2OSAzLjEwMy0zLjEwM2EuNTAyLjUwMiAwIDAgMCAwLS43MDZsLS43OTQtLjc5NGEuNTA9IjIuNTAyIiAwIDAgMC0uNzA2IDBsMTcuMjUgOS4yNWwtLjk3Mi0xLjAzMWEuNzQ5Ljc0OSAwIDAgMCAxNSA4Ljc1djMuNWMwIC40MTY9Ii4zMzQuNzUuNzUuNzVabTMiIDQuMjUgMS4wMzEtLjk3MmEuNzQ5Ljc0OSAwIDAgMCAxOS4yNSAxNWgtMy41YS43NDguNzQ4IDAgMD0iMC0uNzUuNzV2My41YS43NTEuNzUxIiAwIDAgMCAxLjI4MS41MzFsLjk2OS0xLjAyOCAzLjEwMyAzLjEwM2EuNTAyLjUwMiAwIDAgMD0iLjcwNiIgMGwuNzk0LS43OTRhLjUwMi41MDIgMCAwIDAgMC0uNzA2bDE4Ljc1IDE3LjI1em0tNy4wMzEtOS4wMjgtLjk3IDEuMDI4PSItMy4xMDItMy4xMDNhLjUwMi41MDIiIDAgMCAwLS43MDYgMGwtLjc5NC43OTRhLjUwMi41MDIgMCAwIDAgMCAuNzA2bDkuMjUgMTAuPSI3NWwtMS4wMzEuOTcyQS43NDkuNzQ5IiAwIDAgMCA4Ljc0OSAxM2gzLjVjLjQxNiAwIC43NS0uMzM0Ljc1LS43NXYtMy41YzAtLjY2PSI2LS44MDktMS0xLjI4LS41MjhaJnF1b3Q7IiBmaWxsPSIzRCZxdW90OyM5QjlCOUImcXVvdDsiPjwvcGF0aD4KICAgIDwvZz4KICAgIDxkZWZzPgogICAgICA8Y2xpcHBhdGggaWQ9IjNEJnF1b3Q7YSZxdW90OyI+CiAgICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDsjZmZmJnF1b3Q7IiB0cmFuc2Zvcm09IjNEJnF1b3Q7dHJhbnNsYXRlKDYiIDYpIiBkPSIzRCZxdW90O00wIiAwaDE2djE2aDB6PSImZ3Q7Jmx0Oy9wYXRoJmd0OwogICAgICAmbHQ7L2NsaXBQYXRoJmd0OwogICAgJmx0Oy9kZWZzJmd0OwogICZsdDsvc3ZnJmd0OwombHQ7L2J1dHRvbiZndDsKJmx0Oy90ZW1wbGF0ZSZndDsmbHQ7dGFibGUgY2xhc3M9M0QiIGx0LTQtY29scyBsdC03LXJvd3MiPjxjYXB0aW9uIHN0eWxlPSIzRCZxdW90O3RleHQtYWxpZz0iIG46IGxlZnQ7Ij5UYWJsZcKgMy4xLsKgSmVua2lucyBhbmQgVGVrdG9uIC0gYmFzaWMgY29tcGFyaXNvbjwvY2FwdGk9Pjxjb2xncm91cD48Y29sIHN0eWxlPSIzRCZxdW90O3dpZHRoOiIgNTAlOyAiIGNsYXNzPSIzRCZxdW90O2NvbF8xJnF1b3Q7Ij48IS0tRW1wdHktLT48Y29sIHM9InR5bGU9M0QmcXVvdDt3aWR0aDoiIDUwJTsgIiBjbGFzcz0iM0QmcXVvdDtjb2xfMiZxdW90OyI+PCEtLUVtcHR5LS0+PC9jb2xncm91cD48dGhlYWQ+PHRyPjx0aD0gYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaWQ9IjNEJnF1b3Q7aWRtMTQwMDUyMDk4ODAwNDgwJnF1b3Q7IiBzY29wZT0iM0QmcXVvdDtjb2wmcXVvdDsiIGRhdGE9Ii1yb3c9M0QmcXVvdDsxJnF1b3Q7IiBkYXRhLWNvbD0iM0QmcXVvdDsxJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDtjb250ZW50LS1zbSZxdW90OyI+SmVua2luczwvdGg+PHRoIGFsaWduPSIzRCZxdW90O2xlPSIgZnQiIHZhbGlnbj0iM0QmcXVvdDt0b3AmcXVvdDsiIGlkPSIzRCZxdW90O2lkbTE0MDA1MjA5ODc5OTM5MiZxdW90OyIgc2NvcGU9IjNEJnF1b3Q7Y29sJnF1b3Q7IiBkYXRhLXJvdz0iM0QmcXVvdDsxJnF1b3Q7IiBkPSJhdGEtY29sPTNEJnF1b3Q7MiZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7Y29udGVudC0tc20mcXVvdDsiPlRla3RvbjwvdGg+PC90cj48L3RoZWFkPjx0Ym9keT48dHI+PHRkID0gYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaGVhZGVycz0iM0QmcXVvdDtpZG0xNDAwNTIwOTg4MDA0ODAmcXVvdDsiIGRhdGEtcm93PSIzRCZxdW90OzImcXVvdDs9IiBkYXRhLWNvbD0iM0QmcXVvdDsxJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDtjb250ZW50LS1tZCZxdW90OyI+IDxwPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgUGlwZWxpbmUKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9wPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90ZD48dGQgYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaGVhZGVycz0iM0QmcXVvdDtpZG0xNDAwNTIwOTg3OTk9IiAzOTIiIGRhdGEtcm93PSIzRCZxdW90OzImcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzImcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLW1kJnF1b3Q7Ij4gPHA+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBQaXBlbGluZSBhbmQgUGlwZWxpbmVSdW4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9wPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90ZD48L3RyPjx0cj48dGQgYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaGVhZGVycz0iM0QmcXVvdDtpZG0xNDA9IiAwNTIwOTg4MDA0ODAiIGRhdGEtcm93PSIzRCZxdW90OzMmcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzEmcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLW1kJnF1b3Q7Ij4gPHA+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBTdGFnZQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3A+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RkPjx0ZCBhbGlnbj0iM0QmcXVvdDtsZWZ0JnF1b3Q7IiB2YWxpZ249IjNEJnF1b3Q7dG9wJnF1b3Q7IiBoZWFkZXJzPSIzRCZxdW90O2lkbTE0MDA1MjA5ODc5OT0iIDM5MiIgZGF0YS1yb3c9IjNEJnF1b3Q7MyZxdW90OyIgZGF0YS1jb2w9IjNEJnF1b3Q7MiZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7Y29udGVudC0tbWQmcXVvdDsiPiA8cD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFRhc2sKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9wPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90ZD48L3RyPjx0cj48dGQgYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaGVhZGVycz0iM0QmcXVvdDtpZG0xNDA9IiAwNTIwOTg4MDA0ODAiIGRhdGEtcm93PSIzRCZxdW90OzQmcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzEmcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLW1kJnF1b3Q7Ij4gPHA+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBTdGVwCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvcD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdGQ+PHRkIGFsaWduPSIzRCZxdW90O2xlZnQmcXVvdDsiIHZhbGlnbj0iM0QmcXVvdDt0b3AmcXVvdDsiIGhlYWRlcnM9IjNEJnF1b3Q7aWRtMTQwMDUyMDk4Nzk5PSIgMzkyIiBkYXRhLXJvdz0iM0QmcXVvdDs0JnF1b3Q7IiBkYXRhLWNvbD0iM0QmcXVvdDsyJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDtjb250ZW50LS1tZCZxdW90OyI+IDxwPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQSBzdGVwIGluIGEgdGFzawogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3A+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RkPjwvdHI+PC90Ym9keT48L3RhYmxlPjwvcmgtdGFibGU+PC9zZWN0aW9uPjwvc2VjdGlvbj48c2VjdGlvbj0gY2xhc3M9IjNEJnF1b3Q7c2VjdGlvbiZxdW90OyIgaWQ9IjNEJnF1b3Q7anQtbWlncmF0aW5nLWEtc2FtcGxlLXBpcGVsaW5lLWZyb20tamVua2lucy10by10ZWs9IiB0b25fbWlncmF0aW5nLWZyb20tamVua2lucy10by10ZWt0b24iPjxkaXYgY2xhc3M9IjNEJnF1b3Q7dGl0bGVwYWdlJnF1b3Q7Ij48ZGl2PjxkaXY+PGg9IDMgY2xhc3M9IjNEJnF1b3Q7dGl0bGUmcXVvdDsiPjxhIGhyZWY9IjNEJnF1b3Q7aHR0cHM6Ly9kb2NzLnJlZGhhdC5jb20vZW4vZG9jdW1lbnRhdGlvbi9vcGVucz0iIGhpZnRfY29udGFpbmVyX3BsYXRmb3JtIDQuMTAgaHRtbCBjaWNkIG1pZ3JhdGluZy1mcm9tLWplbmtpbnMtdG8tdGVrdG9uI2p0LT0ibWlncmF0aW5nLWEtc2FtcGxlLXBpcGVsaW5lLWZyb20tamVua2lucy10by10ZWt0b25fbWlncmF0aW5nLWZyb20tamVua2lucy10PSIgby10ZWt0b24iIGNsYXNzPSIzRCZxdW90O2FuY2hvci1oZWFkaW5nIiB0ZXN0LWhvcnNlIj4zLjEuMi7CoE1pZ3JhdGluZyBhIHNhbXBsPQplIHBpcGVsaW5lIGZyb20gSmVua2lucyB0byBUZWt0b248L2E+PHJoLXRvb2x0aXAgcG9zaXRpb249IjNEJnF1b3Q7dG9wJnF1b3Q7Ij48dGVtcGxhdGU9IHNoYWRvd21vZGU9IjNEJnF1b3Q7b3BlbiZxdW90OyI+PCEtLS0tPgogICAgICA8ZGl2IGlkPSIzRCZxdW90O2NvbnRhaW5lciZxdW90OyIgc3R5bGU9IjNEJnF1b3Q7JnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDsiIGNlbnRlciAiPgogICAgICAgIDxkaXYgaWQ9IjNEJnF1b3Q7aW52b2tlciZxdW90OyI+CiAgICAgICAgICA8c2xvdCBpZD0iM0QmcXVvdDtpbnZva2VyLXNsb3QmcXVvdDsiPjwvc2xvdD4KICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGlkPSIzRCZxdW90O3Rvb2x0aXAmcXVvdDsiIHJvbGU9IjNEJnF1b3Q7c3RhdHVzJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDsiIGRhcmsgIj4KICAgICAgICAgIDxzbG90IGlkPSIzRCZxdW90O2NvbnRlbnQmcXVvdDsiIG5hbWU9IjNEJnF1b3Q7Y29udGVudCZxdW90OyI+PCEtLT9saXQkMjE3MTA1OTYzJC0tPjwvc2xvPT4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8L3RlbXBsYXRlPjxyaC1idXR0b24gY2xhc3M9IjNEJnF1b3Q7Y29weS1saW5rLWJ0biZxdW90OyIgdmFyaWFudD0iM0QmcXVvdDtsaW5rJnF1b3Q7IiBhcmlhLWxhYj0iZWw9M0QmcXVvdDtDb3B5IiBsaW5rIHRvIGNsaXBib2FyZCI+PHRlbXBsYXRlIHNoYWRvd21vZGU9IjNEJnF1b3Q7b3BlbiZxdW90OyIgc2hhZG93ZGVsZWdhdGVzPSJmb2N1cz0zRCZxdW90OyZxdW90OyI+PCEtLS0tPgogICAgICA8YnV0dG9uIHBhcnQ9IjNEJnF1b3Q7YnV0dG9uJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDsiIGxpbmsgIiBhcmlhLWRpc2FibGVkPSIzRCZxdW90O2ZhbHNlJnF1b3Q7Ij4KICAgICAgICA8c3BhbiBhcmlhLWhpZGRlbj0iM0QmcXVvdDt0cnVlJnF1b3Q7Ij4KICAgICAgICAgIDxzbG90IGlkPSIzRCZxdW90O2ljb24mcXVvdDsiIHBhcnQ9IjNEJnF1b3Q7aWNvbiZxdW90OyIgbmFtZT0iM0QmcXVvdDtpY29uJnF1b3Q7Ij48IS0tP2xpdCQyMTcxMDU5NjMkPQotLT48cmgtaWNvbiBzZXQ9IjNEJnF1b3Q7dWkmcXVvdDsiIGljb249IjNEJnF1b3Q7JnF1b3Q7Ij48dGVtcGxhdGUgc2hhZG93bW9kZT0iM0QmcXVvdDtvcGVuJnF1b3Q7Ij48IS0tLS0+CiAgICAgIDxkaXYgaWQ9IjNEJnF1b3Q7Y29udGFpbmVyJnF1b3Q7IiBhcmlhLWhpZGRlbj0iM0QmcXVvdDtmYWxzZSZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7IiB1aSAiPjwhLS0/bGl0JDI9CjE3MTA1OTYzJC0tPjxzcGFuIHBhcnQ9IjNEJnF1b3Q7ZmFsbGJhY2smcXVvdDsiPjxzbG90Pjwvc2xvdD48L3NwYW4+CiAgICAgIDwvZGl2PgogICAgPC90ZW1wbGF0ZT48L3JoLWljb24+PC9zbG90PgogICAgICAgIDwvc3Bhbj4KICAgICAgICA8c3BhbiBhcmlhLWhpZGRlbj0iM0QmcXVvdDtmYWxzZSZxdW90OyI+PHNsb3QgaWQ9IjNEJnF1b3Q7dGV4dCZxdW90OyI+PC9zbG90Pjwvc3Bhbj4KICAgICAgPC9idXR0b24+CiAgICA8L3RlbXBsYXRlPjxyaC1pY29uIGNsYXNzPSIzRCZxdW90O2xpbmstaWNvbiZxdW90OyIgc2V0PSIzRCZxdW90O3VpJnF1b3Q7IiBpY29uPSIzRCZxdW90O2xpbmsmcXVvdDsiIHNpemU9Ij0zRCZxdW90O3NtJnF1b3Q7IiBhcmlhLWxhYmVsPSIzRCZxdW90O0NvcHkiIGxpbmsiPjx0ZW1wbGF0ZSBzaGFkb3dtb2RlPSIzRCZxdW90O29wZW4mcXVvdDsiPjwhLS0tLT4KICAgICAgPGRpdiBpZD0iM0QmcXVvdDtjb250YWluZXImcXVvdDsiIGFyaWEtaGlkZGVuPSIzRCZxdW90O3RydWUmcXVvdDsiIGNsYXNzPSIzRCZxdW90OyIgdWkgIj48IS0tP2xpdCQyMT0KNzEwNTk2MyQtLT48IS0tID1DMj1BOSBSZWQgSGF0LCBJbmMuIENDLUJZLTQuMCBsaWNlbnNlZCAtLT48c3ZnIHhtbG5zPSIzRCZxdW90O2h0PSIgdHA6IHd3dy53My5vcmcgMjAwMCBzdmciIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAzMiAzMiI+PHBhdGggZD0iM0QmcXVvdDtNMjkuNzIxIiAyLjI3OWMtMz0iLjAzNC0zLjAzNS03Ljk3LTMuMDM0LTExLjAwMyIgMGwtNi4xNjUgNi4xNjRjLTMuMDM0IDMuMDM0LTMuMDM0IDcuOTcgMCAxMS4wMD0iNGE4LjUyNSIgOC41MjUgMCAwIDAgMS45ODIgMS40MzggMSAxIDAgMCAwIC45My0xLjc3IDYuNTI2IDYuNTI2IDAgMCAxLTEuNDk4LT0iMS4wODIiIDUuNzg3IDUuNzg3IDAgMCAxIDAtOC4xNzZsNi4xNjUtNi4xNjRjMi4yNTQtMi4yNTUgNS45MjItMi4yNTQgOC4xNzUgMD0iczIuMjU0IiA1LjkyMSAwIDguMTc1bC0zLjQwNSAzLjQwNWExIDEgMCAxIDAgMS40MTUgMS40MTRsMy40MDQtMy40MDVjMy4wMzQtMz0iLjAzNCIgMy4wMzQtNy45NyAwLTExLjAwM3oiPjwvcGF0aD48cGF0aCBkPSIzRCZxdW90O00xNy40NjUiIDExLjExNWExIDEgMCAwIDAtLjkzIDE9Ii43NyIgNi41NzEgNi41NzEgMCAwIDEgMS40OTggMS4wODIgNS43ODcgNS43ODcgMCAwIDEgMCA4LjE3NWwtNi4xNjUgNi4xNjVhNS49Ijc4NyIgNS43ODcgMCAwIDEtOC4xNzUgMCA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc1bDMuNDA0LTMuNDA1YTEgMSAwIDEgMC0xLjQ9IjE0LTEuNDE0TDIuMjgiIDE4LjcxOGMtMy4wMzQgMy4wMzMtMy4wMzQgNy45NyAwIDExLjAwMyAxLjUxNiAxLjUxNyAzLjUwOSAyLjI9Ijc1IiA1LjUwMSAyLjI3NXMzLjk4NS0uNzU4IDUuNTAyLTIuMjc1bDYuMTY1LTYuMTY1YzMuMDMzLTMuMDMzIDMuMDMzLTcuOTcgMC09IjExLjAwM2E4LjUyNSIgOC41MjUgMCAwIDAtMS45ODItMS40Mzh6Ij48L3BhdGg+PC9zdmc+)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

This section provides equivalent examples of pipelines in Jenkins and =
Tekton and helps you to migrate your build, test, and deploy pipelines
from= Jenkins to Tekton.

::: {#3D\"jenkins-pipeline\" .section .3D\"section\"}
::: {.3D\"ti= tlepage\"=""}
<div>

<div>

#### [3.1= .2.1. Jenkins pipeline](3D%22https://docs.redhat.com/e=){.3D\"anchor-heading n="" documentation="" openshift_container_platform="" 4.10="" html="" cicd="" migrating-from-="jenkins-to-tekton#jenkins-pipeline\"" test-horse\"=""} {#jenkins-pipeline .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

Consider a Jenkins pipeline written in Groovy for building, testing, =
and deploying:

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22
23. 23
24. 24
25. 25
26. 26
27. 27
28. 28
29. 29
30. 30
31. 31
32. 32
33. 33
34. 34
35. 35
36. 36
37. 37
38. 38
39. 39
40. 40
41. 41
42. 42

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-plaintext\" tabindex="3D\"0\""}
pipeline {
   agent any
   stages {
       stage('Build') {
           steps {
               sh 'make'
           }
       }
       stage('Test'){
           steps {
               sh 'make check'
               junit 'reports/**/*.xml'
           }
       }
       stage('Deploy') {
           steps {
               sh 'make publish'
           }
       }
   }
}
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::

::: {#3D\"tekton-pipeline\" .section .3D\"section\"}
::: {clas="s=3D\"titlepage\""}
<div>

<div>

#### [3.1.2.2. Tekton pipeline](3D%22https://docs.redha=){.3D\"anchor-heading t.com="" en="" documentation="" openshift_container_platform="" 4.10="" html="" cicd="" migratin="g-from-jenkins-to-tekton#tekton-pipeline\"" test-hors="e\""} {#tekton-pipeline .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

In Tekton, the equivalent example of the Jenkins pipeline comprises o= f
three tasks, each of which can be written declaratively using the YAML
sy= ntax:

::: 3D"formalpara"
**Example build task**

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
  name: myproject-build
specworkspa=
ces:
  - : source
  steps:
  - : my-ci-image
    comma=
nd: ["make"]
    worki=
ngDir: $(workspaces.source.path)
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: 3D"formalpara"
**Exa= mple `test`{.3D\"literal\"} task:**

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22
23. 23
24. 24
25. 25
26. 26
27. 27
28. 28
29. 29
30. 30
31. 31
32. 32

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
  name: myproject-test
specworkspa=
ces:
  - : source
  steps:
  - : my-ci-image
    comma=
nd: ["make check"]
    worki=
ngDir: $(workspaces.source.path)
  - : junit-report-image
    scrip=
t: |
      #!/usr/bin/env bash
      junit-report reports/**/*.xml
    worki=
ngDir: $(workspaces.source.path)
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: 3D"formalpara"
**Exa= mple `deploy`{.3D\"literal\"} task:**

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
  name: myprojectd-deploy
specworkspa=
ces:
  - : source
  steps:
  - : my-deploy-image
    comma=
nd: ["make deploy"]
    worki=
ngDir: $(workspaces.source.path)
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

You can combine the three tasks sequentially to form a Tekton pipelin=
e:

::: 3D"formalpara"
**Example: Tekt= on pipeline for building, testing, and deployment**

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22
23. 23
24. 24
25. 25
26. 26
27. 27
28. 28
29. 29
30. 30
31. 31
32. 32
33. 33
34. 34
35. 35
36. 36
37. 37
38. 38
39. 39
40. 40
41. 41
42. 42
43. 43
44. 44
45. 45
46. 46
47. 47
48. 48
49. 49
50. 50
51. 51
52. 52

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
  name: myproject-pipeline
specworkspa=
ces:
  - : shared-dir
  tasks:
  - : build
    taskR=
ef:
      nam=
e: myproject-build
    works=
paces:
    - name: source
      wor=
kspace: shared-dir
  - : test
    taskR=
ef:
      nam=
e: myproject-test
    works=
paces:
    - name: source
      wor=
kspace: shared-dir
  - : deploy
    taskR=
ef:
      nam=
e: myproject-deploy
    works=
paces:
    - name: source
      wor=
kspace: shared-dir
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: {#3D\"jt-= .section .3D\"section\" migrating-from-jenkins-plugins-to-tekton-hub-tasks_migrating-from-jenkins-t="o-tekton\""}
::: 3D"titlepage"
<div>

<div>

### [3.1.3. Migrating from Jenkins plugins to Tekton Hub = tasks](3D=){.3D\"anchor-he= \"https:="" docs.redhat.com="" en="" documentation="" openshift_container_platform="" 4.10="/html/cicd/migrating-from-jenkins-to-tekton#jt-migrating-from-jenkins-plugi=" ns-to-tekton-hub-tasks_migrating-from-jenkins-to-tekton\"="" ading="" test-horse\"=""} {#migrating-from-jenkins-plugins-to-tekton-hub-tasks .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

You can extend the capability of Jenkins by using [plugins]{.3D\"link\"
hr="ef=3D\"https://plugins.jenkinsci.org/\""}. To achieve similar exten=
sibility in Tekton, use any of the available tasks from [Tekton
Hub]{.3D\"link\" h="ref=3D\"https://hub.tekton.dev/\""}.

As an example, consider the
[git-clone](3D%22https://hub.tekt=){.3D\"link\" on.dev="" tekton=""
task="" git-clone\"=""} task available in the Tekton Hu= b, that
corresponds to the [git
plugin](3D%22https://plugins.jenkin=){.3D\"link\" s.io="" git="" \"=""}
for Jenkins.

::: 3D"formalpara"
**Example: git-clone task from Tekton Hub**

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22
23. 23
24. 24
25. 25
26. 26
27. 27
28. 28
29. 29
30. 30
31. 31
32. 32
33. 33
34. 34
35. 35
36. 36
37. 37
38. 38
39. 39
40. 40
41. 41
42. 42
43. 43
44. 44

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
 name: demo-pipeline
specparams:
   - name: repo_url
   - name: revision
 workspac=
es:
   - name: source
 tasks:
   - name: fetch-from-git
     task=
Ref:
       na=
me: git-clone
     para=
ms:
       =
- name: url
         =
value: $(params.repo_url)
       =
- name: revision
         =
value: $(params.revision)
     work=
spaces:
     -<=
/span> name: output
       wo=
rkspace: source
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: {#3D\"jt-extending-t= .section .3D\"section\" ekton-capabilities-using-custom-tasks-and-scripts_migrating-from-jenkins-to="-tekton\""}
::: 3D"titlepage"
<div>

<div>

### [3.1.4. Extending Tekton capabilities using = custom tasks and scripts](3D%22=){.3D\"= https:="" docs.redhat.com="" en="" documentation="" openshift_container_platform="" 4.10="" =="" html="" cicd="" migrating-from-jenkins-to-tekton#jt-extending-tekton-capabilities="-using-custom-tasks-and-scripts_migrating-from-jenkins-to-tekton\"" anchor-heading="" test-horse\"=""} {#extending-tekton-capabilities-using-custom-tasks-and-scripts .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

In Tekton, if you do not find the right task in Tekton Hub, or need gr=
eater control over tasks, you can create custom tasks and scripts to
extend= Tekton=E2=80=99s capabilities.

::: 3D"formalpara"
Example: Custo= m task for running the `maven test`{.3D\"literal\"}
command

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
  name: maven-test
specworkspa=
ces:
  - : source
  steps:
  - : my-maven-image
    comma=
nd: ["mvn test"]
    worki=
ngDir: $(workspaces.source.path)
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: 3D"formalpara"
**Exam= ple: Execute a custom shell script by providing its path**

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token punctuation">...
steps:
  image: ubuntu
  script<=
/span>: |
      #!/usr/bin/env bash
      /workspace/my-script.sh
...
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: 3D"formalpara"
**Exam= ple: Execute a custom Python script by writing it in the YAML
file**=

=09

::: 3D"content-code-block-container"
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token punctuation">...
steps:
  image: python
  script<=
/span>: |
      #!/usr/bin/env python3
      print(=E2=80=9Chello from python!=E2=80=9D)
...
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: {#3D\"jt-comparison-= .section .3D\"section\" of-jenkins-tekton-execution-models_migrating-from-jenkins-to-tekton\"=""}
::: {c="lass=3D\"titlepage\""}
<div>

<div>

### [3.1= .5. Comparison of Jenkins and Tekton execution models](3D%22https://docs.re=){.3D\"anchor-heading dhat.com="" en="" documentation="" openshift_container_platform="" 4.10="" html="" cicd="" migra="ting-from-jenkins-to-tekton#jt-comparison-of-jenkins-tekton-execution-model=" s_migrating-from-jenkins-to-tekton\"="" test-horse\"=""} {#comparison-of-jenkins-and-tekton-execution-models .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

Jenkins and Tekton offer similar functions but are different in archit=
ecture and execution. This section outlines a brief comparison of the
two e= xecution models.

::: {#3D\"wrapper\" sty="le=3D\"background-color:" light-dark(var(--rh-color-surface-lightest,="" #ffffff="),var(--rh-color-surface-darker," #1f1f1f));\"=""}
=20 =20 =20
:::

![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSIzRCZxdW90O25vbmUmcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMjg9IjI4JnF1b3Q7Ij4KICAgIDxwYXRoIGZpbGw9IjNEJnF1b3Q7I0YwRUZFRiZxdW90OyIgZD0iM0QmcXVvdDtNMCIgMGgyOHYyOGgweiI+PC9wYXRoPgogICAgPGcgY2xpcC1wYXRoPSIzRCZxdW90O3VybCgjYSkmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xMi4yNSIgMTVoLTMuNWEuNzUuNzUgMCAwIDAtLjUzMSAxLjI4MWwxLjAyOC45NjktMy4xIDMuMTAzPSJhLjUwMi41MDIiIDAgMCAwIDAgLjcwNmwuNzk0Ljc5NGEuNTAyLjUwMiAwIDAgMCAuNzA2IDBsMy4xMDMtMy4xMDMuOTcyIDEuMDMxPSJBLjc0OS43NDkiIDAgMCAwIDEzIDE5LjI1di0zLjVhLjc0OC43NDggMCAwIDAtLjc1LS43NXptMy41LTJoMy41YS43NTEuNzUxIDA9IjAiIDAgLjUzMS0xLjI4MWwtMS4wMzEtLjk2OSAzLjEwMy0zLjEwM2EuNTAyLjUwMiAwIDAgMCAwLS43MDZsLS43OTQtLjc5NGEuNTA9IjIuNTAyIiAwIDAgMC0uNzA2IDBsMTcuMjUgOS4yNWwtLjk3Mi0xLjAzMWEuNzQ5Ljc0OSAwIDAgMCAxNSA4Ljc1djMuNWMwIC40MTY9Ii4zMzQuNzUuNzUuNzVabTMiIDQuMjUgMS4wMzEtLjk3MmEuNzQ5Ljc0OSAwIDAgMCAxOS4yNSAxNWgtMy41YS43NDguNzQ4IDAgMD0iMC0uNzUuNzV2My41YS43NTEuNzUxIiAwIDAgMCAxLjI4MS41MzFsLjk2OS0xLjAyOCAzLjEwMyAzLjEwM2EuNTAyLjUwMiAwIDAgMD0iLjcwNiIgMGwuNzk0LS43OTRhLjUwMi41MDIgMCAwIDAgMC0uNzA2bDE4Ljc1IDE3LjI1em0tNy4wMzEtOS4wMjgtLjk3IDEuMDI4PSItMy4xMDItMy4xMDNhLjUwMi41MDIiIDAgMCAwLS43MDYgMGwtLjc5NC43OTRhLjUwMi41MDIgMCAwIDAgMCAuNzA2bDkuMjUgMTAuPSI3NWwtMS4wMzEuOTcyQS43NDkuNzQ5IiAwIDAgMCA4Ljc0OSAxM2gzLjVjLjQxNiAwIC43NS0uMzM0Ljc1LS43NXYtMy41YzAtLjY2PSI2LS44MDktMS0xLjI4LS41MjhaJnF1b3Q7IiBmaWxsPSIzRCZxdW90OyM5QjlCOUImcXVvdDsiPjwvcGF0aD4KICAgIDwvZz4KICAgIDxkZWZzPgogICAgICA8Y2xpcHBhdGggaWQ9IjNEJnF1b3Q7YSZxdW90OyI+CiAgICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDsjZmZmJnF1b3Q7IiB0cmFuc2Zvcm09IjNEJnF1b3Q7dHJhbnNsYXRlKDYiIDYpIiBkPSIzRCZxdW90O00wIiAwaDE2djE2aDB6PSImZ3Q7Jmx0Oy9wYXRoJmd0OwogICAgICAmbHQ7L2NsaXBQYXRoJmd0OwogICAgJmx0Oy9kZWZzJmd0OwogICZsdDsvc3ZnJmd0OwombHQ7L2J1dHRvbiZndDsKJmx0Oy90ZW1wbGF0ZSZndDsmbHQ7dGFibGUgY2xhc3M9M0QiIGx0LTQtY29scyBsdC03LXJvd3MiPjxjYXB0aW9uIHN0eWxlPSIzRCZxdW90O3RleHQtYWxpZz0iIG46IGxlZnQ7Ij5UYWJsZcKgMy4yLsKgQ29tcGFyaXNvbiBvZiBleGVjdXRpb24gbW9kZWxzIGluIEplbmtpbnMgYW49CmQgVGVrdG9uPC9jYXB0aW9uPjxjb2xncm91cD48Y29sIHN0eWxlPSIzRCZxdW90O3dpZHRoOiIgNTAlOyAiIGNsYXNzPSIzRCZxdW90O2NvbF8xJnF1b3Q7Ij48IS0tLT0KLUVtcHR5LS0tLT48Y29sIHN0eWxlPSIzRCZxdW90O3dpZHRoOiIgNTAlOyAiIGNsYXNzPSIzRCZxdW90O2NvbF8yJnF1b3Q7Ij48IS0tRW1wdHktLT48L2NvbGdyb3VwPT48dGhlYWQ+PHRyPjx0aCBhbGlnbj0iM0QmcXVvdDtsZWZ0JnF1b3Q7IiB2YWxpZ249IjNEJnF1b3Q7dG9wJnF1b3Q7IiBpZD0iM0QmcXVvdDtpZG0xNDAwNTIwOTg3MzY0ODAmcXVvdDsiIHNjbz0icGU9M0QmcXVvdDtjb2wmcXVvdDsiIGRhdGEtcm93PSIzRCZxdW90OzEmcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzEmcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLXNtJnF1b3Q7Ij5KZW5raW5zPC90aD49Cjx0aCBhbGlnbj0iM0QmcXVvdDtsZWZ0JnF1b3Q7IiB2YWxpZ249IjNEJnF1b3Q7dG9wJnF1b3Q7IiBpZD0iM0QmcXVvdDtpZG0xNDAwNTIwOTg3MzUzOTImcXVvdDsiIHNjb3BlPSIzRCZxdW90O2NvbCZxdW90OyIgZD0iYXRhLXJvdz0zRCZxdW90OzEmcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzImcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLXNtJnF1b3Q7Ij5UZWt0b248L3RoPjwvdHI+PC90aGVhZD49Cjx0Ym9keT48dHI+PHRkIGFsaWduPSIzRCZxdW90O2xlZnQmcXVvdDsiIHZhbGlnbj0iM0QmcXVvdDt0b3AmcXVvdDsiIGhlYWRlcnM9IjNEJnF1b3Q7aWRtMTQwMDUyMDk4NzM2NDgwJnF1b3Q7PSIgZGF0YS1yb3c9IjNEJnF1b3Q7MiZxdW90OyIgZGF0YS1jb2w9IjNEJnF1b3Q7MSZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7Y29udGVudC0tbGcmcXVvdDsiPiA8cD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgSmVua2lucyBoYXMgYSBjb250cm9sIG5vZGUuIEplbmtpbnMgZXhlY3V0ZXMgcGlwZWxpbmVzIGFuZCBzdGVwcyBjPQplbnRyYWxseSwgb3Igb3JjaGVzdHJhdGVzIGpvYnMgcnVubmluZyBpbiBvdGhlciBub2Rlcy4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3A+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdGQ+PHRkIGFsaWduPSIzRCZxdW90O2xlZnQmcXVvdDsiIHZhbGlnbj0iM0QmcXVvdDt0b3AmcXVvdDsiIGhlYWRlcnM9IjNEJnF1b3Q7aWRtMTQwMDUyMDk4NzM1Mz0iIDkyIiBkYXRhLXJvdz0iM0QmcXVvdDsyJnF1b3Q7IiBkYXRhLWNvbD0iM0QmcXVvdDsyJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDtjb250ZW50LS1sZyZxdW90OyI+IDxwPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBUZWt0b24gaXMgc2VydmVybGVzcyBhbmQgZGlzdHJpYnV0ZWQsIGFuZCB0aGVyZSBpcyBubyBjZW50cmFsIGRlcGU9Cm5kZW5jeSBmb3IgZXhlY3V0aW9uLgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvcD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90ZD48L3RyPjx0cj48dGQgYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaGVhZGVycz0iM0QmcXVvdDtpZG0xNDAwPSIgNTIwOTg3MzY0ODAiIGRhdGEtcm93PSIzRCZxdW90OzMmcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzEmcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLWxnJnF1b3Q7Ij4gPHA+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFRoZSBjb250YWluZXJzIGFyZSBsYXVuY2hlZCBieSB0aGUgY29udHJvbCBub2RlIHRocm91Z2ggdGhlIHBpcGVsaT0KbmUuCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9wPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3RkPjx0ZCBhbGlnbj0iM0QmcXVvdDtsZWZ0JnF1b3Q7IiB2YWxpZ249IjNEJnF1b3Q7dG9wJnF1b3Q7IiBoZWFkZXJzPSIzRCZxdW90O2lkbTE0MDA1MjA5ODczNTM9IiA5MiIgZGF0YS1yb3c9IjNEJnF1b3Q7MyZxdW90OyIgZGF0YS1jb2w9IjNEJnF1b3Q7MiZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7Y29udGVudC0tbGcmcXVvdDsiPiA8cD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgVGVrdG9uIGFkb3B0cyBhICYjMzk7Y29udGFpbmVyLWZpcnN0JiMzOTsgYXBwcm9hY2gsIHdoZXJlIGV2ZXJ5IHN0ZXAgaXMgZXg9CmVjdXRlZCBhcyBhIGNvbnRhaW5lciBydW5uaW5nIGluIGEgcG9kIChlcXVpdmFsZW50IHRvIG5vZGVzIGluIEplbmtpbnMpLgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvcD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90ZD48L3RyPjx0cj48dGQgYWxpZ249IjNEJnF1b3Q7bGVmdCZxdW90OyIgdmFsaWduPSIzRCZxdW90O3RvcCZxdW90OyIgaGVhZGVycz0iM0QmcXVvdDtpZG0xNDAwPSIgNTIwOTg3MzY0ODAiIGRhdGEtcm93PSIzRCZxdW90OzQmcXVvdDsiIGRhdGEtY29sPSIzRCZxdW90OzEmcXVvdDsiIGNsYXNzPSIzRCZxdW90O2NvbnRlbnQtLW1kJnF1b3Q7Ij4gPHA+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIEV4dGVuc2liaWxpdHkgaXMgYWNoaWV2ZWQgdXNpbmcgcGx1Z2lucy4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3A+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvdGQ+PHRkIGFsaWduPSIzRCZxdW90O2xlZnQmcXVvdDsiIHZhbGlnbj0iM0QmcXVvdDt0b3AmcXVvdDsiIGhlYWRlcnM9IjNEJnF1b3Q7aWRtMTQwMDUyMDk4NzM1Mz0iIDkyIiBkYXRhLXJvdz0iM0QmcXVvdDs0JnF1b3Q7IiBkYXRhLWNvbD0iM0QmcXVvdDsyJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDtjb250ZW50LS1sZyZxdW90OyI+IDxwPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBFeHRlbnNpYmlsaXR5IGlzIGFjaGlldmVkIHVzaW5nIHRhc2tzIGluIFRla3RvbiBIdWIsIG9yIGJ5IGNyZWF0aW49CmcgY3VzdG9tIHRhc2tzIGFuZCBzY3JpcHRzLgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvcD4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC90ZD48L3RyPjwvdGJvZHk+PC90YWJsZT48L3JoLXRhYmxlPjwvc2VjdGlvbj48c2VjdGlvbiBjbGFzcz0iM0QmcXVvdDtzPSIgZWN0aW9uIiBpZD0iM0QmcXVvdDtqdC1leGFtcGxlcy1vZi1jb21tb24tdXNlLWNhc2VzX21pZ3JhdGluZy1mcm9tLWplbmtpbnMtdG8tdGVrPSIgdG9uIj48ZGl2IGNsYXNzPSIzRCZxdW90O3RpdGxlcGFnZSZxdW90OyI+PGRpdj48ZGl2PjxoMyBjbGFzcz0iM0QmcXVvdDt0aXRsZSZxdW90OyI+PGEgaHJlZj0iM0QmcXVvdDtodHRwPSIgczogZG9jcy5yZWRoYXQuY29tIGVuIGRvY3VtZW50YXRpb24gb3BlbnNoaWZ0X2NvbnRhaW5lcl9wbGF0Zm9ybSA0LjEwIGh0bWw9Ii9jaWNkL21pZ3JhdGluZy1mcm9tLWplbmtpbnMtdG8tdGVrdG9uI2p0LWV4YW1wbGVzLW9mLWNvbW1vbi11c2UtY2FzZXNfbWlncj0iIGF0aW5nLWZyb20tamVua2lucy10by10ZWt0b24iIGNsYXNzPSIzRCZxdW90O2FuY2hvci1oZWFkaW5nIiB0ZXN0LWhvcnNlIj4zLjEuNi4mYW1wO25iPQpzcDtFeGFtcGxlcyBvZiBjb21tb24gdXNlIGNhc2VzPC9hPjxyaC10b29sdGlwIHBvc2l0aW9uPSIzRCZxdW90O3RvcCZxdW90OyI+PHRlbXBsYXRlIHM9ImhhZG93bW9kZT0zRCZxdW90O29wZW4mcXVvdDsiPjwhLS0tLT4KICAgICAgPGRpdiBpZD0iM0QmcXVvdDtjb250YWluZXImcXVvdDsiIHN0eWxlPSIzRCZxdW90OyZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7IiBjZW50ZXIgIj4KICAgICAgICA8ZGl2IGlkPSIzRCZxdW90O2ludm9rZXImcXVvdDsiPgogICAgICAgICAgPHNsb3QgaWQ9IjNEJnF1b3Q7aW52b2tlci1zbG90JnF1b3Q7Ij48L3Nsb3Q+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBpZD0iM0QmcXVvdDt0b29sdGlwJnF1b3Q7IiByb2xlPSIzRCZxdW90O3N0YXR1cyZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7IiBkYXJrICI+CiAgICAgICAgICA8c2xvdCBpZD0iM0QmcXVvdDtjb250ZW50JnF1b3Q7IiBuYW1lPSIzRCZxdW90O2NvbnRlbnQmcXVvdDsiPjwhLS0/bGl0JDIxNzEwNTk2MyQtLT48L3Nsbz0+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC90ZW1wbGF0ZT48cmgtYnV0dG9uIGNsYXNzPSIzRCZxdW90O2NvcHktbGluay1idG4mcXVvdDsiIHZhcmlhbnQ9IjNEJnF1b3Q7bGluayZxdW90OyIgYXJpYS1sYWI9ImVsPTNEJnF1b3Q7Q29weSIgbGluayB0byBjbGlwYm9hcmQiPjx0ZW1wbGF0ZSBzaGFkb3dtb2RlPSIzRCZxdW90O29wZW4mcXVvdDsiIHNoYWRvd2RlbGVnYXRlcz0iZm9jdXM9M0QmcXVvdDsmcXVvdDsiPjwhLS0tLT4KICAgICAgPGJ1dHRvbiBwYXJ0PSIzRCZxdW90O2J1dHRvbiZxdW90OyIgY2xhc3M9IjNEJnF1b3Q7IiBsaW5rICIgYXJpYS1kaXNhYmxlZD0iM0QmcXVvdDtmYWxzZSZxdW90OyI+CiAgICAgICAgPHNwYW4gYXJpYS1oaWRkZW49IjNEJnF1b3Q7dHJ1ZSZxdW90OyI+CiAgICAgICAgICA8c2xvdCBpZD0iM0QmcXVvdDtpY29uJnF1b3Q7IiBwYXJ0PSIzRCZxdW90O2ljb24mcXVvdDsiIG5hbWU9IjNEJnF1b3Q7aWNvbiZxdW90OyI+PCEtLT9saXQkMjE3MTA1OTYzJD0KLS0+PHJoLWljb24gc2V0PSIzRCZxdW90O3VpJnF1b3Q7IiBpY29uPSIzRCZxdW90OyZxdW90OyI+PHRlbXBsYXRlIHNoYWRvd21vZGU9IjNEJnF1b3Q7b3BlbiZxdW90OyI+PCEtLS0tPgogICAgICA8ZGl2IGlkPSIzRCZxdW90O2NvbnRhaW5lciZxdW90OyIgYXJpYS1oaWRkZW49IjNEJnF1b3Q7ZmFsc2UmcXVvdDsiIGNsYXNzPSIzRCZxdW90OyIgdWkgIj48IS0tP2xpdCQyPQoxNzEwNTk2MyQtLT48c3BhbiBwYXJ0PSIzRCZxdW90O2ZhbGxiYWNrJnF1b3Q7Ij48c2xvdD48L3Nsb3Q+PC9zcGFuPgogICAgICA8L2Rpdj4KICAgIDwvdGVtcGxhdGU+PC9yaC1pY29uPjwvc2xvdD4KICAgICAgICA8L3NwYW4+CiAgICAgICAgPHNwYW4gYXJpYS1oaWRkZW49IjNEJnF1b3Q7ZmFsc2UmcXVvdDsiPjxzbG90IGlkPSIzRCZxdW90O3RleHQmcXVvdDsiPjwvc2xvdD48L3NwYW4+CiAgICAgIDwvYnV0dG9uPgogICAgPC90ZW1wbGF0ZT48cmgtaWNvbiBjbGFzcz0iM0QmcXVvdDtsaW5rLWljb24mcXVvdDsiIHNldD0iM0QmcXVvdDt1aSZxdW90OyIgaWNvbj0iM0QmcXVvdDtsaW5rJnF1b3Q7IiBzaXplPSI9M0QmcXVvdDtzbSZxdW90OyIgYXJpYS1sYWJlbD0iM0QmcXVvdDtDb3B5IiBsaW5rIj48dGVtcGxhdGUgc2hhZG93bW9kZT0iM0QmcXVvdDtvcGVuJnF1b3Q7Ij48IS0tLS0+CiAgICAgIDxkaXYgaWQ9IjNEJnF1b3Q7Y29udGFpbmVyJnF1b3Q7IiBhcmlhLWhpZGRlbj0iM0QmcXVvdDt0cnVlJnF1b3Q7IiBjbGFzcz0iM0QmcXVvdDsiIHVpICI+PCEtLT9saXQkMjE9CjcxMDU5NjMkLS0+PCEtLSA9QzI9QTkgUmVkIEhhdCwgSW5jLiBDQy1CWS00LjAgbGljZW5zZWQgLS0+PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

Both Jenkins and Tekton offer capabilities for common CI/CD use cases,=
such as:

::: 3D"itemizedlist"
-   Compiling, building, and deploying images using maven
-   Extending the core capabilities by using plugins
-   Reusing shareable libraries and custom scripts
:::

::: {#3D\"running-a-maven-pipe= .section .3D\"section\" line-in-jenkins-and-tekton\"=""}
::: 3D"titlepage"
<div>

<div>

#### [3.1.= 6.1. Running a maven pipeline in Jenkins and Tekton](3D%22https://docs.redhat.com/en/documentation/openshift_conta=){.3D\"anchor-heading iner_platform="" 4.10="" html="" cicd="" migrating-from-jenkins-to-tekton#running-a-mav="en-pipeline-in-jenkins-and-tekton\"" test-horse\"=""} {#running-a-maven-pipeline-in-jenkins-and-tekton .3D= \"title\"=""}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

You can use maven in both Jenkins and Tekton workflows for compiling,=
building, and deploying images. To map your existing Jenkins workflow to
T= ekton, consider the following examples:

::: 3D"formalpara"
Example: Comp= ile and build an image and deploy it to OpenShift using
maven in Jenkins

=09

::: {.3D\"content-code-block-container\" wrap-available="3D\"true=" \"=""}
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1.  1
2.  2
3.  3
4.  4
5.  5
6.  6
7.  7
8.  8
9.  9
10. 10
11. 11
12. 12
13. 13
14. 14
15. 15
16. 16
17. 17
18. 18
19. 19
20. 20
21. 21
22. 22
23. 23
24. 24
25. 25
26. 26
27. 27
28. 28
29. 29
30. 30
31. 31
32. 32
33. 33
34. 34
35. 35
36. 36
37. 37
38. 38
39. 39
40. 40
41. 41
42. 42
43. 43
44. 44
45. 45
46. 46
47. 47
48. 48
49. 49
50. 50
51. 51
52. 52
53. 53
54. 54
55. 55
56. 56

=20
:::

::: {#3D\"actions\"}
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-plaintext\" tabindex="3D\"0\""}
#!/usr/bin/groovy
node('maven') {
    stage 'Checkout'
    checkout scm

    stage 'Build'
    sh 'cd helloworld && mvn clean'
    sh 'cd helloworld && mvn compile'

    stage 'Run Unit Tests'
    sh 'cd helloworld && mvn test'

    stage 'Package'
    sh 'cd helloworld && mvn package'

    stage 'Archive artifact'
    sh 'mkdir -p artifacts/deployments && cp helloworld/target/*.wa=
r artifacts/deployments'
    archive 'helloworld/target/*.war'

    stage 'Create Image'
    sh 'oc login https://kubernetes.default -u admin -p admin --insecure-sk=
ip-tls-verify=3Dtrue'
    sh 'oc new-project helloworldproject'
    sh 'oc project helloworldproject'
    sh 'oc process -f helloworld/jboss-eap70-binary-build.json | oc create =
-f -'
    sh 'oc start-build eap-helloworld-app --from-dir=3Dartifacts/'

    stage 'Deploy'
    sh 'oc new-app helloworld/jboss-eap70-deploy.json' }
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: 3D"formalpara"
**Exa= mple: Compile and build an image and deploy it to OpenShift using
maven in = Tekton.**

=09

::: {.3D\"content-code-block-container\" wrap-available="3D\"true=" \"=""}
::: {#3D\"container\" .3D\"expandable truncated\"="" style="3D\"column-=" gap:="" 50px;\"=""}
::: {#3D\"content-lines\" tabindex="3D\"0\""}
::: {#3D\"sizers\" aria-hidden="3D\"true\""}
:::

1

\<= !\-\-\--\>

2

\<= !\-\-\--\>

3

\<= !\-\-\--\>

4

\<= !\-\-\--\>

5

\<= !\-\-\--\>

6

\<= !\-\-\--\>

7

\<= !\-\-\--\>

8

\<= !\-\-\--\>

9

\<= !\-\-\--\>

10

=

11

=

12

=

13

=

14

=

15

=

16

=

17

=

18

=

19

=

20

=

21

=

22

=

23

=

24

=

25

=

26

=

27

=

28

=

29

=

30

=

31

=

32

=

33

=

34

=

35

=

36

=

37

=

38

=

39

=

40

=

41

=

42

=

43

=

44

=

45

=

46

=

47

=

48

=

49

=

50

=

51

=

52

=

53

=

54

=

55

=

56

=

57

=

58

=

59

=

60

=

61

=

62

=

63

=

64

=

65

=

66

=

67

=

68

=

69

=

70

=

71

=

72

=

73

=

74

=

75

=

76

=

77

=

78

=

79

=

80

=

81

=

82

=

83

=

84

=

85

=

86

=

87

=

88

=

89

=

90

=

91

=

92

=

93

=

94

=

95

=

96

=

97

=

98

=

99

=

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190
:::

Show more =20
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIHY9Imlld0JveD0zRCZxdW90OzAiIDAgMTEgNyI+CiAgICAgICAgICAgIDxwYXRoIGQ9IjNEJnF1b3Q7TTQuOTE5LjIzOS4yNDIiIDQuODQ3YS44MDEuODAxIDAgMCAwIDAgMS4xNDhsLjc3OC43NjY9ImEuODMuODMiIDAgMCAwIDEuMTY1IDBsNS41IDMuNDk1IDguODE1IDYuNzZhLjgzLjgzIDAgMCAwIDEuMTY1IDBsLjc3OC0uNzY2YS49IjgwMi44MDIiIDAgMCAwIDAtMS4xNDhsNi4wOC4yMzlhLjgyNi44MjYgMCAwIDAtMS4xNjIgMHoiPjwvcGF0aD4KICAgICAgICAgIDwvc3ZnPg==)
:::

=20

``` {.3D\"language-yaml\" tabindex="3D\"0\""}
<=
span class=3D"token key atrule">apiVersion=
: tekton.dev/v1beta1
kindmetadata<=
/span>:
  name: maven-pipeline
specworkspa=
ces:
    - name: shared-workspace
    - name: maven-settings
    - name: kubeconfig=
-dir
      opt=
ional: true
  params<=
/span>:
    - name: repo-url
    - name: revision
    - name: context-path
  tasks:
    - name: fetch-repo
      tas=
kRef:
        n=
ame: git-clone
      wor=
kspaces:
        - name: output
          workspace: shared-workspace
      par=
ams:
        - name: url
          value: "$(params.repo-url)"
        - name: subdirectory
          value: ""
        - name: deleteExisting
          value: "true"
        - name: revision
          value: $(params.revision)
    - name: mvn-build
      tas=
kRef:
        n=
ame: maven
      run=
After:
        - fetch-repo
      wor=
kspaces:
        - name: source
          workspace: shared-workspace
        - name: maven<=
span class=3D"token punctuation">-settings
          workspace: maven-settings
      par=
ams:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["-DskipTests", "clean", "compile"]
    - name: mvn-tests
      tas=
kRef:
        n=
ame: maven
      run=
After:
        - mvn-build
      wor=
kspaces:
        - name: source
          workspace: shared-workspace
        - name: maven<=
span class=3D"token punctuation">-settings
          workspace: maven-settings
      par=
ams:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["test"=
]
    - name: mvn-package
      tas=
kRef:
        n=
ame: maven
      run=
After:
        - mvn-tests
      wor=
kspaces:
        - name: source
          workspace: shared-workspace
        - name: maven<=
span class=3D"token punctuation">-settings
          workspace: maven-settings
      par=
ams:
        - name: CONTEXT_DIR
          value: "$(params.context-path)"
        - name: GOALS
          value: ["package"]
    - name: create-image-and-deploy
      tas=
kRef:
        n=
ame: openshift-client
      run=
After:
        - mvn-package
      wor=
kspaces:
        - name: manifest-dir
          workspace: shared-workspace
        - name: kubeconfig-dir
          workspace: kubeconfig-dir
      par=
ams:
        - name: SCRIPT
          value: |<=
span class=3D"token scalar string">
            cd "$(params.context-path)"
            mkdir -p ./artifacts/deployments && cp ./target/*.war .=
/artifacts/deployments
            oc new-project helloworldproject
            oc project helloworldproject
            oc process -f jboss-eap70-binary-build.json | oc create -f -
            oc start-build eap-helloworld-app --from-dir=3Dartifacts/
            oc new-app jboss-eap70-deploy.json
```

::: 3D"content-code-block-container-actions"
::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Copy to Clipboard]{.3D\"copy-link-text\"}

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMD0iMjAmcXVvdDsiPgogIDxwYXRoIGZpbGw9IjNEJnF1b3Q7Y3VycmVudENvbG9yJnF1b3Q7IiBkPSIzRCZxdW90O00xMiIgMGgyYy45IDAgMCAuOSAwIDJ2MTBoMXYyYzAtLjYuNC0xIDEtPSIxaDEwVjB6JnF1b3Q7Ij48L3BhdGg+CiAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE4IiAyMGg4Yy0xLjEgMC0yLS45LTItMnY4YzAtMS4xLjktMiAyLTI9ImgxMGMxLjEiIDAgMiAuOSAyIDJ2MTBjMCAxLjEtLjkgMi0yIDJ6bTggN2MtLjYgMC0xIC40LTEgMXYxMGMwIC42LjQgMSAxIDFoMTA9ImMuNiIgMCAxLS40IDEtMXY4YzAtLjYtLjQtMS0xLTFoOHoiPjwvcGF0aD4KPC9zdmc+)

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[Toggle word wrap]{.3D\"wrap-link-text\"}

[
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt3cmFwLWljb24mcXVvdDsiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7IiBmaWxsPSIzRCZxdW90O2M9IiB1cnJlbnRjb2xvciIgdmlld2JveD0iM0QmcXVvdDswIiAwIDIwIDIwIiBzdHlsZT0iM0QmcXVvdDtkaXNwbGF5OiIgaW5saW5lOyIgZGF0YS12aXNpYmxlLT0id2hlbj0zRCZxdW90O3dyYXBwZWQtZmFsc2UmcXVvdDsiPgogICAgICA8cGF0aCBkPSIzRCZxdW90O00xOSIgMGMuMzEzLjAzOS43ODEtLjA3NyAxIC4wNTd2MjBjLS4zMTMtLjAzOS0uNzgxLjA3Ny0xLS4wPSI1N1YwWk0xMC44MiIgNC45OTJjOS44NzcgNC45OTYgOC4zMSA1LjU3IDguMTc0IDZjMS4yMS4wMyAyLjQzMi0uMDczIDMuNjM1LjA4PSIyLjE4MS4zODMiIDMuNjc3IDIuNzk2IDMuMDY2IDQuOTIyLS40MSAxLjc1My0yLjEwOCAyLjk5NS0zLjg3NyAzLjAxNGwxMSAxNGg9IjUuMjA3bDIuNjgyLTIuNjgyLS43MDctLjcwN0wzLjI5MyIgMTQuNWwzLjg4OSAzLjg4OS43MDctLjcwN2w1LjIwNyAxNWg1LjczNmw9Ii4wMDQtLjAwOGMxLjQ0NC4wMDUiIDIuODk2LS41OSAzLjgzMi0xLjcyMiAxLjY1LTEuODIgMS42MTItNC44NS0uMDgtNi42M2E1IDU9IjAiIDAgMCAxMSA1YTEuOTQ4IDEuOTQ4IDAgMCAwLS4xOC0uMDA4eiI+PC9wYXRoPgogICAgICA8cGF0aCBkPSIzRCZxdW90O000IiA1aDdjLS4wMzkuMzEzLjA3Ny43ODEtLjA1NyAxaDR2NXptMCAwYy4zMTMuMDM5Ljc4MS0uMDc3PSIxIiAuMDU3djIwYy0uMzEzLS4wMzktLjc4MS4wNzctMS0uMDU3djB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"wrap-icon\"}
![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDt1bndyYXAtaWNvbiZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIGZpbGw9IjNEPSIgIm5vbmUiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMSAyMCIgc3R5bGU9IjNEJnF1b3Q7ZGlzcGxheToiIG5vbmU7IiBkYXRhLXZpc2libGUtd2hlbj0iM0QmcXVvdDs9IiB3cmFwcGVkLXRydWUiPgogICAgICA8cGF0aCBmaWxsPSIzRCZxdW90O2N1cnJlbnRDb2xvciZxdW90OyIgZD0iM0QmcXVvdDtNMTIiIDEzaDF2N2gtMXptMTIgMGgxdjdoLTF6Ij48L3BhdGg+CiAgICAgIDxwYXRoIHN0cm9rZT0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTE2LjQ2NSIgNi40NjQgMjAgMTBsLTMuNTM1IDMuNTM2Ij49CjwvcGF0aD4KICAgICAgPHBhdGggZmlsbD0iM0QmcXVvdDtjdXJyZW50Q29sb3ImcXVvdDsiIGQ9IjNEJnF1b3Q7TTMiIDkuNWgxN3YxaDN6bTAgMGgxdjIwaDB6Ij48L3BhdGg+CiAgICA8L3N2Zz4=){.3D\"unwrap-icon\"}
]{.3D\"wrap-toggle-icons\"}
:::
:::
:::

::: {#3D\"extending-the= .section .3D\"section\" -core-capabilities-of-jenkins-and-tekton-by-using-plugins\"=""}
::: {.3D\"ti= tlepage\"=""}
<div>

<div>

#### [3.1.6.2. Extending = the core capabilities of Jenkins and Tekton by using plugins](3D%22https://docs.redhat.com/e=){.3D\"anchor-heading n="" documentation="" openshift_container_platform="" 4.10="" html="" cicd="" migrating-from-="jenkins-to-tekton#extending-the-core-capabilities-of-jenkins-and-tekton-by-=" using-plugins\"="" test-horse\"=""} {#extending-the-core-capabilities-of-jenkins-and-tekton-by-using-plugins .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

Jenkins has the advantage of a large ecosystem of numerous plugins de=
veloped over the years by its extensive user base. You can search and
brows= e the plugins in the [Jenkins Plugin
Index](3D%22https://plugins.jenkins.io/%22=){.3D\"link\"}.

Tekton also has many tasks developed and contributed by the community=
and enterprise users. A publicly available catalog of reusable Tekton
task= s are available in the [T= ekton
Hub](3D%22https://hub.tekton.dev/%22){.3D\"link\"}.

In addition, Tekton incorporates many of the plugins of the Jenkins e=
cosystem within its core capabilities. For example, authorization is a
crit= ical function in both Jenkins and Tekton. While Jenkins ensures
authorizati= on using the [Role-based Authorization
Strategy](3D%22https://plugins.jenkins.io/role-stra=){.3D\"link\"
tegy="" \"=""} plugin, Tekton uses OpenShift= =E2=80=99s built-in
Role-based Access Control system.

::: {#3D\"sharing-reusable-code-i= .section .3D\"section\" n-jenkins-and-tekton\"=""}
::: 3D"titlepage"
<div>

<div>

#### [3.1.6.3. = ;Sharing reusable code in Jenkins and Tekton](3D%22https://docs.redhat.com/en/documentation/openshift_container_p=){.3D\"anchor-heading latform="" 4.10="" html="" cicd="" migrating-from-jenkins-to-tekton#sharing-reusable-co="de-in-jenkins-and-tekton\"" test-horse\"=""} {#sharing-reusable-code-in-jenkins-and-tekton .3D\"title= \"=""}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

Jenkins [shared
libraries](3D%22https://www.jenkins.io/doc/book/pip=){.3D\"link\"
eline="" shared-libraries="" \"=""} provide reusable code for par= ts of
Jenkins pipelines. The libraries are shared between [Jenkinsfile=
s](3D%22https://www.jenkins.io/doc/book/pipeline/jenkinsfile/%22){.3D\"link\"=}
to create highly modular pipelines without code repetition.

Although there is no direct equivalent of Jenkins shared libraries in=
Tekton, you can achieve similar workflows by using tasks from the
[Tekton Hub](3D%22https://hub.tekton.dev/%22){.=3D\"link\"}, in
combination w= ith custom tasks and scripts.

::: 3D"titlepage"
<div>

<div>

### [3.1.7. Addition= al resources](3D%22https=){.3D\"anchor-heading :="" docs.redhat.com="" en="" documentation="" openshift_container_platform="" 4.10="" html="" =="" cicd="" migrating-from-jenkins-to-tekton#migrating-from-jenkins-to-tekton_sett="ing-up-trusted-ca\"" test-horse\"=""}= {#addition-al-resources .3D\"title\"}

::: {#3D\"container\" .3D\" style="3D\"\"" center="" \"=""}
::: {#3D\"invoker\"}
:::

::: {#3D\"tooltip\" .3D\" role="3D\"status\"" dark="" \"=""}
:::
:::

[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" ui="" \"=""}
[]{part="3D\"fallback\""}
:::

[]{aria-hidden="3D\"false\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTI5LjcyMSIgMi4yNzljLTM9Ii4wMzQtMy4wMzUtNy45Ny0zLjAzNC0xMS4wMDMiIDBsLTYuMTY1IDYuMTY0Yy0zLjAzNCAzLjAzNC0zLjAzNCA3Ljk3IDAgMTEuMDA9IjRhOC41MjUiIDguNTI1IDAgMCAwIDEuOTgyIDEuNDM4IDEgMSAwIDAgMCAuOTMtMS43NyA2LjUyNiA2LjUyNiAwIDAgMS0xLjQ5OC09IjEuMDgyIiA1Ljc4NyA1Ljc4NyAwIDAgMSAwLTguMTc2bDYuMTY1LTYuMTY0YzIuMjU0LTIuMjU1IDUuOTIyLTIuMjU0IDguMTc1IDA9InMyLjI1NCIgNS45MjEgMCA4LjE3NWwtMy40MDUgMy40MDVhMSAxIDAgMSAwIDEuNDE1IDEuNDE0bDMuNDA0LTMuNDA1YzMuMDM0LTM9Ii4wMzQiIDMuMDM0LTcuOTcgMC0xMS4wMDN6Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTcuNDY1IiAxMS4xMTVhMSAxIDAgMCAwLS45MyAxPSIuNzciIDYuNTcxIDYuNTcxIDAgMCAxIDEuNDk4IDEuMDgyIDUuNzg3IDUuNzg3IDAgMCAxIDAgOC4xNzVsLTYuMTY1IDYuMTY1YTUuPSI3ODciIDUuNzg3IDAgMCAxLTguMTc1IDAgNS43ODcgNS43ODcgMCAwIDEgMC04LjE3NWwzLjQwNC0zLjQwNWExIDEgMCAxIDAtMS40PSIxNC0xLjQxNEwyLjI4IiAxOC43MThjLTMuMDM0IDMuMDMzLTMuMDM0IDcuOTcgMCAxMS4wMDMgMS41MTYgMS41MTcgMy41MDkgMi4yPSI3NSIgNS41MDEgMi4yNzVzMy45ODUtLjc1OCA1LjUwMi0yLjI3NWw2LjE2NS02LjE2NWMzLjAzMy0zLjAzMyAzLjAzMy03Ljk3IDAtPSIxMS4wMDNhOC41MjUiIDguNTI1IDAgMCAwLTEuOTgyLTEuNDM4eiI+PC9wYXRoPjwvc3ZnPg==)
:::

::: {.3D\"section= slot="3D\"content\"" -link="" tooltip-content\"=""}
[Copy link]{.3D\"copy-link-text\"}
:::

</div>

</div>

::: 3D"itemizedlist"
-   [Role-based Access
    Control](3D%22https://access.redhat.com/documentation/en=){.3D\"link\"
    -us="" openshift_container_platform="" 4.10="" html-single=""
    authentication_and_author="ization/#using-rbac\""}
:::

Previous\<= /a\>

Next
:::
:::

::: {.3D\"page-layout-options\" v-c6b48c1e="3D\"\""}
\<= label for=3D\"page-format\" data-v-5cade871=3D\"\"\>FormatMulti-p=
ageSingle-pageView full doc as PDF
:::

Jum= p to section

[Back to
top](3D%22https://docs.redhat.com/en/documentation/=){part="3D\"trigger\""
openshift_container_platform="" 4.10="" html="" cicd=""
migrating-from-jenkins-to-tekto="n#\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTMwIiAyM2EuOTk3Ljk5Nz0iMCIgMCAxLS43MDctLjI5M2wxNiA5LjQxNCAyLjcwNyAyMi43MDdhMSAxIDAgMSAxLTEuNDE0LTEuNDE0bDE0LjkzOSA3LjY0N2ExLj0iNTAxIiAxLjUwMSAwIDAgMSAyLjEyMiAwbDEzLjY0NiAxMy42NDZhMSAxIDAgMCAxIDMwIDIzeiI+PC9wYXRoPjwvc3ZnPg==)
:::

Back to top

## Red Hat footer {#3D\"heading\"}

::: {.3D\"section part="3D\"section" header\"=""}
::: {.3D\"header-primary\" part="3D\"header-primary\""}
::: {.3D\"logo\" part="3D\"logo\""}
[![3D\"Red](3D%22https://static.redhat.c=){hat\"="" om="" libs=""
redhat="" brand-assets="" 2="" corp=""
logo--on-dark.svg\"=""}](3D%22https://docs.redhat.com/%22)
:::
:::

::: {.3D\"header-secondary\" part="3D\"header-secondary\""}
::: 3D"social-links"
::: {.3D\"header\" part="3D\"header\""}
:::

::: {.3D\"default\" part="3D\"default\""}
:::
:::
:::
:::

::: {.3D\"section part="3D\"section" main\"=""}
::: {.3D\"main-primary\" part="3D\"main-primary\""}
::: {.3D\"links\" part="3D\"links\""}
=20
:::
:::

::: {.3D\"main-secondary\" part="3D\"main-secondary\""}
:::
:::

[![3D\"Red](3D%22https://docs.redhat.com/Logo-Red_Hat-Do=){hat=""
logo\"="" cumentation-a-reverse-rgb.svg\"="" loading="3D\"lazy\""
width="3D\"222\"" height="3D\"40\"="
v-81a16915="3D\"\""}](3D%22https://docs.redhat.com/en%22){slot="3D\"logo\""
an="alytics-category=3D\"Footer\"" analytics-text="3D\"Logo\""
v-81a16915="3D=" \"\"=""}
[](3D%22https://docs.redhat.com/en/documentation/openshift_contain=){er_platform=""
4.10="" html="" cicd="" migrating-from-jenkins-to-tekton\"=""
aria-label="3D\"=" \"=""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" social="" \"=""}
[]{part="3D\"fallback\""}
:::

[](3D%22https://github.com/redhat-documentation%22){ana="lytics-region=3D\"social-links-exit\""
analytics-category="3D\"Footer|socia=" l-links\"=""
analytics-text="3D\"Github\"" v-81a16915="3D\"\"" aria-label="3D\"="
github\"=""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" social="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iPTNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAzMCAzMCI+PHBhdGggZD0iM0QmcXVvdDtNMTUiIDQuMjJhMT0iMS4wNSIgMTEuMDUgMCAwIDAtMy41IDIxLjU0Yy41Ni4xMS43Ni0uMjQuNzYtLjUzdi0xLjg4Yy0zLjA3LjY3LTMuNzItMS40OC0zLj0iNzItMS40OGEyLjkxIiAyLjkxIDAgMCAwLTEuMjMtMS42MmMtMS0uNjguMDgtLjY3LjA4LS42N2EyLjMyIDIuMzIgMCAwIDEgMS42OT0iMS4xNCIgMi4zNiAyLjM2IDAgMCAwIDMuMjIuOTIgMi4zOSAyLjM5IDAgMCAxIC43LTEuNDhjLTIuNDUtLjI4LTUtMS4yMy01LTUuPSI0NmE0LjMiIDQuMyAwIDAgMSAxLjEzLTMgNCA0IDAgMCAxIC4wNi0yLjlzLjkzLS4zIDMgMS4xNGExMC4yOSAxMC4yOSAwIDAgMSA1PSIuNTQiIDBjMi4xMS0xLjQ0IDMtMS4xNCAzLTEuMTRhNCA0IDAgMCAxIC4xMSAyLjkzIDQuMjUgNC4yNSAwIDAgMSAxLjEzIDNjMCA0PSIuMjQtMi41OCIgNS4xOC01LjA1IDUuNDVhMi42MyAyLjYzIDAgMCAxIC43NSAyLjA1djNjMCAuMzMuMi42NC43Ni41M2ExMS4wNSAxPSIxLjA1IiAwIDAgMCAxNSA0LjIyeiIgZmlsbC1ydWxlPSIzRCZxdW90O2V2ZW5vZGQmcXVvdDsiPjwvcGF0aD48L3N2Zz4=)
:::

Github[![3D\"reddit\"](3D=){\"data:image=""
svg+xml,%3csvg%20xmlns="3D'http://www.w3.org/2000/svg'%20data-ic="
on-name="3D'reddit'%20height=3D'512'%20width=3D'512'%20viewBox=3D'0%200%2051="
2%20512'%3e%3cpath%20fill="3D'rgb(163,163,163)'%20d=3D'M201.5%20305.5c-13.8%="
200-24.9-11.1-24.9-24.6%200-13.8%2011.1-24.9%2024.9-24.9%2013.6%200%2024.6%="2011.1%2024.6%2024.9%200%2013.6-11.1%2024.6-24.6%2024.6zM504%20256c0%20137-="
111%20248-248%20248s8%20393%208%20256%20119%208%20256%208s248%20111%20248%2="0248zm-132.3-41.2c-9.4%200-17.7%203.9-23.8%2010-22.4-15.5-52.6-25.5-86.1-26="
.6l17.4-78.3%2055.4%2012.5c0%2013.6%2011.1%2024.6%2024.6%2024.6%2013.8%200%="2024.9-11.3%2024.9-24.9s-11.1-24.9-24.9-24.9c-9.7%200-18%205.8-22.1%2013.8l="
-61.2-13.6c-3-.8-6.1%201.4-6.9%204.4l-19.1%2086.4c-33.2%201.4-63.1%2011.3-8="5.5%2026.8-6.1-6.4-14.7-10.2-24.1-10.2-34.9%200-46.3%2046.9-14.4%2062.8-1.1="
%205-1.7%2010.2-1.7%2015.5%200%2052.6%2059.2%2095.2%20132%2095.2%2073.1%200="%20132.3-42.6%20132.3-95.2%200-5.3-.6-10.8-1.9-15.8%2031.3-16%2019.8-62.5-1="
4.9-62.5zm302.8%20331c-18.2%2018.2-76.1%2017.9-93.6%200-2.2-2.2-6.1-2.2-8.3="%200-2.5%202.5-2.5%206.4%200%208.6%2022.8%2022.8%2087.3%2022.8%20110.2%200%="
202.5-2.2%202.5-6.1%200-8.6-2.2-2.2-6.1-2.2-8.3%200zm7.7-75c-13.6%200-24.6%="2011.1-24.6%2024.9%200%2013.6%2011.1%2024.6%2024.6%2024.6%2013.8%200%2024.9="
-11.1%2024.9-24.6%200-13.8-11-24.9-24.9-24.9z'="" %3e%3c="" svg%3e\"=""
width="3D\"20\"" =="" height="3D\"20\""
v-81a16915="3D\"\""}]{.3D\"reddit-span\" slot="3D\"so=" cial-links\"=""
role="3D\"listitem\"" v-81a16915="3D\"\""}
[](3D%22https://docs.redhat.com/en/documentation/openshift_contain=){er_platform=""
4.10="" html="" cicd="" migrating-from-jenkins-to-tekton\"=""
aria-label="3D\"=" \"=""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" social="" \"=""}
[]{part="3D\"fallback\""}
:::

[](3D%22https://www.youtube.com/@redhat%22){analytics-r="egion=3D\"social-links-exit\""
analytics-category="3D\"Footer|social-links\"="
analytics-text="3D\"YouTube\"" v-81a16915="3D\"\""
aria-label="3D\"Youtube=" \"=""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" social="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iPTNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAzMCAzMCI+PHBhdGggZD0iM0QmcXVvdDtNMTIuNjgiIDE3Lj0iOTJWMTEuNmw2LjA3IiAzLjE3LTYuMDcgMy4xNXptMjYgMTAuNWE0LjgyIDQuODIgMCAwIDAtLjktMi4yMyAzLjIxIDMuMjEgMCAwPSIwLTIuMjUtLjk1QzE5LjczIiA3LjA5IDE1IDcuMDkgMTUgNy4wOXMtNC43MiAwLTcuODcuMjNhMy4yMSAzLjIxIDAgMCAwLTIuMjUuPSI5NUE0LjgyIiA0LjgyIDAgMCAwIDQgMTAuNWEzNC43NiAzNC43NiAwIDAgMC0uMjIgMy42NHYxLjcxYTM0Ljc2IDM0Ljc2IDAgMCAwPSI0IiAxOS40OWE0LjgyIDQuODIgMCAwIDAgLjkgMi4yMyAzLjc0IDMuNzQgMCAwIDAgMi40NyAxYzEuOC4xNyA3LjY1LjIzIDcuNjU9Ii4yM3M0LjczIiAwIDcuODctLjI0YTMuMTcgMy4xNyAwIDAgMCAyLjI1LTEgNC44MiA0LjgyIDAgMCAwIC45LTIuMjMgMzQuNzYgMzQ9Ii43NiIgMCAwIDAgLjIyLTMuNjR2LTEuN2EzNC43NiAzNC43NiAwIDAgMCAyNiAxMC41eiI+PC9wYXRoPjwvc3ZnPg==)
:::

Youtube
[=](3D%22https://docs.redhat.com/en/documentation/openshift_contain=){er_platform=""
4.10="" html="" cicd="" migrating-from-jenkins-to-tekton\"=""
aria-label="3D\"=" \"=""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"false\"" social="" \"=""}
[]{part="3D\"fallback\""}
:::

[](3D%22https://twitter.com/RedHat%22){analytics-region="=3D\"social-links-exit\""
analytics-category="3D\"Footer|social-links\""
data="-analytics-text=3D\"Twitter\"" v-81a16915="3D\"\""
aria-label="3D\"Twitter\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" social="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iPTNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAzMCAzMCI+PHBhdGggZD0iM0QmcXVvdDttMTYuNzgiIDEzLj0iNTQiIDYuOTYtOC4wOWgtMS42NWwtNi4wNCA3LjAyLTQuODItNy4wMmg1LjY3bDcuMyAxMC42Mi03LjMgOC40OGgxLjY1bDYuMzgtNz0iLjQyIiA1LjEgNy40Mmg1LjU2bC03LjU3LTExLjAxem0tMi4yNiAyLjYyLS43NC0xLjA2bDcuOSA2LjY5aDIuNTNsNC43NSA2Ljc5Lj0iNzQiIDEuMDYgNi4xNyA4LjgzaC0yLjUzbC01LjAzLTcuMnoiPjwvcGF0aD48L3N2Zz4=)
:::

Twitter

### Learn {#3D\"rh-footer-yq75= slot="3D\"lin=" ks\"="" analytics-text="3D\"Learn\"" v-81a16915="3D\"\"" aq4an\"=""}

-   [Developer resources](3D%22https://developer=){s.redhat.com=""
    learn\"="" analytics-category="3D\"Footer|Learn\""
    analytics="-text=3D\"Developer" resources\"=""
    v-81a16915="3D\"\""}\<= /li\>
-   [Cloud learning
    hub](3D%22https://cloud.redhat.com/learn%22){dat="a-analytics-category=3D\"Footer|Learn\""
    analytics-text="3D\"Cloud" learning="hub\"" v-81a16915="3D\"\""}
-   [Interactive
    labs](3D%22https://www.redhat.com/en/interactive-labs%22){analytics="-category=3D\"Footer|Learn\""
    analytics-text="3D\"Interactive" labs\"="" v-="81a16915=3D\"\""}
-   [Training and certification](3D%22=){https:="" www.redhat.com=""
    services="" training-and-certification\"=""
    analytics-="category=3D\"Footer|Learn\""
    analytics-text="3D\"Training" and=""
    certification=" data-v-81a16915=3D" \"=""}
-   [Customer
    support](3D%22https://access.redhat.com/support%22){analytics-catego="ry=3D\"Footer|Learn\""
    analytics-text="3D\"Customer" support\"="" v-81a1691="5=3D\"\""}
-   [See all documen= tation](3D%22https:/=){docs.redhat.com=""
    products\"="" analytics-category="3D\"Footer|Learn\""
    an="alytics-text=3D\"See" all="" documentation\"=""
    v-81a16915="3D\"\""}

### Try, buy, & sell {#3D\"rh-footer-1w3euv7md\" slot="3D\"links\"" analytics-text="3D\"Try" buy="" sell\"="data-v-81a16915=3D\"\""}

\<= ul slot=3D\"links\" data-v-81a16915=3D\"\"
aria-labelledby=3D\"rh-footer-1w3euv7= md\"\>

[Product trial
center](3D%22https://redhat.com/en/products/tria=){ls\"=""
analytics-category="3D\"Footer|Try" buy="" sell\"=""
analytics-text="3D\"=" product="" trial="" center\"=""
v-81a16915="3D\"\""}

[Red Hat Ecosystem
Catalog](3D%22https://catalog.redhat.com/%22){analytic="s-category=3D\"Footer|Try"
buy="" sell\"="" analytics-text="3D\"Red" hat="" ecosystem="Catalog\""
v-81a16915="3D\"\""}

[Red Hat
Store](3D%22https://www.redhat.com/en/store%22){analyt="ics-category=3D\"Footer|Try"
buy="" sell\"="" analytics-text="3D\"Red" hat=""
store\"="data-v-81a16915=3D\"\""}

Buy online (Japan)

### Comm= unities {#3D\"rh-footer-igjxw3n8f\" slot="3D\"links\"" analytic="s-text=3D\"Communities\"" v-81a16915="3D\"\""}

-   [Customer Portal C= ommunity](3D%22https://access.redhat.=){com=""
    analytics-category="3D\"Footer|Communities\""
    analytic="s-text=3D\"Customer" portal="" community\"=""
    v-81a16915="3D\"\""}
-   [Events](3D%22https://www.redhat.com=){events\"=""
    analytics-category="3D\"Footer|Communities\""
    analytics-text="=3D\"Events\"" v-81a16915="3D\"\""}
-   How we contribute

=

::: {.3D\"base\" part="3D\"base\""}
::: {.3D\"header\" part="3D\"header\""}
:::

::: {.3D\"content\" part="3D\"content\""}
:::
:::

### About Red Hat Documentation {#about-red-hat-documentation slot="3D\"header\"" analytics-text="3D\"About" red="" hat="" doc="umentation\"" v-81a16915="3D\"\""}

We help Red Hat users innovate and achieve their go= als with our
products and services with content they can trust. [Explore our recent
updates](3D%22=){https:="" www.redhat.com="" en="" blog=""
whats-new-docsredhatcom\"="" analytics-cate="gory=3D\"Footer|About"
red="" hat="" documentation\"="" analytics-text="3D\"Explore" ==""
our="" recent="" updates\"="" v-81a16915="3D\"\""}.

::: {.3D\"base\" part="3D\"base\""}
::: {.3D\"header\" part="3D\"header\""}
:::

::: {.3D\"content\" part="3D\"content\""}
:::
:::

### Making open source more inclusive {#making-open-source-more-inclusive slot="3D\"header\"" analytics-text="3D\"Making" open="" sourc="e" more="" inclusive\"="" v-81a16915="3D\"\""}

Red Hat is committed to replacing problemati= c language in our code,
documentation, and web properties. For more details= , see the [Red Hat
Blog](3D%22https://www.redhat.com/en/blog/making-open-source-more=){-inclusive-eradicating-problematic-language\"=""
analytics-category="3D\"Foo=" ter|making="" open="" source="" more=""
inclusive\"="" analytics-text="3D\"Red" hat=""
blog\"="data-v-81a16915=3D\"\""}.

::: {.3D\"base\" part="3D\"base\""}
::: {.3D\"header\" part="3D\"header\""}
:::

::: {.3D\"content\" part="3D\"content\""}
:::
:::

### About Red Hat {#about-red-hat slot="3D\"header\"" analytics-text="3D\"About" red="" hat\"="" da="ta-v-81a16915=3D\"\""}

We delive= r hardened solutions that make it easier for enterprises to
work across pla= tforms and environments, from the core datacenter to
the network edge.

\<= /rh-footer-block\>

::: {.3D\"base\" part="3D\"base\""}
::: {.3D\"header\" part="3D\"header\""}
:::

::: {.3D\"content\" part="3D\"content\""}
:::
:::

### Theme {#theme slot="3D\"header\"" analytics-text="3D\"Theme\"" v-81a="16915=3D\"\""}

::: {.3D\"theme-container\" v-81a16915="3D\"\"" da="ta-v-9af16c28=3D\"\""}
[ ]{aria-hidden="3D\"true\""}

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" ui="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodD0iIHRwOiB3d3cudzMub3JnIDIwMDAgc3ZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgMzIgMzIiPjxwYXRoIGQ9IjNEJnF1b3Q7TTIzLjk0IiAxNmExIDEgMD0iMCIgMS0uOTkyLS44NzYgNi45NTcgNi45NTcgMCAwIDAtNi4wNjktNi4wNjIgMSAxIDAgMSAxIC4yNDItMS45ODUgOC45NTMgOC45NT0iMyIgMCAwIDEgNy44MTIgNy44YS45OTkuOTk5IDAgMCAxIDIzLjk0IDE2em0xNiA1YTEgMSAwIDAgMS0xLTF2MWExIDEgMCAxIDEgMj0iMHYzYTEiIDEgMCAwIDEtMSAxem0wIDI3YTEgMSAwIDAgMS0xLTF2LTNhMSAxIDAgMSAxIDIgMHYzYTEgMSAwIDAgMS0xIDF6bTQ9IjE3SDFhMSIgMSAwIDEgMSAwLTJoM2ExIDEgMCAxIDEgMCAyem0yNyAwaC0zYTEgMSAwIDEgMSAwLTJoM2ExIDEgMCAxIDEgMCAyem09IjUuMzk0IiAyNy42MDZhMSAxIDAgMCAxLS43MDctMS43MDdsMi4xMi0yLjEyYTEgMSAwIDEgMSAxLjQxNSAxLjQxM2w2LjEgMjcuMzE9IjNhLjk5Ny45OTciIDAgMCAxLS43MDcuMjkzem0yNC40ODUgOC41MTVhMSAxIDAgMCAxLS43MDctMS43MDdsMjUuOSA0LjY4NmExIDE9IjAiIDEgMSAxLjQxNSAxLjQxNWwtMi4xMjIgMi4xMmEuOTk3Ljk5NyAwIDAgMS0uNzA3LjI5NHptLTE2Ljk3IDBhLjk5Ny45OTcgMD0iMCIgMS0uNzA3LS4yOTNsNC42ODYgNi4xYTEgMSAwIDEgMSAxLjQxNS0xLjQxNWwyLjEyIDIuMTIyYTEgMSAwIDAgMS0uNzA2IDEuPSI3MDdabTE5LjA5MSIgMTkuMDkxYS45OTcuOTk3IDAgMCAxLS43MDctLjI5M2wtMi4xMi0yLjEyYTEgMSAwIDEgMSAxLjQxMy0xLjQxPSI1bDIuMTIyIiAyLjEyMWExIDEgMCAwIDEtLjcwNyAxLjcwN3ptMTYgMjQuODc1Yy00Ljg5NCAwLTguODc1LTMuOTgxLTguODc1LTguPSI4NzVhOC44NzkiIDguODc5IDAgMCAxIDUuMjI3LTguMDg4Ljg3Ni44NzYgMCAwIDEgMS4xNTMgMS4xNjMgNi45NDUgNi45NDUgMCAwPSIwLS42MyIgMi45MjVhNy4xMzMgNy4xMzMgMCAwIDAgMjAgMTkuMTI1YTYuOTQ4IDYuOTQ4IDAgMCAwIDIuOTI1LS42My44NzYuODc9IjYiIDAgMCAxIDEuMTYzIDEuMTU0YTguODggOC44OCAwIDAgMSAxNiAyNC44NzV6bS00Ljc4NS0xNC4xNTNhNy4xMzUgNy4xMzUgMD0iMCIgMCA4Ljg3NSAxNiA3LjEzMyA3LjEzMyAwIDAgMCAxNiAyMy4xMjVhNy4xMyA3LjEzIDAgMCAwIDUuMjc4LTIuMzRjLS40MTkuMD0iNi0uODQ1LjA5LTEuMjc4LjA5LTQuODk0IiAwLTguODc1LTMuOTgxLTguODc1LTguODc1IDAtLjQzMy4wMy0uODYuMDktMS4yNzh6Ij48L3BhdGg+PC9zdmc+)
:::

[]{aria-hidden="3D\"true\""}

System default

::: {#3D\"container\" .3D\" aria-hidden="3D\"true\"" microns="" \"=""}
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iPTNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiIHZpZXdib3g9IjNEJnF1b3Q7MCIgMCAyMCAyMCI+PHBhdGggZD0iM0QmcXVvdDtNMTguOTIiIDUuNj0iMkMxOC43NyIgNS4yNSAxOC40IDUgMTggNWgyYTEuMDAzIDEuMDAzIDAgMCAwLS43MSAxLjcxbDcuNjUgNy42NWMuMjkuMjkuNjguND0iNCIgMS4wNi40NHMuNzctLjE1IDEuMDYtLjQ0bDcuNjUtNy42NWMuMjktLjI5LjM3LS43Mi4yMi0xLjA5eiI+PC9wYXRoPjwvc3ZnPg==)
:::
:::

=20

::: {.3D\"section part="3D\"section" base\"="" global-base="" \"=""}
::: {.3D\"global-logo\" part="3D\"logo\""}
[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iM0QmcXVvdDtnbG9iYWwtbG9nby1pbWFnZSZxdW90OyIgcGFydD0iM0QmcXVvdDtsb2dvLWltYWdlJnF1b3Q7IiBkYXRhPSItbmFtZT0zRCZxdW90O0xheWVyIiAxIiB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmlld2JveD0iM0QmcXVvdDswIiAwIDE5MiAxPSI0NSZxdW90OyI+CiAgICAgICAgICAgICAgICAgICAgICA8dGl0bGU+UmVkIEhhdCBsb2dvPC90aXRsZT4KICAgICAgICAgICAgICAgICAgICA8ZGVmcz4KICAgICAgICAgICAgICAgICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgICAgICAgICAgICAgLmJhbmQgewogICAgICAgICAgICAgICAgICAgICAgICAgIGZpbGw6IHRyYW5zcGFyZW50OwogICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICA8L3N0eWxlPgogICAgICAgICAgICAgICAgICAgIDwvZGVmcz4KICAgICAgICAgICAgICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtiYW5kJnF1b3Q7IiBkPSIzRCZxdW90O00xNTcuNzcsNjIuNjFhMTQsMTQsMCwwLDEsLjMxPSIgLDMuNDJjMCwxNC44OC0xOC4xLDE3LjQ2LTMwLjYxLDE3LjQ2Yzc4LjgzLDgzLjQ5LDQyLjUzLDUzLjI2LDQyLjUzLDQ0YTYuNDMsPSI2LjQzLDAsMCwxLC4yMi0xLjk0bC0zLjY2LDkuMDZhMTguNDUsMTguNDUsMCwwLDAtMS41MSw3LjMzYzAsMTguMTEsNDEsNDUuNDg9IiAsODcuNzQsNDUuNDgsMjAuNjksMCwzNi40My03Ljc2LDM2LjQzLTIxLjc3LDAtMS4wOCwwLTEuOTQtMS43My0xMC4xM3oiPjwvcGE9PgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O2Nscy0xJnF1b3Q7IiBkPSIzRCZxdW90O00xMjcuNDcsODMuNDljMTIuNTEsMCwzMC42MS09IiAyLjU4LDMwLjYxLTE3LjQ2YTE0LDE0LDAsMCwwLS4zMS0zLjQybC03LjQ1LTMyLjM2Yy0xLjcyLTcuMTItMy4yMy0xMC4zNS0xNS49IjczLTE2LjZDMTI0Ljg5LDguNjksMTAzLjc2LjUsOTcuNTEuNSw5MS42OS41LDkwLDgsODMuMDYsOGMtNi42OCwwLTExLjY0LTUuNj0iIC0xNy44OS01LjYtNiwwLTkuOTEsNC4wOS0xMi45MywxMi41LDAsMC04LjQxLDIzLjcyLTkuNDksMjcuMTZhNi40Myw2LjQzLDAsMD0iLDAsNDIuNTMsNDRjMCw5LjIyLDM2LjMsMzkuNDUsODQuOTQsMzkuNDVNMTYwLDcyLjA3YzEuNzMsOC4xOSwxLjczLDkuMDUsMS43PSIgMywxMC4xMywwLDE0LTE1Ljc0LDIxLjc3LTM2LjQzLDIxLjc3Yzc4LjU0LDEwNCwzNy41OCw3Ni42LDM3LjU4LDU4LjQ5YTE4LjQ1PSIsMTguNDUsMCwwLDEsMS41MS03LjMzQzIyLjI3LDUyLC41LDU1LC41LDc0LjIyYzAsMzEuNDgsNzQuNTksNzAuMjgsMTMzLjY1LDc9IiAwLjI4LDQ1LjI4LDAsNTYuNy0yMC40OCw1Ni43LTM2LjY1LDAtMTIuNzItMTEtMjcuMTYtMzAuODMtMzUuNzgiPjwvcGF0aD4KICAgICAgICAgICAgICAgICAgPC9zdmc+){.3D\"global-logo-image\"}](=3D%22https://redhat.com/%22){.3D\"global-logo-anchor\"
part="3D\"logo-anchor\"" aria-label="3D\"Visit" red="" hat\"=""}
:::

::: {.3D\"global-primary\" part="3D\"primary\""}
=20

::: {.3D\"global-links-primary\" part="3D\"links-primary\""}
:::

=20
:::

::: {.3D\"spacer\" part="3D\"spacer\""}
:::

::: {.3D\"global-secondary\" part="3D\"secondary\""}
=20

::: {.3D\"global-links-secondary\" part="3D\"links-seconda=" ry\"=""}
:::

=20
:::

=20
:::

-   [About Red Hat](3D%22https://redhat.com/en/about/compa=){ny\"=""
    analytics-category="3D\"Footer|Corporate\""
    analytics-text="3D\"Abo=" ut="" red="" hat\"="" v-81a16915="3D\"\""}
-   Jobs
-   [Events](3D%22https://redhat.com/en/events%22){da="ta-analytics-category=3D\"Footer|Corporate\""
    analytics-text="3D\"Events\"" d="ata-v-81a16915=3D\"\""}
-   [Location= s](3D%22http=){s:="" redhat.com="" en="" about=""
    office-locations\"="" analytics-category="3D\"Footer="
    |corporate\"="" analytics-text="3D\"Locations\""
    v-81a16915="3D\"\""}
-   [Contact Red Hat](3D%22https://redhat.com/en/contact=){\"=""
    analytics-category="3D\"Footer|Corporate\""
    analytics-text="3D\"Conta=" ct="" red="" hat\"=""
    v-81a16915="3D\"\""}
-   [Red Hat
    Blog](3D%22https://redhat.com/en/blog%22){analytics-category="=3D\"Footer|Corporate\""
    analytics-text="3D\"Red" hat="" blog\"="" v-81a16915="=3D\"\""}
-   [Inclusion at Red Hat](3D%22https:/=){redhat.com="" en="" about=""
    our-culture="" diversity-equity-inclusion\"=""
    analytics="-category=3D\"Footer|Corporate\""
    analytics-text="3D\"Diversity" equity="" and="inclusion\""
    v-81a16915="3D\"\""}
-   [Cool Stuff
    Store](3D%22https://coolstuff.redhat.com/%22){analytics-ca="tegory=3D\"Footer|Corporate\""
    analytics-text="3D\"Cool" stuff="" store\"="" v="-81a16915=3D\"\""}
-   [Red H= at Summit](3D=){\"https:="" www.redhat.com="" en=""
    analytics-category="3D\"Footer|Corpor=" ate\"=""
    analytics-text="3D\"Red" hat="" summit\"="" v-81a16915="3D\"\""}

::: {.3D\"status-legal\" v-5f538988="3D\"\"" slo="t=3D\"links-secondary\"" v-if="3D\"true\""}
[[All systems operational]{.3D\"status-description\" v-5f538988="3D\"\""
js="3D\"st=" atus-description\"=""}[]{.3D\"current-status-indicator
v-5f538988="3D\"\"" =="" status-icon="" status-dot="" status-good\"=""
="js=3D\"status-icon\""}](3D%22https:/=){.3D\"status-page-widget\"
v-5f538988="3D\"\"" status.redhat.com="" \"="" js="3D\"status-page-wi="
dget\"=""}
:::

=C2= =A9 2025 Red Hat, Inc.=C2=A9 2025 R= ed Hat

-   [Privacy statement](3D%22https://redhat=){.com="" en="" about=""
    privacy-policy\"="" analytics-category="3D\"Footer|Red" hat=""
    leg="al" and="" privacy="" links\"="" analytics-text="3D\"Privacy"
    statement\"="" v-81a1="6915=3D\"\""}
-   [Terms of use](3D%22htt=){ps:="" redhat.com="" en="" about=""
    terms-use\"="" analytics-category="3D\"Footer|Red" h="at" legal=""
    and="" privacy="" links\"="" analytics-text="3D\"Terms" of=""
    use\"="" v-81a="16915=3D\"\""}
-   [All policies and guidelines](3D%22https:/=){redhat.com="" en=""
    about="" all-policies-guidelines\"="" analytics-category="3D\"Fo="
    oter|red="" hat="" legal="" and="" privacy="" links\"=""
    analytics-text="3D\"All" policies="" a="nd" guidelines\"=""
    v-81a16915="3D\"\""}
-   [[Cookie preferences]{#3D\"icon-id07849808917898049\"
    .3D\"truste_cursor_point= role="3D\"link\"" ta="bindex=3D\"0\""
    lang="3D\"en\"" aria-haspopup="3D\"dialog\"" aria-label="3D\"Cookie"
    pref="erences," opens="" a="" dedicated="" popup="" modal=""
    window\"="" er\"=""}]{#=3D\"teconsent\" v-81a16915="3D\"\""
    consent="3D\"0,1,2\"" aria-label="3D\"Open" co="okie" preferences=""
    modal\"=""}

::: {#3D\"consent_blackbar\" style="3D\"position:fixed;bottom:0;width:100%;=" z-index:5;padding:10px;\"=""}
:::

::: {#3D\"teleports\"}
=
:::

::: {role="3D\"status\"" style="3D\"position:" fixed;="" inset-block-start:="" inse="t-inline-start:" 0px;="" overflow:="" hidden;="" clip:="" rect(0px,="" 0px,="" 0px);="" whit="e-space:" nowrap;="" border:="" 0px;\"=""}
:::

\<= /iframe\>

::: {#3D\"ZN_bCxD2jjWRr4bfVQ\"}
:::

\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: image/svg+xml Content-Transfer-Encoding: quoted-printable
Content-Location:
https://static.redhat.com/libs/redhat/brand-assets/2/corp/logo\--on-dark.svg
![](data:image/svg+xml;base64,PHN2ZyBpZD0iM0QmcXVvdDtMYXllcl8xJnF1b3Q7IiBkYXRhLW5hbWU9IjNEJnF1b3Q7TGF5ZXIiIDEiIHhtbG5zPSIzRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvcz0iIHZnIiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgNjEzIDE0NSI+PGRlZnM+PHN0eWxlPi5jbHMtMXtmaWxsOiNlMDA7fS5jbHMtMntmaWxsOiNmZmY9Cjt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPlJlZEhhdC1Mb2dvLUEtUmV2ZXJzZTwvdGl0bGU+PHBhdGggY2xhc3M9IjNEJnF1b3Q7Y2xzLTEmcXVvdDsiID0gZD0iM0QmcXVvdDtNMTI3LjQ3LDgzLjQ5YzEyLjUxLDAsMzAuNjEtMi41OCwzMC42MS0xNy40NmExNCwxNCwwLDAsMC0uMzEtMy40MmwtNy40PSIgNS0zMi4zNmMtMS43Mi03LjEyLTMuMjMtMTAuMzUtMTUuNzMtMTYuNmMxMjQuODksOC42OSwxMDMuNzYuNSw5Ny41MS41LDkxLjY5PSIuNSw5MCw4LDgzLjA2LDhjLTYuNjgsMC0xMS42NC01LjYtMTcuODktNS42LTYsMC05LjkxLDQuMDktMTIuOTMsMTIuNSwwLDAtOC49IiA0MSwyMy43Mi05LjQ5LDI3LjE2YTYuNDMsNi40MywwLDAsMCw0Mi41Myw0NGMwLDkuMjIsMzYuMywzOS40NSw4NC45NCwzOS40NW09IjE2MCw3Mi4wN2MxLjczLDguMTksMS43Myw5LjA1LDEuNzMsMTAuMTMsMCwxNC0xNS43NCwyMS43Ny0zNi40MywyMS43N0M3OC41ND0iICwxMDQsMzcuNTgsNzYuNiwzNy41OCw1OC40OWExOC40NSwxOC40NSwwLDAsMSwxLjUxLTcuMzNjMjIuMjcsNTIsLjUsNTUsLjUsNz0iNC4yMmMwLDMxLjQ4LDc0LjU5LDcwLjI4LDEzMy42NSw3MC4yOCw0NS4yOCwwLDU2LjctMjAuNDgsNTYuNy0zNi42NSwwLTEyLjcyPSIgLTExLTI3LjE2LTMwLjgzLTM1Ljc4Ij48L3BhdGg+PHBhdGggZD0iM0QmcXVvdDtNMTYwLDcyLjA3YzEuNzMsOC4xOSwxLjczLDkuMDUsMS43MywxMC4xPSIgMywwLDE0LTE1Ljc0LDIxLjc3LTM2LjQzLDIxLjc3Yzc4LjU0LDEwNCwzNy41OCw3Ni42LDM3LjU4LDU4LjQ5YTE4LjQ1LDE4LjQ1PSIsMCwwLDEsMS41MS03LjMzbDMuNjYtOS4wNkE2LjQzLDYuNDMsMCwwLDAsNDIuNTMsNDRjMCw5LjIyLDM2LjMsMzkuNDUsODQuOTQ9IiAsMzkuNDUsMTIuNTEsMCwzMC42MS0yLjU4LDMwLjYxLTE3LjQ2YTE0LDE0LDAsMCwwLS4zMS0zLjQyeiI+PC9wYXRoPjxwYXRoIGNsYXNzPSI9M0QmcXVvdDtjbHMtMiZxdW90OyIgZD0iM0QmcXVvdDtNNTc5Ljc0LDkyLjhjMCwxMS44OSw3LjE1LDE3LjY3LDIwLjE5LDE3LjY3YTUyLjExLDUyLjExLDAsMD0iICwwLDExLjg5LTEuNjh2OTVhMjQuODQsMjQuODQsMCwwLDEtNy42OCwxLjE2Yy01LjM3LDAtNy4zNi0xLjY4LTcuMzYtNi43M3Y2OD0iLjNoMTUuNTZWNTQuMUg1OTYuNzh2LTE4bC0xNywzLjY4VjU0LjFINTY4LjQ5VjY4LjNoMTEuMjVabS01MywuMzJjMC0zLjY4LDMuPSIgNjktNS40Nyw5LjI2LTUuNDdhNDMuMTIsNDMuMTIsMCwwLDEsMTAuMSwxLjI2djcuMTVhMjEuNTEsMjEuNTEsMCwwLDEtMTAuNjMsPSIyLjYzYy01LjQ2LDAtOC43My0yLjEtOC43My01LjU3bTUuMiwxNy41NmM2LDAsMTAuODQtMS4yNiwxNS4zNi00LjMxdjMuMzdoMTY9IiAuODJ2NzQuMDhjMC0xMy41Ni05LjE0LTIxLTI0LjM5LTIxLTguNTIsMC0xNi45NCwyLTI2LDYuMWw2LjEsMTIuNTJjNi41Mi0yLjc9IjQsMTItNC40MiwxNi44My00LjQyLDcsMCwxMC42MiwyLjczLDEwLjYyLDguMzF2Mi43M2E0OS41Myw0OS41MywwLDAsMC0xMi42Mj0iIC0xLjU4Yy0xNC4zMSwwLTIyLjkzLDYtMjIuOTMsMTYuNzMsMCw5Ljc4LDcuNzgsMTcuMjQsMjAuMTksMTcuMjRtLTkyLjQ0LS45ND0iaDE4LjA5VjgwLjkyaDMwLjI5djI4LjgySDUwNlYzNi4xMkg0ODcuOTNWNjQuNDFINDU3LjY0VjM2LjEySDQzOS41NVpNMzcwLjYyPSIgLDgxLjg3YzAtOCw2LjMxLTE0LjEsMTQuNjItMTQuMWExNy4yMiwxNy4yMiwwLDAsMSwzOTcsNzIuMDl2OTEuNTRhMTYuMzYsMTYuPSIzNiwwLDAsMSwzODUuMjQsOTZjLTguMiwwLTE0LjYyLTYuMS0xNC42Mi0xNC4wOW0yNi42MSwyNy44N2gxNi44M1YzMi40NGwtMTc9IiAsMy42OHY1Ny4wNWEyOC4zLDI4LjMsMCwwLDAtMTQuMi0zLjY4Yy0xNi4xOSwwLTI4LjkyLDEyLjUxLTI4LjkyLDI4LjVhMjguMjU9IiwyOC4yNSwwLDAsMCwyOC40LDI4LjYsMjUuMTIsMjUuMTIsMCwwLDAsMTQuOTMtNC44M1pNMzIwLDY3YzUuMzYsMCw5Ljg4LDMuND0iIDcsMTEuNjcsOC44M2gzMDguNDdjMzEwLjE1LDcwLjMsMzE0LjM2LDY3LDMyMCw2N20yOTEuMzMsODJjMCwxNi4yLDEzLjI1LDI4Lj0iODIsMzAuMjgsMjguODIsOS4zNiwwLDE2LjItMi41MywyMy4yNS04LjQybC0xMS4yNi0xMGMtMi42MywyLjc0LTYuNTIsNC4yMS0xPSIgMS4xNCw0LjIxYTE0LjM5LDE0LjM5LDAsMCwxLTEzLjY4LTguODNoMzkuNjV2ODMuNTVjMC0xNy42Ny0xMS44OC0zMC4zOS0yOC4wPSI4LTMwLjM5YTI4LjU3LDI4LjU3LDAsMCwwLTI5LDI4LjgxTTI2Miw1MS41OGM2LDAsOS4zNiwzLjc4LDkuMzYsOC4zMVMyNjgsNjg9IiAuMiwyNjIsNjguMmgyNDQuMTF2NTEuNTh6bS0zNiw1OC4xNmgxOC4wOXY4Mi45MmgxMy43N2wxMy44OSwyNi44MmgyOTJsLTE2LjI9Ii0yOS40NWEyMi4yNywyMi4yNywwLDAsMCwxMy44OC0yMC43MmMwLTEzLjI1LTEwLjQxLTIzLjQ1LTI2LTIzLjQ1SDIyNlomcXVvdDsvIj48IS0tPQpzdmctLT4KLS0tLS0tTXVsdGlwYXJ0Qm91bmRhcnktLXp4ZnkxY1k3RjJSWjhGZ3JnaEFCdERVaENoS2c0MDFzTUhvUFEwdkRFTC0tLS0KQ29udGVudC1UeXBlOiBpbWFnZS9zdmcreG1sCkNvbnRlbnQtVHJhbnNmZXItRW5jb2Rpbmc6IHF1b3RlZC1wcmludGFibGUKQ29udGVudC1Mb2NhdGlvbjogaHR0cHM6Ly9kb2NzLnJlZGhhdC5jb20vTG9nby1SZWRfSGF0LURvY3VtZW50YXRpb24tQS1SZXZlcnNlLVJHQi5zdmcKCjw/eG1sIHZlcnNpb249IjNEJnF1b3Q7MS4wJnF1b3Q7IiBlbmNvZGluZz0iM0QmcXVvdDt1dGYtOCZxdW90OyIgPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDI3LjkuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246PQogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgdmVyc2lvbj0iM0QmcXVvdDsxLjEmcXVvdDsiIGlkPSIzRCZxdW90O1R3b19saW5lcyZxdW90OyIgeG1sbnM9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcmcXVvdDsiID0geG1sbnM6eGxpbms9IjNEJnF1b3Q7aHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayZxdW90OyIgeD0iM0QmcXVvdDswcHgmcXVvdDsiIHk9IjNEJnF1b3Q7MHB4JnF1b3Q7IiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgOTAxLjcgMTYyLjYiIHN0eWxlPSIzRCZxdW90O2VuYWJsZS1iYWNrZ3JvdW5kOm5ldyIgMCAwIDkwMS43IDE2Mi49IjY7JnF1b3Q7IiB4bWw6c3BhY2U9IjNEJnF1b3Q7cHJlc2VydmUmcXVvdDsiPgo8c3R5bGUgdHlwZT0iM0QmcXVvdDt0ZXh0L2NzcyZxdW90OyI+CiAgICAuc3Qwe2ZpbGw6I0ZGRkZGRjt9CiAgICAuc3Qxe2ZpbGw6I0VFMDAwMDt9Cjwvc3R5bGU+CjxnIGlkPSIzRCZxdW90O1R3b19saW5lX2xvZ28mcXVvdDsiPgogICAgPGc+CiAgICAgICAgPHBhdGggY2xhc3M9IjNEJnF1b3Q7c3QwJnF1b3Q7IiBkPSIzRCZxdW90O00zMTguNiw2NS4ydi01NmgyNS40YzIuOSwwLDUuNSwwLjQsNy44LDEuM2MyLjMsMD0iIC45LDQuMywyLDUuOSwzLjVjMS42LDEuNSwyLjgsMy4yLDMuNyw1LjIgYzAuOSwyLDEuMyw0LjIsMS4zLDYuNmMwLDMuNi0xLDYuOC0zLjEsOS41Yy0yLjEsMi43LTQuOSw0LjctOC40LDUuOGwxMi41PSIsMjQuMWgtOS4zbC0xMS42LTIzSDMyN3YyM0gzMTguNnoiIG0zNDMuMywxNi42aDMyNyB2MTguN2gxNi4zYzMuNSwwLDYuMi0wLjksOC4xLTIuN2MxLjktMS44LDIuOC00LDIuOC02LjZjMC0yLjYtMC45LTQuOC0yLjg9Ii02LjZDMzQ5LjYsMTcuNSwzNDYuOSwxNi42LDM0My4zLDE2LjZ6JnF1b3Q7LyI+CiAgICAgICAgPHBhdGggY2xhc3M9IjNEJnF1b3Q7c3QwJnF1b3Q7IiBkPSIzRCZxdW90O00zNjYuMSw0NC44YzAtMi45LDAuNS01LjYsMS42LTguMnMyLjUtNC44LDQuMy02Lj0iIDdjMS44LTEuOSw0LTMuNCw2LjUtNC41YzIuNS0xLjEsNS4yLTEuNiw4LTEuNiBjMi44LDAsNS40LDAuNSw3LjgsMS42YzIuNCwxLjEsNC41LDIuNiw2LjIsNC41YzEuNywxLjksMy4xLDQuMSw0LjEsNi44YzE9IiwyLjYsMS41LDUuNCwxLjUsOC40djIuM0gzNzRjMC41LDMuNCwyLjEsNi4xLDQuNiw4LjQiIGMyLjYsMi4yLDUuNiwzLjMsOS4xLDMuM2MyLDAsMy45LTAuMyw1LjctMWMxLjgtMC42LDMuNC0xLjUsNC42LTIuNmw1LjEsNT0iYy0yLjQsMS45LTQuOSwzLjItNy40LDQuMWMtMi41LDAuOS01LjMsMS4zLTguNCwxLjMiIGMtMywwLTUuOC0wLjUtOC40LTEuNmMtMi42LTEuMS00LjktMi42LTYuOC00LjRjLTEuOS0xLjktMy40LTQuMS00LjUtNi43Yz0iMzY2LjYsNTAuNiwzNjYuMSw0Ny44LDM2Ni4xLDQ0Ljh6IiBtMzg2LjMsMzAuNiBjLTMuMSwwLTUuOCwxLTgsM2MtMi4yLDItMy43LDQuNi00LjIsNy44aDI0LjJjLTAuNS0zLjEtMS45LTUuNy00LjItNy44YzM9IjkxLjgsMzEuNiwzODkuMiwzMC42LDM4Ni4zLDMwLjZ6JnF1b3Q7LyI+CiAgICAgICAgPHBhdGggY2xhc3M9IjNEJnF1b3Q7c3QwJnF1b3Q7IiBkPSIzRCZxdW90O000NDUuMSw2NS4ydi0zLjhjLTEuNywxLjQtMy42LDIuNS01LjgsMy4zYy0yLjEsMD0iIC44LTQuNCwxLjItNi43LDEuMmMtMi45LDAtNS42LTAuNS04LjEtMS42IGMtMi41LTEuMS00LjctMi42LTYuNS00LjVjLTEuOC0xLjktMy4zLTQuMS00LjQtNi43Yy0xLjEtMi42LTEuNi01LjMtMS42LT0iOC4yczAuNS01LjYsMS42LTguMmMxLjEtMi42LDIuNS00LjgsNC40LTYuNyIgYzEuOC0xLjksNC0zLjQsNi42LTQuNWMyLjUtMS4xLDUuMy0xLjYsOC4yLTEuNmMyLjMsMCw0LjUsMC4zLDYuNiwxYzIuMSwwPSIuNyw0LDEuNyw1LjcsM1Y5LjJsOC0xLjh2NTcuOEg0NDUuMXoiIG00MTkuOSw0NC44IGMwLDQsMS4zLDcuNCw0LDEwLjFjMi43LDIuNyw2LDQuMSw5LjgsNC4xYzIuMywwLDQuNS0wLjQsNi40LTEuM2MxLjktMC45LD0iMy41LTIuMSw0LjktMy42VjM1LjZjLTEuMy0xLjQtMi45LTIuNi00LjktMy41IiBjLTItMC45LTQuMS0xLjMtNi40LTEuM2MtMy45LDAtNy4yLDEuMy05LjksNGM0MjEuMiwzNy41LDQxOS45LDQwLjgsNDE5Ljk9Iiw0NC44eiZxdW90Oy8iPgogICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O3N0MCZxdW90OyIgZD0iM0QmcXVvdDtNNDgwLjEsNjUuMnYtNTZoOC40djI0aDI5Ljh2LTI0aDguNHY1NmgtOC40VjQwLjg9IiBoLTI5Ljh2MjQuNGg0ODAuMXoiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTU0OS4yLDY2Yy00LjQsMC04LTEuMi0xMC44LTMuNWMtMi44LTIuMy00LjItNS4zPSIgLTQuMi04LjljMC00LjEsMS42LTcuMSw0LjctOS4yYzMuMS0yLjEsNy4xLTMuMiwxMS44LTMuMiBjMiwwLDMuOSwwLjIsNS44LDAuNmMxLjksMC40LDMuNywwLjksNS4zLDEuNnYtNC4zYzAtMi45LTAuOS01LTIuNi02LjVjLTE9Ii43LTEuNC00LjItMi4yLTcuNC0yLjJjLTIsMC00LDAuMy02LDAuOSIgYy0yLjEsMC42LTQuMywxLjQtNi42LDIuNmwtMy02YzIuOS0xLjMsNS43LTIuNCw4LjQtMy4xYzIuNy0wLjcsNS41LTEuMSw4PSIuMy0xLjFjNS4yLDAsOS4zLDEuMywxMi4yLDMuOCIgYzIuOSwyLjUsNC40LDYuMSw0LjQsMTAuOHYyN2gtNy44di0zLjVjLTEuOCwxLjQtMy43LDIuNS01LjgsMy4yYzU1My45LDY1PSIuNiw1NTEuNiw2Niw1NDkuMiw2NnoiIG01NDEuOSw1My40YzAsMiwwLjksMy42LDIuNiw0LjggYzEuNywxLjIsMy45LDEuOCw2LjYsMS44YzIuMSwwLDQuMS0wLjMsNS45LTFjMS44LTAuNiwzLjQtMS42LDQuOS0yLjl2LTcuPSIxYy0xLjUtMC44LTMuMS0xLjQtNC44LTEuOGMtMS43LTAuNC0zLjYtMC42LTUuNy0wLjYiIGMtMi44LDAtNSwwLjYtNi44LDEuOGM1NDIuOCw0OS42LDU0MS45LDUxLjMsNTQxLjksNTMuNHoiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTU4Mi42LDU1LjJWMzEuMkg1NzR2LTYuN2g4LjZWMTQuMWw3LjktMS45djEyLjNoPSIgMTJ2Ni43aC0xMnYyMi4xYzAsMi4xLDAuNSwzLjUsMS40LDQuNCBjMC45LDAuOSwyLjUsMS4zLDQuNiwxLjNjMS4yLDAsMi4yLTAuMSwzLTAuMmMwLjktMC4xLDEuOC0wLjQsMi44LTAuOHY2Ljc9ImMtMS4xLDAuNC0yLjQsMC43LTMuOCwwLjljLTEuNCwwLjItMi43LDAuMy0zLjgsMC4zIiBjLTMuOSwwLTctMC45LTktMi44YzU4My43LDYxLjQsNTgyLjYsNTguNyw1ODIuNiw1NS4yeiI+PC9wYXRoPgogICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O3N0MCZxdW90OyIgZD0iM0QmcXVvdDtNMzE4LDkzLjJoMjEuNWMxNi44LDAsMjkuNiwxMi4zLDI5LjYsMjguMmMwLDE1LjY9IiAtMTIuOCwyNy44LTI5LjYsMjcuOGgzMTh2OTMuMnogbTMyOS42LDEwMy42djM1LjRoOS44IGMxMCwwLDE3LjctNy43LDE3LjctMTcuNWMwLTEwLTcuNy0xNy44LTE3LjctMTcuOGgzMjkuNnoiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTM5Ni42LDEwNi44YzEyLjUsMCwyMi4yLDkuNSwyMi4yLDIxLjdjMCwxMi4yLTkuPSIgOCwyMS42LTIyLjIsMjEuNnMtMjIuMi05LjQtMjIuMi0yMS42IGMzNzQuNCwxMTYuMywzODQuMSwxMDYuOCwzOTYuNiwxMDYuOHogbTM5Ni42LDExNi4zYy02LjQsMC0xMS41LDUuMy0xMS41LD0iMTIuMmMwLDYuNyw1LDEyLjEsMTEuNSwxMi4xczExLjUtNS40LDExLjUtMTIuMSIgYzQwOC4xLDEyMS42LDQwMy4xLDExNi4zLDM5Ni42LDExNi4zeiI+PC9wYXRoPgogICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O3N0MCZxdW90OyIgZD0iM0QmcXVvdDtNNDU1LjksMTM1LjhsNi42LDYuOGMtNC4zLDQuNy0xMC41LDcuNC0xNyw3LjRjLTE9IiAyLjMsMC0yMS44LTkuNC0yMS44LTIxLjZjMC0xMi4yLDkuNS0yMS43LDIxLjgtMjEuNyBjNi42LDAsMTMsMi43LDE3LjMsNy40bC02LjcsNy4xYy0zLjEtMy40LTYuNS01LTEwLjMtNWMtNi4zLDAtMTEuMiw1LjMtMTE9Ii4yLDEyLjJjMCw2LjksNSwxMiwxMS40LDEyIiBjNDQ5LjcsMTQwLjQsNDUyLjksMTM4LjksNDU1LjksMTM1Ljh6Ij48L3BhdGg+CiAgICAgICAgPHBhdGggY2xhc3M9IjNEJnF1b3Q7c3QwJnF1b3Q7IiBkPSIzRCZxdW90O000NzguOSwxMzEuOWMwLDUuMiwzLjQsOC43LDguNyw4LjdjMy43LDAsNi42LTEuND0iICw4LjYtNC4ydi0yOC45aDExdjQxLjdoLTExdi0zLjRjLTMuMSwyLjctNy4xLDQuMi0xMS43LDQuMiBjLTkuOCwwLTE2LjUtNi45LTE2LjUtMTYuNnYtMjUuOWgxMC45djEzMS45eiI+PC9wYXRoPgogICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O3N0MCZxdW90OyIgZD0iM0QmcXVvdDtNNTE1LjQsMTA3LjZoMTF2My4xYzMtMi42LDYuNi0zLjksMTAuOS0zLjljNS40LDA9IiAsOS44LDIuMywxMi42LDYuMmMzLjQtNCw4LjItNi4yLDEzLjgtNi4yIGM5LjQsMCwxNiw2LjksMTYsMTYuNnYyNS45aC0xMXYtMjQuM2MwLTUuMi0zLTguNy03LjktOC43Yy0zLjQsMC02LjEsMS40LT0iOCw0LjJjMC4yLDAuOSwwLjIsMS45LDAuMiwzdjI1LjloLTExdi0yNC4zIiBjMC01LjItMy04LjctNy44LTguN2MtMy4zLDAtNS45LDEuNC03LjgsMy44djI5LjJoLTExdjEwNy42eiI+PC9wYXRoPgogICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O3N0MCZxdW90OyIgZD0iM0QmcXVvdDtNNjA3LjYsMTA2LjhjMTEuOCwwLDIwLjYsOS42LDIwLjYsMjIuNHYyLjloLTMxYzE9IiAuNSw1LjIsNi4xLDguNywxMS44LDguN2MzLjcsMCw3LTEuMiw5LjItMy40bDcuMiw2LjYgYy01LjEsNC4yLTEwLjIsNi0xNi45LDZjLTEyLjYsMC0yMi40LTkuNC0yMi40LTIxLjZjNTg2LjEsMTE2LjQsNTk1LjUsMTA2PSIuOCw2MDcuNiwxMDYuOHoiIG01OTcuMSwxMjQuM2gyMC40IGMtMS40LTUtNS4zLTguNC0xMC4yLTguNGM2MDIuMywxMTUuOSw1OTguNSwxMTkuMiw1OTcuMSwxMjQuM3oiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTYzNC44LDEwNy42aDExdjMuNGMzLjEtMi43LDcuMS00LjIsMTEuNy00LjJjOS44PSIgLDAsMTYuNSw2LjksMTYuNSwxNi42djI1LjloNjYzdi0yNC4zIGMwLTUuMi0zLjQtOC43LTguNy04LjdjLTMuNywwLTYuNiwxLjQtOC42LDQuMnYyOC45aC0xMXYxMDcuNnoiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTY4Ni41LDExNi44aC04LjZ2LTkuMmg4LjZWOTYuOWwxMS0yLjV2MTMuMWgxMS44PSIgdjkuMmgtMTEuOHYxOC41YzAsMy45LDEuNSw1LjQsNS44LDUuNGMyLjIsMCwzLjgtMC4zLDUuOC0xIHY5Yy0yLjQsMC43LTYuMiwxLjMtOC41LDEuM2MtOS4xLDAtMTQuMS00LjItMTQuMS0xMi40djExNi44eiI+PC9wYXRoPgogICAgICAgIDxwYXRoIGNsYXNzPSIzRCZxdW90O3N0MCZxdW90OyIgZD0iM0QmcXVvdDtNNzEyLjcsMTM3LjJjMC04LjIsNi43LTEyLjYsMTcuMS0xMi42YzMuNiwwLDcsMC49IiA2LDEwLjIsMS42di0zYzAtNC45LTMtNy4zLTguOC03LjNjLTMuOCwwLTcuOCwxLjMtMTIuNywzLjQgbC00LTguMWM2LjUtMywxMi40LTQuNSwxOC42LTQuNWMxMS4xLDAsMTcuOCw1LjQsMTcuOCwxNS40djI3aDc0MHYtM2MtMy41PSIsMi42LTcuNCwzLjctMTIuMSwzLjciIGM3MTguNywxNTAsNzEyLjcsMTQ0LjUsNzEyLjcsMTM3LjJ6IG03MzAuOCwxNDIuMWMzLjUsMCw2LjYtMC45LDkuMi0yLjZ2LT0iNi4yYy0yLjYtMS01LjQtMS41LTguOC0xLjVjLTQuOCwwLTgsMS44LTgsNS4yIiBjNzIzLjIsMTQwLjEsNzI2LjEsMTQyLjEsNzMwLjgsMTQyLjF6Ij48L3BhdGg+CiAgICAgICAgPHBhdGggY2xhc3M9IjNEJnF1b3Q7c3QwJnF1b3Q7IiBkPSIzRCZxdW90O003NjMuMywxMTYuOGgtOC42di05LjJoOC42Vjk2LjlsMTEtMi41djEzLjFoMTEuOD0iIHY5LjJoLTExLjh2MTguNWMwLDMuOSwxLjUsNS40LDUuOCw1LjRjMi4yLDAsMy44LTAuMyw1LjgtMSB2OWMtMi40LDAuNy02LjIsMS4zLTguNSwxLjNjLTkuMSwwLTE0LjEtNC4yLTE0LjEtMTIuNHYxMTYuOHoiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTc5MC42LDk2LjRjMC0zLjQsMi45LTYuMiw2LjItNi4yYzMuNCwwLDYuMiwyLjgsPSIgNi4yLDYuMmMwLDMuNC0yLjgsNi4yLTYuMiw2LjIgYzc5My41LDEwMi42LDc5MC42LDk5LjgsNzkwLjYsOTYuNHogbTgwMi40LDE0OS4yaC0xMXYtNDEuN2gxMXYxNDkuMnoiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTgzMS4yLDEwNi44YzEyLjUsMCwyMi4yLDkuNSwyMi4yLDIxLjdjMCwxMi4yLTkuPSIgOCwyMS42LTIyLjIsMjEuNmMtMTIuNSwwLTIyLjItOS40LTIyLjItMjEuNiBjODA4LjksMTE2LjMsODE4LjcsMTA2LjgsODMxLjIsMTA2Ljh6IG04MzEuMiwxMTYuM2MtNi40LDAtMTEuNSw1LjMtMTEuNSw9IjEyLjJjMCw2LjcsNSwxMi4xLDExLjUsMTIuMWM2LjUsMCwxMS41LTUuNCwxMS41LTEyLjEiIGM4NDIuNywxMjEuNiw4MzcuNywxMTYuMyw4MzEuMiwxMTYuM3oiPjwvcGF0aD4KICAgICAgICA8cGF0aCBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTg2MCwxMDcuNmgxMXYzLjRjMy4xLTIuNyw3LjEtNC4yLDExLjctNC4yYzkuOCwwPSIgLDE2LjUsNi45LDE2LjUsMTYuNnYyNS45aC0xMC45di0yNC4zIGMwLTUuMi0zLjQtOC43LTguNy04LjdjLTMuNywwLTYuNiwxLjQtOC42LDQuMnYyOC45aC0xMXYxMDcuNnoiPjwvcGF0aD4KICAgIDwvZz4KICAgIDxnIGlkPSIzRCZxdW90O0hhdF9pY29uXzAwMDAwMDQ1NjE4MDkyMzA1NTMzNTUyNTYwMDAwMDAyMTQzNTA4NzEwMjcwMzU2NjI1XyZxdW90OyI+CiAgICAgICAgPGc+CiAgICAgICAgICAgIDxnPgogICAgICAgICAgICAgICAgPHBhdGggaWQ9IjNEJnF1b3Q7UmVkX2hhdF8wMDAwMDE2MTU5MjQyNDg3MjkwNzYxOTM3MDAwMDAwMjY1MzE1NzM4OTg3NDc3MTM0OF89IiAiIGNsYXNzPSIzRCZxdW90O3N0MSZxdW90OyIgZD0iM0QmcXVvdDtNMTI5LDkyLjJjMTIuNSwwLDMwLjYtMi42LDMwLjYtMTcuNSIgYzAtMS4yLDAtMi4zLTAuMy0zLjRsMTUxLjgsMzljLTEuNy03LjEtMy4yLTEwLjMtMTUuNy0xNi42Yy05LjctNS0zMC44LT0iMTMuMS0zNy4xLTEzLjFjLTUuOCwwLTcuNSw3LjUtMTQuNCw3LjUiIGMtNi43LDAtMTEuNi01LjYtMTcuOS01LjZjLTYsMC05LjksNC4xLTEyLjksMTIuNWMwLDAtOC40LDIzLjctOS41LDI3LjI9IkM0NCw1MS41LDQ0LDUyLjIsNDQsNTIuOEM0NCw2Miw4MC4zLDkyLjIsMTI5LDkyLjJ6IiBtMTYxLjUsODAuOGMxLjcsOC4yLDEuNyw5LjEsMS43LDEwLjFjMCwxNC0xNS43LDIxLjgtMzYuNCwyMS44Yy00Ni44LDA9Ii04Ny43LTI3LjQtODcuNy00NS41YzAtMi44LDAuNi01LjQsMS41LTcuMyIgYzIzLjgsNjAuOCwyLDYzLjgsMiw4M2MwLDMxLjUsNzQuNiw3MC4zLDEzMy43LDcwLjNjNDUuMywwLDU2LjctMjAuNSw1Nj0iLjctMzYuNkMxOTIuMywxMDMuOSwxODEuNCw4OS40LDE2MS41LDgwLjh6JnF1b3Q7LyI+CiAgICAgICAgICAgICAgICA8cGF0aCBpZD0iM0QmcXVvdDtCbGFja19iYW5kXzAwMDAwMDY5MzU3MDE0NTg4NjcxNzU3OTgwMDAwMDAzODYxMjcwMTc4OTYyMzU0OD0iIDI2XyIgZD0iM0QmcXVvdDtNMTYxLjUsODAuOGMxLjcsOC4yLDEuNyw5LjEsMS43LDEwLjEiIGMwLDE0LTE1LjcsMjEuOC0zNi40LDIxLjhjLTQ2LjgsMC04Ny43LTI3LjQtODcuNy00NS41YzAtMi44LDAuNi01LjQsMS49IjUtNy4zbDMuNy05LjFDNDQsNTEuNSw0NCw1Mi4yLDQ0LDUyLjgiIGM0NCw2Miw4MC4zLDkyLjIsMTI5LDkyLjJjMTIuNSwwLDMwLjYtMi42LDMwLjYtMTcuNWMwLTEuMiwwLTIuMy0wLjMtMy49IjRMMTYxLjUsODAuOHomcXVvdDsvIj4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxwYXRoIGlkPSIzRCZxdW90O0RpdmlkaW5nX2xpbmVfMDAwMDAxMTk4MzAwOTA2OTYxMDc0NTk4OTAwMDAwMTUwNDkzNTYzNjAzODIxNjIzPSIgMDlfIiBjbGFzcz0iM0QmcXVvdDtzdDAmcXVvdDsiIGQ9IjNEJnF1b3Q7TTI1NS41LDE2MC43Yy0xLjIsMC0yLjItMS0yLjItMi4yIiB2NC4yYzAtMS4yLDEtMi4yLDIuMi0yLjJzMi4yLDEsMi4yLDIuMnYxNTQuMmMyNTcuNywxNTkuNywyNTYuNywxNjAuNywyNTUuPSI1LDE2MC43eiZxdW90Oy8iPgo8L2c+Cjwvc3ZnPg==){#3D\"Layer_1\"}=0A
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: image/svg+xml Content-Transfer-Encoding: quoted-printable
Content-Location:
https://docs.redhat.com/\_nuxt/Red-Hat-Summit-logo.DsUYtlmu.svg
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iM0QmcXVvdDs4OCZxdW90OyIgaGVpZ2h0PSIzRCZxdW90OzQ2JnF1b3Q7IiB2aWV3Ym94PSIzRCZxdW90OzAiIDAgODggNDYiIGZpbGw9IjNEJnF1b3Q7bm9uZSZxdW90OyIgeG1sbnM9Ij0zRCZxdW90O2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJnF1b3Q7Ij4KPGcgY2xpcC1wYXRoPSIzRCZxdW90O3VybCgjY2xpcDBfNDMzNF8yMjUxKSZxdW90OyI+CjxwYXRoIGQ9IjNEJnF1b3Q7TTg4IiAwaDB2MzkuMzUwMWgzNy40Nzk2bDQ0LjExOTcgNDZsNTAuNzU5OSAzOS4zNTAxaDg4djB6IiBmaWxsPSI9M0QmcXVvdDsjRUUwMDAwJnF1b3Q7LyI+CjxwYXRoIGQ9IjNEJnF1b3Q7TTczLjUxMDQiIDIzLjMwMzNoNzEuNTI1NHYyMC43ODUyaDczLjUxMDR2MTguMjQ0M2w3Ni41MjI1IDE3LjU5MTk9IlYyMC43ODUySDc5LjI3MjJWMjMuMzAzM0g3Ni41MjI1VjI3LjA1NzVDNzYuNTIyNSIgMjcuOTM4OCA3Ni44NTMyIDI4LjI0NzggNzc9Ii44MjMyIiAyOC4yNDc4Yzc4LjMwMjIgMjguMjQ3OCA3OC42Nzg3IDI4LjE5MDYgNzkuMTgxIDI4LjA0MTh2MzAuNDc5N2M3OC42MjE9IjYiIDMwLjY1MTQgNzcuNjUyIDMwLjc3NzMgNzcuMDgxNCAzMC43NzczYzc0LjcxOTkgMzAuNzc3MyA3My41MTA0IDI5LjcxMjggNzM9Ii41MTA0IiAyNy42NDEydjIzLjI5MTh2MjMuMzAzM3oiIGZpbGw9IjNEJnF1b3Q7d2hpdGUmcXVvdDsvIj4KPHBhdGggZD0iM0QmcXVvdDtNNjcuMDk3NyIgMTguMjFjNjcuMDk3NyAxNy4yOTQ0IDY3LjgzOSAxNi41NTA0IDY4Ljc1MiAxNi41NTA0YzY5Lj0iNjY0NSIgMTYuNTUwNCA3MC40MDYzIDE3LjI5NDQgNzAuNDA2MyAxOC4yMWM3MC40MDYzIDE5LjEyNTcgNjkuNjY0NSAxOS44Njk2PSI2OC43NTIiIDE5Ljg2OTZjNjcuODM5IDE5Ljg2OTYgNjcuMDk3NyAxOS4xMjU3IDY3LjA5NzcgMTguMjF6bTcwLjI1OCAzMC42NTE0PSJINjcuMjQ1OVYyMC43ODUzSDcwLjI1OFYzMC42NTE0WiZxdW90OyIgZmlsbD0iM0QmcXVvdDt3aGl0ZSZxdW90Oy8iPgo8cGF0aCBkPSIzRCZxdW90O001MC4wNjQiIDIwLjc4NTNoNTMuMDc2MXYyMS40MTQ4YzUzLjc2MDggMjAuODc2OCA1NC42MDUgMjAuNTkwNyA1PSI1LjUyOTIiIDIwLjU5MDdjNTYuNzYxMiAyMC41OTA3IDU3Ljc3NjYgMjEuMDk0MyA1OC40NDk3IDIxLjk1MjdjNTkuMjQ4NSAyMS4wPSI3MTQiIDYwLjM0MzkgMjAuNTkwNyA2MS42NDQ2IDIwLjU5MDdjNjMuODgwOCAyMC41OTA3IDY1LjQ1NTEgMjIuMjI3NCA2NS40NTUxPSIyNC41NjI0VjMwLjY0SDYyLjQ0MzFWMjQuOTc0NEM2Mi40NDMxIiAyMy44ODcgNjEuODE1OCAyMy4xODg5IDYwLjg0NTggMjMuMTg9Ijg5QzYwLjE3MjciIDIzLjE4ODkgNTkuNjEzOCAyMy40NTIxIDU5LjIyNTYgMjMuOTMyOGM1OS4yNDg1IDI0LjEzODggNTkuMjU5OD0iMjQuMzQ0OSIgNTkuMjU5OCAyNC41NjI0djMwLjY0aDU2LjI0Nzd2MjQuOTc0NGM1Ni4yNDc3IDIzLjg4NyA1NS42MjA0IDIzLjE4OD0iOSIgNTQuNjUwNCAyMy4xODg5YzUzLjk3NzQgMjMuMTg4OSA1My40NDEzIDIzLjQyOTIgNTMuMDY0OCAyMy44OTg1djMwLjY1MTRoNT0iMC4wNTI3VjIwLjc4NTNINTAuMDY0WiZxdW90OyIgZmlsbD0iM0QmcXVvdDt3aGl0ZSZxdW90Oy8iPgo8cGF0aCBkPSIzRCZxdW90O00zMi44ODI1IiAyMC43ODUzaDM1Ljg5NDZ2MjEuNDE0OGMzNi41NzkxIDIwLjg3NjggMzcuNDIzNCAyMC41OTA3PSIzOC4zNDc1IiAyMC41OTA3YzM5LjU3OTggMjAuNTkwNyA0MC41OTUgMjEuMDk0MyA0MS4yNjg1IDIxLjk1MjdjNDIuMDY2OSAyMS49IjA3MTQiIDQzLjE2MjMgMjAuNTkwNyA0NC40NjMgMjAuNTkwN2M0Ni42OTkxIDIwLjU5MDcgNDguMjczNSAyMi4yMjc0IDQ4LjI3MzU9IjI0LjU2MjRWMzAuNjRINDUuMjYxNFYyNC45NzQ0QzQ1LjI2MTQiIDIzLjg4NyA0NC42MzQyIDIzLjE4ODkgNDMuNjY0MiAyMy4xOD0iODlDNDIuOTkxMSIgMjMuMTg4OSA0Mi40MzIyIDIzLjQ1MjEgNDIuMDQ0IDIzLjkzMjhjNDIuMDY2OSAyNC4xMzg4IDQyLjA3ODUgMj0iNC4zNDQ5IiA0Mi4wNzg1IDI0LjU2MjR2MzAuNjRoMzkuMDY2M3YyNC45NzQ0YzM5LjA2NjMgMjMuODg3IDM4LjQzODggMjMuMTg4OT0iMzcuNDY5IiAyMy4xODg5YzM2Ljc5NTkgMjMuMTg4OSAzNi4yNTk3IDIzLjQyOTIgMzUuODgzMSAyMy44OTg1djMwLjY1MTRoMzIuPSI4NzExVjIwLjc4NTNIMzIuODgyNVomcXVvdDsiIGZpbGw9IjNEJnF1b3Q7d2hpdGUmcXVvdDsvIj4KPHBhdGggZD0iM0QmcXVvdDtNMjQuNDYxMyIgMjYuNDYyM2MyNC40NjEzIDI3LjU0OTYgMjUuMTY4NiAyOC4yNDc4IDI2LjI0MTIgMjguMjQ3OD0iQzI3LjAwNTYiIDI4LjI0NzggMjcuNTk4OSAyNy45NzMxIDI4LjAwOTYgMjcuNDY5NXYyMC43OTY3aDMxLjAyMTZ2MzAuNjYyOGgyOD0iLjAwOTZWMjkuOTg3NUMyNy4yNzk0IiAzMC41NDg0IDI2LjM3ODEgMzAuODQ2IDI1LjM3NCAzMC44NDZjMjMuMDY5MyAzMC44NDYgMj0iMS40NDkyIiAyOS4yMDkyIDIxLjQ0OTIgMjYuODc0M3YyMC43OTY3aDI0LjQ2MTN2MjYuNDYyM3oiIGZpbGw9IjNEJnF1b3Q7d2hpdGUmcXVvdDsvIj4KPHBhdGggZD0iM0QmcXVvdDtNMTAuMzkzNSIgMjYuMzI0OWMxMS45Nzk0IDI3LjYwNjkgMTMuMjIzIDI4LjEzMzQgMTQuNzI5IDI4LjEzMzRjMT0iNi4yMzUxIiAyOC4xMzM0IDE3LjA2OCAyNy42NjQxIDE3LjA2OCAyNi44NjI5YzE3LjA2OCAyNi4xMzA0IDE2LjU2NTkgMjUuNzc1Nj0iMTUuMjY1MyIgMjUuNTU4MWwxMi40MDE1IDI1LjA1NDVjMTAuMjc5NCAyNC42NzY4IDkuMTE1NjUgMjMuMzk0OSA5LjExNTY1IDIxPSIuNDcyQzkuMTE1NjUiIDE4LjkzMSAxMS4xMjM3IDE3LjQwODggMTQuNDU1MiAxNy40MDg4YzE2LjM5NDggMTcuNDA4OCAxOC40OTQxPSIxOC4xMTg0IiAxOS45MjAzIDE5LjI3NDRsMTguMjMxNyAyMS42NDM3YzE2Ljg1MTIgMjAuNTc5MiAxNS42MDc2IDIwLjA5ODUgMTQ9Ii4yMzg0IiAyMC4wOTg1YzEyLjkzNzggMjAuMDk4NSAxMi4xMzkxIDIwLjUyMiAxMi4xMzkxIDIxLjIzMTdjMTIuMTM5MSAyMS44ODQ9IjEyLjU4NDEiIDIyLjIwNDUgMTMuNjc5NCAyMi4zODc2bDE2LjM3MiAyMi44MzRjMTguODgyIDIzLjI0NjEgMjAuMjA1NSAyNC41Mj0iOCIgMjAuMjA1NSAyNi41NDI0YzIwLjIwNTUgMjkuMTg2MyAxOC4wMjYzIDMwLjgzNDUgMTQuNTAwOCAzMC44MzQ1YzEyLjQwMTUgMz0iMC44MzQ1IiAxMC4yNDUyIDMwLjAzMzMgOC42MjUwNiAyOC42NDg0bDEwLjQwNDkgMjYuMzEzNWwxMC4zOTM1IDI2LjMyNDl6IiBmaT0ibGw9M0QmcXVvdDt3aGl0ZSZxdW90Oy8iPgo8cGF0aCBkPSIzRCZxdW90O001OS4wNzY0IiAxNC4xMDFjNTkuMDc2NCAxNS4yMzQxIDU5Ljc2MTEgMTUuNzgzNSA2MC45OTMxIDE1Ljc4MzVjPSI2MS4yOTAxIiAxNS43ODM1IDYxLjgxNDggMTUuNzE0OCA2Mi4xMjI2IDE1LjYyMzN2MTQuMzA3YzYxLjg0OSAxNC4zODcxIDYxLjY1PSI0OSIgMTQuNDIxNSA2MS4zOTI1IDE0LjQyMTVjNjAuODc5IDE0LjQyMTUgNjAuNjk2NiAxNC4yNjEyIDYwLjY5NjYgMTMuNzgwNXYxPSIxLjc2NjFINjIuMTc5N1YxMC40MTU1SDYwLjY5NjZWOC42OTg2OEw1OS4wNzY0IiA5LjA1MzQ4djEwLjQxNTVoNTguMDAzOXYxMS43PSI2NjFINTkuMDc2NFYxNC4xMDFaTTU0LjAzMzUiIDE0LjEzNTRjNTQuMDMzNSAxMy43ODA1IDU0LjM4NzEgMTMuNjA4OSA1NC45MTE5PSIxMy42MDg5QzU1LjI2NTkiIDEzLjYwODkgNTUuNTg1MyAxMy42NTQ3IDU1Ljg3MDYgMTMuNzM0N3YxNC40MjE1YzU1LjU3MzcgMTQ9Ii41OTMyIiA1NS4yMjAxIDE0LjY3MzMgNTQuODU1MiAxNC42NzMzYzU0LjMzIDE0LjY3MzMgNTQuMDIyMiAxNC40NjczIDU0LjAyMjI9IjE0LjEzNTRNNTQuNTEyOCIgMTUuODE3OWM1NS4wODMgMTUuODE3OSA1NS41Mzk1IDE1LjY5MiA1NS45NzMxIDE1LjQwNTh2MTUuNz0iMjYzSDU3LjU3MDNWMTIuMzI2OUM1Ny41NzAzIiAxMS4wMzM2IDU2LjcwMzIgMTAuMzI0IDU1LjI0MyAxMC4zMjRjNTQuNDMyOSAxMD0iLjMyNCIgNTMuNjM0MSAxMC41MTg1IDUyLjc2NjkgMTAuOTA3N2w1My4zNDkyIDEyLjA5OGM1My45NjUyIDExLjgzNDggNTQuNDg5OT0iMTEuNjc0NiIgNTQuOTQ2NCAxMS42NzQ2YzU1LjYxOTUgMTEuNjc0NiA1NS45NjE4IDExLjkzNzggNTUuOTYxOCAxMi40NjQzdjEyPSIuNzI3NkM1NS41ODUzIiAxMi42MjQ1IDU1LjE4NTkgMTIuNTc4NyA1NC43NjM2IDEyLjU3ODdjNTMuNDA2MiAxMi41Nzg3IDUyLjU4PSI0NSIgMTMuMTUxIDUyLjU4NDUgMTQuMTgxMmM1Mi41ODQ1IDE1LjExOTcgNTMuMzI2MyAxNS44MjkzIDU0LjUwMTIgMTUuODI5M200PSI1LjcwNDgiIDE1LjczNzdoNDcuNDI3NHYxMi45OTA4aDUwLjMxNDJ2MTUuNzM3N2g1Mi4wMzY4djguNzEwMTRoNTAuMzE0MnYxMS40PSIxMTNINDcuNDI3NFY4LjcxMDE0SDQ1LjcwNDhWMTUuNzM3N1pNMzkuMTQ0NCIgMTMuMDcwOWMzOS4xNDQ0IDEyLjMwNDEgMzkuNzQ5PSIxIiAxMS43MjAzIDQwLjUzNjUgMTEuNzIwM2M0MC45ODEzIDExLjcyMDMgNDEuMzgwOCAxMS44NjkxIDQxLjY1NDQgMTIuMTMyNHYxPSIzLjk4NjZDNDEuMzY5MSIgMTQuMjcyNyA0MC45ODEzIDE0LjQxMDEgNDAuNTM2NSAxNC40MTAxYzM5Ljc2MDUgMTQuNDEwMSAzOS4xPSI0NDQiIDEzLjgyNjMgMzkuMTQ0NCAxMy4wNTk1bTQxLjY3NzMgMTUuNzI2M2g0My4yNzQ2djguMzQzODdsNDEuNjU0NCA4LjY5ODY4PSJWMTAuNzAxN0M0MS4yNTUiIDEwLjQ3MjcgNDAuNzk4OSAxMC4zNDY4IDQwLjMwODMgMTAuMzQ2OGMzOC43Njc5IDEwLjM0NjggMzcuPSI1NTg1IiAxMS41MzcyIDM3LjU1ODUgMTMuMDcwOWMzNy41NTg1IDE0LjYwNDYgMzguNzQ1MSAxNS44MDY0IDQwLjI2MjUgMTUuODA2PSI0QzQwLjc4NzMiIDE1LjgwNjQgNDEuMjc3OSAxNS42NDYyIDQxLjY4ODYgMTUuMzQ4NnYxNS43Mzc3bDQxLjY3NzMgMTUuNzI2M3ptPSIzNC4zMjk3IiAxMS42NTE2YzM0Ljg0MzEgMTEuNjUxNiAzNS4yNjUyIDExLjk4MzYgMzUuNDM2NCAxMi40OTg2aDMzLjIyM2MzMy4zPSI4MjciIDExLjk2MDcgMzMuNzgyIDExLjY1MTYgMzQuMzI5NyAxMS42NTE2em0zMS41OTE0IDEzLjA4MjRjMzEuNTkxNCAxNC42Mjc1PSIzMi44NTc5IiAxNS44MjkzIDM0LjQ3OCAxNS44MjkzYzM1LjM2NzkgMTUuODI5MyAzNi4wMTgyIDE1LjU4OSAzNi42OTE0IDE1LjA9IjI4MUwzNS42MTg5IiAxNC4wNzgxYzM1LjM2NzkgMTQuMzQxNCAzNS4wMDI4IDE0LjQ3ODcgMzQuNTU3OSAxNC40Nzg3YzMzLjk1MzI9IjE0LjQ3ODciIDMzLjQ2MjYgMTQuMTQ2OCAzMy4yNTcyIDEzLjYzMTdoMzcuMDMzN3YxMy4yMzEyYzM3LjAzMzcgMTEuNTQ4NyAzNT0iLjkwNDEiIDEwLjMyNCAzNC4zNjM5IDEwLjMyNGMzMi44MjM2IDEwLjMyNCAzMS42MDI4IDExLjUyNTcgMzEuNjAyOCAxMy4wNzA5bT0iMjguODA3NiIgMTAuMTYzN2MyOS4zNzggMTAuMTYzNyAyOS42OTc1IDEwLjUzIDI5LjY5NzUgMTAuOTUzNWMyOS42OTc1IDExLjM3Nz0iMjkuMzc4IiAxMS43NDMyIDI4LjgwNzYgMTEuNzQzMmgyNy4xMDc2djEwLjE1MjNoMjguODA3NnYxMC4xNjM3em0yNS4zODQ4IDE1PSIuNzE0OEgyNy4xMDc2VjEzLjE1MUgyOC40MTk2TDI5Ljc0MzEiIDE1LjcxNDhoMzEuNjU5OWwzMC4xMTk2IDEyLjg5OTJjMzAuOTUyPSI1IiAxMi41MzMgMzEuNDQzMSAxMS43ODkgMzEuNDQzMSAxMC45MTkxYzMxLjQ0MzEgOS42NDg2NiAzMC40NTA1IDguNjc1OCAyOC45PSI2NzMiIDguNjc1OGgyNS4zODQ4djE1LjcwMzR2MTUuNzE0OHoiIGZpbGw9IjNEJnF1b3Q7d2hpdGUmcXVvdDsvIj4KPC9nPgo8ZGVmcz4KPGNsaXBwYXRoIGlkPSIzRCZxdW90O2NsaXAwXzQzMzRfMjI1MSZxdW90OyI+CjxyZWN0IHdpZHRoPSIzRCZxdW90Ozg4JnF1b3Q7IiBoZWlnaHQ9IjNEJnF1b3Q7NDYmcXVvdDsiIGZpbGw9IjNEJnF1b3Q7d2hpdGUmcXVvdDsvIj4KPC9jbGlwcGF0aD4KPC9kZWZzPgo8L3N2Zz4=)=0A
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: image/svg+xml Content-Transfer-Encoding: quoted-printable
Content-Location:
https://static.redhat.com/libs/redhat/rh-iconfont/latest/svg/web-icon-close.svg
![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iM0QmcXVvdDtodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyZxdW90OyIgdmlld2JveD0iM0QmcXVvdDswIiAwIDE2IDE2Ij48dGl0bGU+VUlfST0KY29uLVJlZF9IYXQtQ2xvc2UtQS1CbGFjay1SR0I8L3RpdGxlPjxwYXRoIGQ9IjNEJnF1b3Q7TTEyLjU0IiAxMS40Nmw4LjkyIDcuODNsMy40NT0iLTMuNDZhLjYzLjYzIiAwIDAgMCAwLS44OC42MS42MSAwIDAgMC0uODggMGw4IDYuOTQgNC41NCAzLjQ2YS42MS42MSAwIDAgMC0uOD0iOCIgMCAuNjMuNjMgMCAwIDAgMCAuODhsMy40OSAzLjQ5LTMuNjYgMy42NmEuNjEuNjEgMCAwIDAgMCAuODguNjMuNjMgMCAwIDAgLj0iODgiIDBsOCA4LjcxbDMuNjMgMy42M2EuNjMuNjMgMCAwIDAgLjg4IDAgLjYxLjYxIDAgMCAwIC4wMy0uODh6Ij48L3BhdGg+PC9zdmc+)
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: image/png Content-Transfer-Encoding: base64
Content-Location:
https://www.redhat.com/rhdc/managed-files/rhel-logo-img.png
iVBORw0KGgoAAAANSUhEUgAAADEAAAAwCAYAAAC4wJK5AAAACXBIWXMAAAsTAAALEwEAmpwYAAAA
AXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAWMSURBVHgB1VpNSGNXFD4mcaELjdWFIJUo/qAw
NApCF4XGbVFJlzNQRneFFnRVobOILlqwG22ZgdmZbDqz0/GnWzMwS9HAbFRQgys31mhRC/68+b6b
e/WZyb8vGj84efe+n/vOd+8599x3TyokB4LBYMCyrOdXV1cBVL1aSg68M1ZRURFD8d3i4uJ8tnsr
Ml0YGhoaRUMTopU+PT2V4+Njubi4kFKjqqpKKisrpaamxpyKQyZBJpzu/s9IoOd9l5eXsygGqPD2
9rbs7u7K+fm53Deqq6ulvr5eOjs7FTEg6na7R+bn5+P2+26R0ARWUPTt7OzI1tbWgyifCpJpaWmR
1tZWVuMg0m8nck0CBLwgsI6ij8pvbm5KuaGjo0ONiiSJ9IBIghWXuQGOG5IyJkDYdKPFhMx5N39o
RiDx9ujoSNbW1qSccXBwIA0NDTSxr7u7u99vbGzE1UgYVqurq/IYYCwFE0+QR0UC83GQDDmNPgZQ
Vwr0fk5fdg0MDDCYeff396UUaJbSQOvLGOZ3gY2fNQYyJ/ENZAES02WnYawGruDzgIQXI+FYPGDP
/wJ5puuvIR/FeZhOh/4+jzl5VxK1kB+1sPwB8kJKQyAVHnEAVHxcbpT/Qx/vC3ciQVt/KUkTOoL8
DPlb7h8uKQLGaSns/SkIZ4dcBGqlNChoJNI5LQkc5XiOpH+TJAm/OI+8R+I7yHtJEviglflVshOw
jxg74LXkhnnmqeSPvElUSP5gj7/UylCpN5IknY2EnfATSCFRK28Sy5BvtUJ8YUxunFpsyo/ra2bE
hiA/SeYRa5bbhEnUr9+XLwryiT2t0JRW9pmWKX3dxAjGhheSfZp1Mq4UNcUaMv9I0mHHbdfoJ7ls
3+m4UtQUa8Ah59AzPuzJjYKZnNKY4e+6zudobncNjHmTGB4elpWVFfH5fJ9dY3wgGZoVe/eV3MxI
RCFxJRAIqPeMjY2J4yS8Xq96AXc+Zmdn05KhcqnOb5S3O2262ML22C4J8D0FAftLE4ODgxY+9yxU
swpeZIXDYctgenpanUt3L0bBwohY/0JAwnqSoU10jhUKhazDw0PVJkhkbNMu1Jd6U/+CSBhBT1kY
EfVSHmFqGe9tztLO6OjoLeXZbr462EkU5dgX0ah8xD7QyciIsnuaAc2MfpOKvTTPG7OcmZmRmkRC
tfNff7/soN1iUBCJ1MD0VzgsX4DM5OSkuk4y6+vraf3FKE+bp9DH+FxPT49E0E6mAJoX8jUnrJ2s
XZuNN+fwFxC6tm0eWTfACChfkAw+RHlaCnPKtXaKx+PKnLjdGIlEVJkmMzc3p0aH9SjMhdc5fSYS
iVvPs/e/1GXOXA+2drKT6YeNs4wtFYnFYqpuzqUqXzZrpzdy24lNr/v9fkUiFU6unYqanQyZH3SZ
hDJ9A6QjQMVj+jkqPaSl2E0Fx9ZOxCutXNmunbLBybVTMXBky8bA+AbNhKPBXmcvmx3AfL/J8wHT
YQYuTNtxFmz5sTvB+At72sxkJMKZLdc3eSHweJL9D/0THpLAVqBKKTkJ+0y2J86jtja5AYSMUcwF
Rky1JhobG6UUKAUBQuubQMor6tJ5rwizlMzAPAaYrCqg8ttqdkKqS1WY2HsM6OvrU0eYklp5qpwd
EnpxEKhjHoz+wSxMuYId3dTURIf+c2Fh4S3PXccJ+MYECMRtadayg9GNelJfc95tCshC/t/V1fUO
xSDszct5+OTkpCyS8dQFmVJpa2tTBFwuF5Px1/k5t/1mEEmQCIbKX1dX5+MMwL9GUB6CDJVvb2+X
3t5e48j8W8T3Wf8WYQc+OIbBOgRCPtaZ4yaZs7MzKTUYyBh8TexiCEBubnJ5eXkm3f0594lBhrni
IBr6iiMk9wAqzUgMs4lC+cjS0lI02/2fAE/wAANFrr7rAAAAAElFTkSuQmCC
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location: https://docs.redhat.com/\_nuxt/default.CXM6N0t5.css
\@charset \"utf-8\"; rh-alert\[data-v-84359384\] { width: 100%; }
.element-invisible, .sr-only, .visually-hidden { height: 1px; overflow:
hid= den; padding: 0px; position: absolute; width: 1px; clip: rect(0px,
0px, 0px= , 0px); border: 0px; white-space: nowrap; } \@keyframes
reveal-nav {=20 0% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); opacity: 0;=
visibility: hidden; } 99% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); } 100% { max-height:
9999em; opacity: 1; visibility: visible; } } \@keyframes
reveal-nav-parts {=20 0% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); opacity: 0;=
visibility: hidden; } 1% { visibility: visible; } 99% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); } 100% { max-height:
9999em; opacity: 1; visibility: visible; } } \@media print {
.pfe-navigation\_\_menu, pfe-navigation \[slot\] { display: none
!important; = } } pfe-navigation { \--pfe-broadcasted\--text:
var(\--pfe-theme\--color\--text,#151= 515);
\--pfe-broadcasted\--text\--muted:
var(\--pfe-theme\--color\--text\--muted,#= 6a6e73);
\--pfe-broadcasted\--link: var(\--pfe-theme\--color\--link,#06c);
\--pfe= -broadcasted\--link\--hover:
var(\--pfe-theme\--color\--link\--hover,#004080); \--=
pfe-broadcasted\--link\--focus:
var(\--pfe-theme\--color\--link\--focus,#004080);=
\--pfe-broadcasted\--link\--visited:
var(\--pfe-theme\--color\--link\--visited,#6= 753ac);
\--pfe-broadcasted\--link-decoration: var(\--pfe-theme\--link-decoratio=
n,none); \--pfe-broadcasted\--link-decoration\--hover:
var(\--pfe-theme\--link-d= ecoration\--hover,underline);
\--pfe-broadcasted\--link-decoration\--focus: var=
(\--pfe-theme\--link-decoration\--focus,underline);
\--pfe-broadcasted\--link-de= coration\--visited:
var(\--pfe-theme\--link-decoration\--visited,none); } \@supports
(display:grid) { pfe-navigation { animation: 0.1618s ease 4s 1 normal
forwards running rev= eal-nav; max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); } pfe-navigation \> \*
{ animation: 0.1618s ease 4s 1 normal forwards running=
reveal-nav-parts; opacity: 0; transition: opacity
var(\--pfe-reveal-duratio= n,.1618s) ease-in-out; visibility: hidden; }
} pfe-navigation.pfe-navigation\--processed,
pfe-navigation.pfe-navigation\--pr= ocessed \> \* { animation: auto ease
0s 1 normal none running none; opacity: = 1; visibility: visible; }
pfe-navigation pfe-primary-detail { display: none; }
pfe-navigation\[pfelement\] { display: block; } pfe-navigation-dropdown
{ color: var(\--pfe-navigation\_\_dropdown\--Color,#151= 515); }
#pfe-navigation\[breakpoint=3D\"desktop\"\]
.hidden-at-desktop\[class\]\[class\]\[cl= ass\],
#pfe-navigation\[breakpoint=3D\"mobile\"\]
.hidden-at-mobile\[class\]\[class= \]\[class\],
#pfe-navigation\[breakpoint=3D\"tablet\"\]
.hidden-at-tablet\[class\]\[c= lass\]\[class\],
pfe-navigation\[breakpoint=3D\"desktop\"\] .hidden-at-desktop\[cla=
ss\]\[class\]\[class\], pfe-navigation\[breakpoint=3D\"mobile\"\]
.hidden-at-mobile\[= class\]\[class\]\[class\],
pfe-navigation\[breakpoint=3D\"tablet\"\] .hidden-at-tabl=
et\[class\]\[class\]\[class\] { display: none; } #pfe-navigation,
#pfe-navigation \*, pfe-navigation, pfe-navigation \* { box-= sizing:
border-box; } #pfe-navigation \[pfelement\]
.pfe-navigation\_\_log-in-link, pfe-navigation \[p= felement\]
.pfe-navigation\_\_log-in-link { display: none; } #pfe-navigation,
pfe-navigation { align-items: stretch; background: var(\--p=
fe-navigation\_\_nav-bar\--Background,#151515); color:
var(\--pfe-navigation\_\_n=
av-bar\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
displa= y: flex; font-family: var(\--pfe-navigation\--FontFamily,Red Hat
Text,RedHatT= ext,Arial,Helvetica,sans-serif); font-size:
var(\--pf-global\--FontSize\--md,1= rem); height: auto; line-height:
1.5; margin: 0px; max-width: 9999em; min-h= eight:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); padding: 0px 16px;
posi= tion: relative; z-index:
var(\--pfe-navigation\--ZIndex,var(\--pfe-theme\--zind=
ex\--navigation,95)); } \@media (min-width: 768px) { #pfe-navigation,
pfe-navigation { flex-wrap: wrap; margin: 0px; max-width= : 9999em;
padding: 0px 16px; } } \@media (min-width: 1200px) { #pfe-navigation,
pfe-navigation { margin: 0px auto; padding: 0px 32px; } }
#pfe-navigation .pfe-navigation\_\_dropdown, #pfe-navigation
pfe-navigation-d= ropdown, pfe-navigation .pfe-navigation\_\_dropdown,
pfe-navigation pfe-navig= ation-dropdown { display: none; }
#pfe-navigation \> \[slot=3D\"account\"\], #pfe-navigation \>
\[slot=3D\"search\"\], = #pfe-navigation \>
\[slot=3D\"secondary-links\"\], pfe-navigation \> \[slot=3D\"acc=
ount\"\], pfe-navigation \> \[slot=3D\"search\"\], pfe-navigation \>
\[slot=3D\"secon= dary-links\"\] { height: 0px; overflow: hidden;
visibility: hidden; width: 0p= x; } \@media (min-width: 768px) {
#pfe-navigation nav.pfe-navigation, pfe-navigation nav.pfe-navigation {
a= lign-items: stretch; display: flex; flex-wrap: wrap; } } \@media
(min-width: 992px) { #pfe-navigation nav.pfe-navigation, pfe-navigation
nav.pfe-navigation { f= lex-wrap: nowrap; } } #pfe-navigation
.pfe-navigation\_\_logo-wrapper, pfe-navigation .pfe-navigati=
on\_\_logo-wrapper { align-items: center; display: flex;
justify-content: fle= x-start; margin: 0px; min-width: 150px; padding:
10px 16px 10px 0px; } \@media (min-width: 768px) {
.pfe-navigation\--no-main-menu #pfe-navigation
.pfe-navigation\_\_logo-wrapp= er, .pfe-navigation\--no-main-menu
pfe-navigation .pfe-navigation\_\_logo-wrap= per { margin-right: auto; }
} .pfe-navigation\--collapse-secondary-links
.pfe-navigation\--no-main-menu #pf= e-navigation
.pfe-navigation\_\_logo-wrapper, .pfe-navigation\--collapse-secon=
dary-links .pfe-navigation\--no-main-menu pfe-navigation
.pfe-navigation\_\_lo= go-wrapper { margin-right: 0px; } #pfe-navigation
.pfe-navigation\_\_logo-link, pfe-navigation .pfe-navigation\_=
\_logo-link { border-radius: 3px; display: block; margin-left: -8px;
outline= : 0px; padding: 6px 8px; position: relative; } #pfe-navigation
.pfe-navigation\_\_logo-link:focus, pfe-navigation .pfe-navig=
ation\_\_logo-link:focus { outline: 0px; } #pfe-navigation
.pfe-navigation\_\_logo-link:focus::after, pfe-navigation .pf=
e-navigation\_\_logo-link:focus::after { border: 1px dashed rgb(255,
255, 255= ); inset: 0px; content: \"\"; display: block; position:
absolute; } #pfe-navigation .pfe-navigation\_\_logo-image,
pfe-navigation .pfe-navigation= \_\_logo-image { display: block; height:
auto; width: 100%; } \@media (min-width: 576px) { #pfe-navigation
.pfe-navigation\_\_logo-image, pfe-navigation .pfe-navigati=
on\_\_logo-image { height: var(\--pfe-navigation\_\_logo\--height,40px);
width: a= uto; } } \@media print { #pfe-navigation
.pfe-navigation\_\_logo-image, pfe-navigation .pfe-navigati=
on\_\_logo-image { display: none; } } #pfe-navigation
.pfe-navigation\_\_logo-image:only-child, pfe-navigation .pfe=
-navigation\_\_logo-image:only-child { display: block; } \@media
(min-width: 576px) { #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--s= mall,
pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image= \--small {
height: var(\--pfe-navigation\_\_logo\--height,32px); } } \@media print
{ #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--s= creen,
pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-imag= e\--screen {
display: none !important; } } \@media screen { #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--p= rint,
pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image= \--print {
display: none !important; } } #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--scr=
een.pfe-navigation\_\_logo-image\--print, pfe-navigation
.pfe-navigation\_\_logo=
-image.pfe-navigation\_\_logo-image\--screen.pfe-navigation\_\_logo-image\--print=
{ display: inline-block !important; } #pfe-navigation
.pfe-navigation\_\_fallback-links a, #pfe-navigation .pfe-nav=
igation\_\_log-in-link, #pfe-navigation .pfe-navigation\_\_menu-link,
#pfe-navi= gation .pfe-navigation\_\_secondary-link, pfe-navigation
.pfe-navigation\_\_fal= lback-links a, pfe-navigation
.pfe-navigation\_\_log-in-link, pfe-navigation =
.pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-link = { \--pfe-icon\--color:
var(\--pfe-navigation\_\_dropdown\--link\--Color,var(\--pfe-=
theme\--color\--link,#06c)); align-items: center; appearance: none;
backgroun= d: 0px 0px; border: 0px; color:
var(\--pfe-navigation\_\_nav-bar\--Color\--defau=
lt,var(\--pfe-theme\--color\--ui-base\--text,#fff)); cursor: pointer;
display: = flex; font-family: inherit; font-size:
var(\--pf-global\--FontSize\--md,1rem);= justify-content: center;
margin: 0px; outline: 0px; padding: 8px 24px; pos= ition: relative;
text-align: center; text-decoration: none; white-space: no= wrap; width:
100%; } \@media print { #pfe-navigation
.pfe-navigation\_\_fallback-links a, #pfe-navigation .pfe-n=
avigation\_\_log-in-link, #pfe-navigation .pfe-navigation\_\_menu-link,
#pfe-na= vigation .pfe-navigation\_\_secondary-link, pfe-navigation
.pfe-navigation\_\_f= allback-links a, pfe-navigation
.pfe-navigation\_\_log-in-link, pfe-navigatio= n
.pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-lin= k { display: none !important; } }
\@media (min-width: 768px) { #pfe-navigation
.pfe-navigation\_\_fallback-links a, #pfe-navigation .pfe-n=
avigation\_\_log-in-link, #pfe-navigation .pfe-navigation\_\_menu-link,
#pfe-na= vigation .pfe-navigation\_\_secondary-link, pfe-navigation
.pfe-navigation\_\_f= allback-links a, pfe-navigation
.pfe-navigation\_\_log-in-link, pfe-navigatio= n
.pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-lin= k { \--pfe-icon\--color:
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var(\--=
pfe-theme\--color\--ui-base\--text,#fff)); color:
var(\--pfe-navigation\_\_nav-ba=
r\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
display: fl= ex; flex-direction: column; font-size:
var(\--pfe-navigation\--FontSize\--xs,1= 2px); height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); justify-content:=
flex-end; padding: 14px 8px; width: auto; } \@supports (display:grid) {
#pfe-navigation .pfe-navigation\_\_fallback-links a, #pfe-navigation
.pfe-n= avigation\_\_log-in-link, #pfe-navigation
.pfe-navigation\_\_menu-link, #pfe-na= vigation
.pfe-navigation\_\_secondary-link, pfe-navigation .pfe-navigation\_\_f=
allback-links a, pfe-navigation .pfe-navigation\_\_log-in-link,
pfe-navigatio= n .pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-lin= k { place-items: center; display:
grid; grid-template-rows: 26px 18px; } } #pfe-navigation
.pfe-navigation\_\_fallback-links a\[class\]:focus, #pfe-navi= gation
.pfe-navigation\_\_fallback-links a\[class\]:hover, #pfe-navigation
.pfe= -navigation\_\_log-in-link\[class\]:focus, #pfe-navigation
.pfe-navigation\_\_log= -in-link\[class\]:hover, #pfe-navigation
.pfe-navigation\_\_menu-link\[class\]:fo= cus, #pfe-navigation
.pfe-navigation\_\_menu-link\[class\]:hover, #pfe-navigati= on
.pfe-navigation\_\_secondary-link\[class\]:focus, #pfe-navigation
.pfe-navig= ation\_\_secondary-link\[class\]:hover, pfe-navigation
.pfe-navigation\_\_fallbac= k-links a\[class\]:focus, pfe-navigation
.pfe-navigation\_\_fallback-links a\[cl= ass\]:hover, pfe-navigation
.pfe-navigation\_\_log-in-link\[class\]:focus, pfe-n= avigation
.pfe-navigation\_\_log-in-link\[class\]:hover, pfe-navigation .pfe-na=
vigation\_\_menu-link\[class\]:focus, pfe-navigation
.pfe-navigation\_\_menu-link= \[class\]:hover, pfe-navigation
.pfe-navigation\_\_secondary-link\[class\]:focus,= pfe-navigation
.pfe-navigation\_\_secondary-link\[class\]:hover { box-shadow: = inset 0
4px 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-th=
eme\--color\--ui-accent,#06c)); } } #pfe-navigation
.pfe-navigation\_\_fallback-links a:focus, #pfe-navigation .p=
fe-navigation\_\_fallback-links a:hover, #pfe-navigation
.pfe-navigation\_\_log= -in-link:focus, #pfe-navigation
.pfe-navigation\_\_log-in-link:hover, #pfe-na= vigation
.pfe-navigation\_\_menu-link:focus, #pfe-navigation .pfe-navigation\_=
\_menu-link:hover, #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, #p= fe-navigation
.pfe-navigation\_\_secondary-link:hover, pfe-navigation .pfe-na=
vigation\_\_fallback-links a:focus, pfe-navigation
.pfe-navigation\_\_fallback-= links a:hover, pfe-navigation
.pfe-navigation\_\_log-in-link:focus, pfe-navig= ation
.pfe-navigation\_\_log-in-link:hover, pfe-navigation
.pfe-navigation\_\_m= enu-link:focus, pfe-navigation
.pfe-navigation\_\_menu-link:hover, pfe-naviga= tion
.pfe-navigation\_\_secondary-link:focus, pfe-navigation
.pfe-navigation\_= \_secondary-link:hover { box-shadow: inset 4px 0 0 0
var(\--pfe-navigation\_\_n=
av-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c)); }
\@media (min-width: 768px) { #pfe-navigation
.pfe-navigation\_\_fallback-links a:focus, #pfe-navigation =
.pfe-navigation\_\_fallback-links a:hover, #pfe-navigation
.pfe-navigation\_\_l= og-in-link:focus, #pfe-navigation
.pfe-navigation\_\_log-in-link:hover, #pfe-= navigation
.pfe-navigation\_\_menu-link:focus, #pfe-navigation .pfe-navigatio=
n\_\_menu-link:hover, #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, = #pfe-navigation
.pfe-navigation\_\_secondary-link:hover, pfe-navigation .pfe-=
navigation\_\_fallback-links a:focus, pfe-navigation
.pfe-navigation\_\_fallbac= k-links a:hover, pfe-navigation
.pfe-navigation\_\_log-in-link:focus, pfe-nav= igation
.pfe-navigation\_\_log-in-link:hover, pfe-navigation .pfe-navigation\_=
\_menu-link:focus, pfe-navigation .pfe-navigation\_\_menu-link:hover,
pfe-navi= gation .pfe-navigation\_\_secondary-link:focus, pfe-navigation
.pfe-navigatio= n\_\_secondary-link:hover { box-shadow: inset 0 4px 0 0
var(\--pfe-navigation\_=
\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c));
} } .pfe-navigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_= fallback-links a:focus,
.pfe-navigation\--collapse-secondary-links #pfe-navi= gation
.pfe-navigation\_\_fallback-links a:hover, .pfe-navigation\--collapse-s=
econdary-links #pfe-navigation .pfe-navigation\_\_log-in-link:focus,
.pfe-nav= igation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_log-in-l= ink:hover,
.pfe-navigation\--collapse-secondary-links #pfe-navigation .pfe-n=
avigation\_\_menu-link:focus, .pfe-navigation\--collapse-secondary-links
#pfe-= navigation .pfe-navigation\_\_menu-link:hover,
.pfe-navigation\--collapse-seco= ndary-links #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, .pfe-nav=
igation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_secondar= y-link:hover,
.pfe-navigation\--collapse-secondary-links pfe-navigation .pfe=
-navigation\_\_fallback-links a:focus,
.pfe-navigation\--collapse-secondary-li= nks pfe-navigation
.pfe-navigation\_\_fallback-links a:hover, .pfe-navigation=
\--collapse-secondary-links pfe-navigation
.pfe-navigation\_\_log-in-link:focu= s,
.pfe-navigation\--collapse-secondary-links pfe-navigation
.pfe-navigation= \_\_log-in-link:hover,
.pfe-navigation\--collapse-secondary-links pfe-navigati= on
.pfe-navigation\_\_menu-link:focus,
.pfe-navigation\--collapse-secondary-li= nks pfe-navigation
.pfe-navigation\_\_menu-link:hover, .pfe-navigation\--colla=
pse-secondary-links pfe-navigation
.pfe-navigation\_\_secondary-link:focus, .=
pfe-navigation\--collapse-secondary-links pfe-navigation
.pfe-navigation\_\_se= condary-link:hover { box-shadow: inset 4px 0 0 0
var(\--pfe-navigation\_\_nav-=
bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c)); }
#pfe-navigation .pfe-navigation\_\_fallback-links a:focus,
#pfe-navigation .p= fe-navigation\_\_log-in-link:focus, #pfe-navigation
.pfe-navigation\_\_menu-lin= k:focus, #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, pfe-navigat= ion
.pfe-navigation\_\_fallback-links a:focus, pfe-navigation
.pfe-navigation= \_\_log-in-link:focus, pfe-navigation
.pfe-navigation\_\_menu-link:focus, pfe-n= avigation
.pfe-navigation\_\_secondary-link:focus { outline: 0px; }
#pfe-navigation .pfe-navigation\_\_fallback-links a:focus::after,
#pfe-naviga= tion .pfe-navigation\_\_log-in-link:focus::after,
#pfe-navigation .pfe-naviga= tion\_\_menu-link:focus::after,
#pfe-navigation .pfe-navigation\_\_secondary-li= nk:focus::after,
pfe-navigation .pfe-navigation\_\_fallback-links a:focus::af= ter,
pfe-navigation .pfe-navigation\_\_log-in-link:focus::after,
pfe-navigati= on .pfe-navigation\_\_menu-link:focus::after,
pfe-navigation .pfe-navigation\_= \_secondary-link:focus::after {
border: 1px dashed; inset: 0px; content: \"\";= display: block;
position: absolute; } #pfe-navigation .pfe-navigation\_\_fallback-links
a pfe-icon, #pfe-navigation= .pfe-navigation\_\_log-in-link pfe-icon,
#pfe-navigation .pfe-navigation\_\_me= nu-link pfe-icon, #pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon,= pfe-navigation
.pfe-navigation\_\_fallback-links a pfe-icon, pfe-navigation =
.pfe-navigation\_\_log-in-link pfe-icon, pfe-navigation
.pfe-navigation\_\_menu= -link pfe-icon, pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon { p= ointer-events: none; }
#pfe-navigation .pfe-navigation\_\_fallback-links a
.secondary-link\_\_icon-wra= pper, #pfe-navigation
.pfe-navigation\_\_fallback-links a \> pfe-icon, #pfe-na= vigation
.pfe-navigation\_\_log-in-link .secondary-link\_\_icon-wrapper, #pfe-n=
avigation .pfe-navigation\_\_log-in-link \> pfe-icon, #pfe-navigation
.pfe-nav= igation\_\_menu-link .secondary-link\_\_icon-wrapper,
#pfe-navigation .pfe-navi= gation\_\_menu-link \> pfe-icon,
#pfe-navigation .pfe-navigation\_\_secondary-li= nk
.secondary-link\_\_icon-wrapper, #pfe-navigation
.pfe-navigation\_\_secondar= y-link \> pfe-icon, pfe-navigation
.pfe-navigation\_\_fallback-links a .second= ary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigation\_\_fallback-links a \> = pfe-icon,
pfe-navigation .pfe-navigation\_\_log-in-link .secondary-link\_\_icon=
-wrapper, pfe-navigation .pfe-navigation\_\_log-in-link \> pfe-icon,
pfe-navig= ation .pfe-navigation\_\_menu-link
.secondary-link\_\_icon-wrapper, pfe-navigat= ion
.pfe-navigation\_\_menu-link \> pfe-icon, pfe-navigation
.pfe-navigation\_\_= secondary-link .secondary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigatio= n\_\_secondary-link \> pfe-icon {
\--pfe-icon\--size: 18px; padding-right: 5px; = } \@media (min-width:
768px) { #pfe-navigation .pfe-navigation\_\_fallback-links a
.secondary-link\_\_icon-w= rapper, #pfe-navigation
.pfe-navigation\_\_fallback-links a \> pfe-icon, #pfe-= navigation
.pfe-navigation\_\_log-in-link .secondary-link\_\_icon-wrapper, #pfe=
-navigation .pfe-navigation\_\_log-in-link \> pfe-icon, #pfe-navigation
.pfe-n= avigation\_\_menu-link .secondary-link\_\_icon-wrapper,
#pfe-navigation .pfe-na= vigation\_\_menu-link \> pfe-icon,
#pfe-navigation .pfe-navigation\_\_secondary-= link
.secondary-link\_\_icon-wrapper, #pfe-navigation
.pfe-navigation\_\_second= ary-link \> pfe-icon, pfe-navigation
.pfe-navigation\_\_fallback-links a .seco= ndary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigation\_\_fallback-links a = \> pfe-icon,
pfe-navigation .pfe-navigation\_\_log-in-link .secondary-link\_\_ic=
on-wrapper, pfe-navigation .pfe-navigation\_\_log-in-link \> pfe-icon,
pfe-nav= igation .pfe-navigation\_\_menu-link
.secondary-link\_\_icon-wrapper, pfe-navig= ation
.pfe-navigation\_\_menu-link \> pfe-icon, pfe-navigation
.pfe-navigation= \_\_secondary-link .secondary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigat= ion\_\_secondary-link \> pfe-icon {
padding: 2px 0px 4px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation .pfe-navigation\_\_= fallback-links a
.secondary-link\_\_icon-wrapper, .pfe-navigation\--collapse-s=
econdary-links #pfe-navigation .pfe-navigation\_\_fallback-links a \>
pfe-icon= , .pfe-navigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation= \_\_log-in-link .secondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-seco= ndary-links #pfe-navigation
.pfe-navigation\_\_log-in-link \> pfe-icon, .pfe-n=
avigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_menu-l= ink .secondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-link= s #pfe-navigation
.pfe-navigation\_\_menu-link \> pfe-icon, .pfe-navigation\--c=
ollapse-secondary-links #pfe-navigation
.pfe-navigation\_\_secondary-link .se= condary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links #pfe-= navigation
.pfe-navigation\_\_secondary-link \> pfe-icon, .pfe-navigation\--col=
lapse-secondary-links pfe-navigation .pfe-navigation\_\_fallback-links a
.sec= ondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-na= vigation
.pfe-navigation\_\_fallback-links a \> pfe-icon, .pfe-navigation\--col=
lapse-secondary-links pfe-navigation .pfe-navigation\_\_log-in-link
.secondar= y-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-navigat= ion
.pfe-navigation\_\_log-in-link \> pfe-icon,
.pfe-navigation\--collapse-seco= ndary-links pfe-navigation
.pfe-navigation\_\_menu-link .secondary-link\_\_icon= -wrapper,
.pfe-navigation\--collapse-secondary-links pfe-navigation .pfe-nav=
igation\_\_menu-link \> pfe-icon,
.pfe-navigation\--collapse-secondary-links pf= e-navigation
.pfe-navigation\_\_secondary-link .secondary-link\_\_icon-wrapper,=
.pfe-navigation\--collapse-secondary-links pfe-navigation
.pfe-navigation\_\_= secondary-link \> pfe-icon { padding: 0px 16px 0px
0px; } #pfe-navigation .pfe-navigation\_\_fallback-links a pfe-icon,
#pfe-navigation= .pfe-navigation\_\_log-in-link pfe-icon,
#pfe-navigation .pfe-navigation\_\_me= nu-link pfe-icon, #pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon,= pfe-navigation
.pfe-navigation\_\_fallback-links a pfe-icon, pfe-navigation =
.pfe-navigation\_\_log-in-link pfe-icon, pfe-navigation
.pfe-navigation\_\_menu= -link pfe-icon, pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon { d= isplay: block; height:
18px; } #pfe-navigation .pfe-navigation\_\_fallback-links a\[class\],
#pfe-navigation .= pfe-navigation\_\_fallback-links a\[href\],
#pfe-navigation .pfe-navigation\_\_lo= g-in-link\[class\],
#pfe-navigation .pfe-navigation\_\_log-in-link\[href\], #pfe-=
navigation .pfe-navigation\_\_menu-link\[class\], #pfe-navigation
.pfe-navigati= on\_\_menu-link\[href\], #pfe-navigation
.pfe-navigation\_\_secondary-link\[class\]= , #pfe-navigation
.pfe-navigation\_\_secondary-link\[href\], pfe-navigation .pf=
e-navigation\_\_fallback-links a\[class\], pfe-navigation
.pfe-navigation\_\_fall= back-links a\[href\], pfe-navigation
.pfe-navigation\_\_log-in-link\[class\], pfe= -navigation
.pfe-navigation\_\_log-in-link\[href\], pfe-navigation .pfe-navigat=
ion\_\_menu-link\[class\], pfe-navigation
.pfe-navigation\_\_menu-link\[href\], pfe= -navigation
.pfe-navigation\_\_secondary-link\[class\], pfe-navigation .pfe-nav=
igation\_\_secondary-link\[href\] { align-items: center;
justify-content: cente= r; } #pfe-navigation
.pfe-navigation\_\_account-toggle, #pfe-navigation \[slot=3D\"a=
ccount\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-nav= igation
\[slot=3D\"account\"\] \> a\[href\] { align-items: center; appearance:
non= e; background: 0px 0px; border: 0px; cursor: pointer; font-family:
inherit;= margin: 0px; outline: 0px; position: relative; text-align:
center; text-de= coration: none; white-space: nowrap;
\--pfe-icon\--color: var(\--pfe-navigatio=
n\_\_nav-bar\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
co= lor:
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var(\--pfe-theme\--color\--=
ui-base\--text,#fff)); display: flex; flex-direction: column; font-size:
var= (\--pfe-navigation\--FontSize\--xs,12px); height:
var(\--pfe-navigation\_\_nav-ba= r\--Height,72px); justify-content:
flex-end; padding: 14px 8px; width: auto;= } \@media print {
#pfe-navigation .pfe-navigation\_\_account-toggle, #pfe-navigation
\[slot=3D= \"account\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-n= avigation
\[slot=3D\"account\"\] \> a\[href\] { display: none !important; } }
#pfe-navigation .pfe-navigation\_\_account-toggle:focus, #pfe-navigation
.pfe= -navigation\_\_account-toggle:hover, #pfe-navigation
\[slot=3D\"account\"\] \> a\[h= ref\]:focus, #pfe-navigation
\[slot=3D\"account\"\] \> a\[href\]:hover, pfe-navigat= ion
.pfe-navigation\_\_account-toggle:focus, pfe-navigation
.pfe-navigation\_\_= account-toggle:hover, pfe-navigation
\[slot=3D\"account\"\] \> a\[href\]:focus, pf= e-navigation
\[slot=3D\"account\"\] \> a\[href\]:hover { box-shadow: inset 4px 0 0= 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--u=
i-accent,#06c)); } #pfe-navigation
.pfe-navigation\_\_account-toggle:focus, #pfe-navigation \[slo=
t=3D\"account\"\] \> a\[href\]:focus, pfe-navigation
.pfe-navigation\_\_account-tog= gle:focus, pfe-navigation
\[slot=3D\"account\"\] \> a\[href\]:focus { outline: 0px= ; }
#pfe-navigation .pfe-navigation\_\_account-toggle:focus::after,
#pfe-navigati= on \[slot=3D\"account\"\] \> a\[href\]:focus::after,
pfe-navigation .pfe-navigatio= n\_\_account-toggle:focus::after,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\]= :focus::after {
border: 1px dashed; inset: 0px; content: \"\"; display: block= ;
position: absolute; } #pfe-navigation .pfe-navigation\_\_account-toggle
pfe-icon, #pfe-navigation \[= slot=3D\"account\"\] \> a\[href\]
pfe-icon, pfe-navigation .pfe-navigation\_\_accou= nt-toggle pfe-icon,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\] pfe-icon { =
pointer-events: none; } \@supports (display:grid) { #pfe-navigation
.pfe-navigation\_\_account-toggle, #pfe-navigation \[slot=3D=
\"account\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-n= avigation
\[slot=3D\"account\"\] \> a\[href\] { place-items: center; display:
grid= ; grid-template-rows: 26px 18px; } } #pfe-navigation
.pfe-navigation\_\_account-toggle\[class\]:focus, #pfe-navigati= on
.pfe-navigation\_\_account-toggle\[class\]:hover, #pfe-navigation
\[slot=3D\"a= ccount\"\] \> a\[href\]\[class\]:focus, #pfe-navigation
\[slot=3D\"account\"\] \> a\[hre= f\]\[class\]:hover, pfe-navigation
.pfe-navigation\_\_account-toggle\[class\]:focu= s, pfe-navigation
.pfe-navigation\_\_account-toggle\[class\]:hover, pfe-navigat= ion
\[slot=3D\"account\"\] \> a\[href\]\[class\]:focus, pfe-navigation
\[slot=3D\"acco= unt\"\] \> a\[href\]\[class\]:hover { box-shadow: inset
0 4px 0 0 var(\--pfe-naviga=
tion\_\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c));
} \@media print { #pfe-navigation .pfe-navigation\_\_account-toggle,
#pfe-navigation \[slot=3D= \"account\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-n= avigation
\[slot=3D\"account\"\] \> a\[href\] { display: none; } } #pfe-navigation
.pfe-navigation\_\_account-toggle pfe-icon, #pfe-navigation \[=
slot=3D\"account\"\] \> a\[href\] pfe-icon, pfe-navigation
.pfe-navigation\_\_accou= nt-toggle pfe-icon, pfe-navigation
\[slot=3D\"account\"\] \> a\[href\] pfe-icon { = \--pfe-icon\--size:
18px; padding: 2px 0px 4px; } \@media (min-width: 768px) {
#pfe-navigation .pfe-navigation\_\_account-toggle pfe-icon,
#pfe-navigation= \[slot=3D\"account\"\] \> a\[href\] pfe-icon,
pfe-navigation .pfe-navigation\_\_acc= ount-toggle pfe-icon,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\] pfe-icon = {
padding-right: 0px; } } #pfe-navigation
.pfe-navigation\_\_account-toggle:focus, #pfe-navigation .pfe=
-navigation\_\_account-toggle:hover, #pfe-navigation
.pfe-navigation\_\_account= -toggle\[aria-expanded=3D\"true\"\],
#pfe-navigation \[slot=3D\"account\"\] \> a\[hre= f\]\[href\]:focus,
#pfe-navigation \[slot=3D\"account\"\] \> a\[href\]\[href\]:hover, p=
fe-navigation .pfe-navigation\_\_account-toggle:focus, pfe-navigation
.pfe-na= vigation\_\_account-toggle:hover, pfe-navigation
.pfe-navigation\_\_account-tog= gle\[aria-expanded=3D\"true\"\],
pfe-navigation \[slot=3D\"account\"\] \> a\[href\]\[hr= ef\]:focus,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\]\[href\]:hover {
box-sh= adow: inset 0 4px 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--=
pfe-theme\--color\--ui-accent,#06c)); } #pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\], pf=
e-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\] { \--pf=
e-icon\--color:
var(\--pfe-navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme=
\--color\--text,#151515)); background:
var(\--pfe-navigation\_\_nav-bar\--toggle-=
-BackgroundColor\--active,var(\--pfe-theme\--color\--surface\--lightest,#fff));
= color:
var(\--pfe-navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme\--color-=
-text,#151515)); } #pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\]:foc= us,
pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\]:= focus {
outline: 0px; } #pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\]:foc=
us::after, pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"=
true\"\]:focus::after { border: 1px dashed
var(\--pfe-navigation\_\_nav-bar\--Col=
or\--active,var(\--pfe-theme\--color\--text,#151515)); inset: 0px;
content: \"\";= display: block; position: absolute; } #pfe-navigation
.pfe-navigation\_\_fallback-links, #pfe-navigation .pfe-navig=
ation\_\_menu, pfe-navigation .pfe-navigation\_\_fallback-links,
pfe-navigation= .pfe-navigation\_\_menu { font-size: inherit;
list-style: none; margin: 0px;= padding: 0px; } \@media (min-width:
768px) { #pfe-navigation .pfe-navigation\_\_fallback-links,
#pfe-navigation .pfe-nav= igation\_\_menu, pfe-navigation
.pfe-navigation\_\_fallback-links, pfe-navigati= on
.pfe-navigation\_\_menu { align-items: stretch; display: flex; } }
#pfe-navigation .pfe-navigation\_\_fallback-links li, #pfe-navigation
.pfe-na= vigation\_\_menu li, pfe-navigation
.pfe-navigation\_\_fallback-links li, pfe-n= avigation
.pfe-navigation\_\_menu li { font-size: inherit; margin: 0px; paddi= ng:
0px; } #pfe-navigation .pfe-navigation\_\_fallback-links li::before,
#pfe-navigation= .pfe-navigation\_\_menu li::before, pfe-navigation
.pfe-navigation\_\_fallback= -links li::before, pfe-navigation
.pfe-navigation\_\_menu li::before { conten= t: none; } #pfe-navigation
.pfe-navigation\_\_fallback-links, pfe-navigation .pfe-naviga=
tion\_\_fallback-links { margin-left: auto; } #pfe-navigation
.pfe-navigation\_\_menu-link, pfe-navigation .pfe-navigation\_=
\_menu-link { display: flex; font-size:
var(\--pf-global\--FontSize\--md,1rem);= white-space: nowrap; }
#pfe-navigation.pfe-navigation\--processed,
pfe-navigation.pfe-navigation\--p= rocessed { display: block; padding:
0px; } #pfe-navigation.pfe-navigation\--processed::before,
pfe-navigation.pfe-navig= ation\--processed::before { content: none; }
#pfe-navigation.pfe-navigation\--processed \> \[slot=3D\"account\"\],
#pfe-naviga= tion.pfe-navigation\--processed \> \[slot=3D\"search\"\],
#pfe-navigation.pfe-nav= igation\--processed \>
\[slot=3D\"secondary-links\"\], pfe-navigation.pfe-navigat=
ion\--processed \> \[slot=3D\"account\"\],
pfe-navigation.pfe-navigation\--process= ed \> \[slot=3D\"search\"\],
pfe-navigation.pfe-navigation\--processed \> \[slot=3D=
\"secondary-links\"\] { height: auto; overflow: visible; visibility:
visible; = width: auto; } #pfe-navigation.pfe-navigation\--processed
pfe-navigation-dropdown, pfe-navi= gation.pfe-navigation\--processed
pfe-navigation-dropdown { display: block; = }
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown,
#pfe-n= avigation.pfe-navigation\--processed pfe-navigation-dropdown,
#pfe-navigatio= n.pfe-navigation\--processed \> \[slot\],
pfe-navigation.pfe-navigation\--proces= sed .pfe-navigation\_\_dropdown,
pfe-navigation.pfe-navigation\--processed pfe= -navigation-dropdown,
pfe-navigation.pfe-navigation\--processed \> \[slot\] { a= nimation:
auto ease 0s 1 normal none running none; opacity: 1; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\], pfe-n=
avigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] {
display: b= lock; height: auto; list-style: none; margin: 0px 0px 8px;
padding: 0px; wi= dth: auto; } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\], pfe=
-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] {
margin: = 0px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\], .pfe-navigation\--collapse-secondary-li=
nks pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] { m= argin: 0px 0px 8px; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a, #=
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> butto= n, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> butt= on { \--pfe-icon\--color:
var(\--pfe-navigation\_\_dropdown\--link\--Color,var(\--p=
fe-theme\--color\--link,#06c)); align-items: center; appearance: none;
backgr= ound: 0px 0px; border: 0px; color:
var(\--pfe-navigation\_\_dropdown\--link\--Co=
lor,var(\--pfe-theme\--color\--link,#06c)); cursor: pointer; display:
flex; fo= nt-family: inherit; font-size:
var(\--pf-global\--FontSize\--md,1rem); justify= -content: flex-start;
margin: 0px; outline: 0px; padding: 8px 24px; positio= n: relative;
text-align: center; text-decoration: none; white-space: nowrap= ; width:
100%; } \@media print { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> but= ton,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> = a, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> bu= tton { display: none !important; }
} \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> but= ton,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> = a, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> bu= tton { \--pfe-icon\--color:
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var=
(\--pfe-theme\--color\--ui-base\--text,#fff)); color:
var(\--pfe-navigation\_\_nav=
-bar\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
display:= flex; flex-direction: column; font-size:
var(\--pfe-navigation\--FontSize\--x= s,12px); height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); justify-conte= nt:
flex-end; padding: 14px 8px; width: auto; } \@supports (display:grid) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> but= ton,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> = a, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> bu= tton { place-items: center;
display: grid; grid-template-rows: 26px 18px; } }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a\[= class\]:focus,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a\[class\]:hover,
#pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> button\[class\]:focus,
#pfe-navigation.pfe-navigation= \--processed
\[slot=3D\"secondary-links\"\] \> button\[class\]:hover, pfe-navigatio=
n.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] \>
a\[class\]:focus, pf= e-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a\[class= \]:hover,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"=
\] \> button\[class\]:focus, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"= secondary-links\"\] \> button\[class\]:hover { box-shadow:
inset 0 4px 0 0 var(-=
-pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent=
,#06c)); } } #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:fo= cus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \>= a:hover,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-link=
s\"\] \> button:focus, #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> button:hover,
pfe-navigation.pfe-navigation\--processed \[slo=
t=3D\"secondary-links\"\] \> a:focus,
pfe-navigation.pfe-navigation\--processed =
\[slot=3D\"secondary-links\"\] \> a:hover,
pfe-navigation.pfe-navigation\--proces= sed
\[slot=3D\"secondary-links\"\] \> button:focus,
pfe-navigation.pfe-navigatio= n\--processed
\[slot=3D\"secondary-links\"\] \> button:hover { box-shadow: inset = 4px
0 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme\--c=
olor\--ui-accent,#06c)); } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:= focus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> a:hover,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-li=
nks\"\] \> button:focus, #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"se= condary-links\"\] \> button:hover,
pfe-navigation.pfe-navigation\--processed \[s=
lot=3D\"secondary-links\"\] \> a:focus,
pfe-navigation.pfe-navigation\--processe= d
\[slot=3D\"secondary-links\"\] \> a:hover,
pfe-navigation.pfe-navigation\--proc= essed
\[slot=3D\"secondary-links\"\] \> button:focus,
pfe-navigation.pfe-navigat= ion\--processed
\[slot=3D\"secondary-links\"\] \> button:hover { box-shadow: inse= t 0
4px 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme-=
-color\--ui-accent,#06c)); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a:focus,
.pfe-navigation\--collapse-se= condary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a:hover, .pfe-navigation\--collapse-secondary-links
#pfe-navigatio= n.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> button:focus, .pfe=
-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--proce= ssed
\[slot=3D\"secondary-links\"\] \> button:hover,
.pfe-navigation\--collapse-s= econdary-links
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a:focus, .pfe-navigation\--collapse-secondary-links
pfe-navigation= .pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:hover, .pfe-navig=
ation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed \[s=
lot=3D\"secondary-links\"\] \> button:focus,
.pfe-navigation\--collapse-secondar= y-links
pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> button:hover { box-shadow: inset 4px
0 0 0 var(\--pfe-navigation\_\_nav-bar=
\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c)); }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:fo= cus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \>= button:focus,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a:focus, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"second= ary-links\"\] \> button:focus { outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:fo= cus::after,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-li=
nks\"\] \> button:focus::after,
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> a:focus::after,
pfe-navigation.pfe-navigation\--proc= essed
\[slot=3D\"secondary-links\"\] \> button:focus::after { border: 1px
dashed= ; inset: 0px; content: \"\"; display: block; position: absolute;
} #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a pf= e-icon,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"=
\] \> button pfe-icon, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> a pfe-icon,
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> button pfe-icon { pointer-events: none; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a .s= econdary-link\_\_icon-wrapper,
#pfe-navigation.pfe-navigation\--processed \[slo=
t=3D\"secondary-links\"\] \> a \> pfe-icon,
#pfe-navigation.pfe-navigation\--proc= essed
\[slot=3D\"secondary-links\"\] \> button
.secondary-link\_\_icon-wrapper, #p=
fe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> button= \> pfe-icon, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-li= nks\"\] \> a .secondary-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation\--pro= cessed
\[slot=3D\"secondary-links\"\] \> a \> pfe-icon,
pfe-navigation.pfe-naviga= tion\--processed
\[slot=3D\"secondary-links\"\] \> button .secondary-link\_\_icon-w=
rapper, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> button \> pfe-icon {
\--pfe-icon\--size: 18px; padding-right: 5px; } \@media (min-width:
768px) { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a = .secondary-link\_\_icon-wrapper,
#pfe-navigation.pfe-navigation\--processed \[s=
lot=3D\"secondary-links\"\] \> a \> pfe-icon,
#pfe-navigation.pfe-navigation\--pr= ocessed
\[slot=3D\"secondary-links\"\] \> button
.secondary-link\_\_icon-wrapper, =
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> butt= on \> pfe-icon,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a .secondary-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a \> pfe-icon,
pfe-navigation.pfe-navi= gation\--processed
\[slot=3D\"secondary-links\"\] \> button .secondary-link\_\_icon=
-wrapper, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links= \"\] \> button \> pfe-icon { padding: 2px
0px 4px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a .secondary-link\_\_icon-wrapper,
.pfe= -navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--proce= ssed
\[slot=3D\"secondary-links\"\] \> a \> pfe-icon,
.pfe-navigation\--collapse-s= econdary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary=
-links\"\] \> button .secondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-= secondary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondar=
y-links\"\] \> button \> pfe-icon,
.pfe-navigation\--collapse-secondary-links pf=
e-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> a .seco= ndary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-nav=
igation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] \> a
\> pfe-icon= , .pfe-navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--= processed
\[slot=3D\"secondary-links\"\] \> button
.secondary-link\_\_icon-wrapper= ,
.pfe-navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--= processed
\[slot=3D\"secondary-links\"\] \> button \> pfe-icon { padding: 0px 16p=
x 0px 0px; } #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a pf= e-icon,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"=
\] \> button pfe-icon, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> a pfe-icon,
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> button pfe-icon { display: block; height:
18px; } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:= focus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> button:focus,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondar=
y-links\"\] \> a:focus, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> button:focus { outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:= focus::after,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> button:focus::after,
pfe-navigation.pfe-navigation\--processed \[sl=
ot=3D\"secondary-links\"\] \> a:focus::after,
pfe-navigation.pfe-navigation\--pr= ocessed
\[slot=3D\"secondary-links\"\] \> button:focus::after { border: 1px
dash= ed
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var(\--pfe-theme\--color\--ui=
-base\--text,#fff)); inset: 0px; content: \"\"; display: block;
position: abso= lute; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a:focus,
.pfe-navigation\--collapse-se= condary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> button:focus, .pfe-navigation\--collapse-secondary-links
pfe-navig= ation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:focus, .pfe-=
navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--process= ed
\[slot=3D\"secondary-links\"\] \> button:focus { box-shadow: none; }
\@media (min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a\[= aria-expanded=3D\"true\"\],
#pfe-navigation.pfe-navigation\--processed \[slot=3D=
\"secondary-links\"\] \> button\[aria-expanded=3D\"true\"\],
pfe-navigation.pfe-nav= igation\--processed
\[slot=3D\"secondary-links\"\] \> a\[aria-expanded=3D\"true\"\], =
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> butto= n\[aria-expanded=3D\"true\"\] { \--pfe-icon\--color:
var(\--pfe-navigation\_\_nav-ba=
r\--Color\--active,var(\--pfe-theme\--color\--text,#151515));
background: var(\--=
pfe-navigation\_\_nav-bar\--toggle\--BackgroundColor\--active,var(\--pfe-theme\--c=
olor\--surface\--lightest,#fff)); color:
var(\--pfe-navigation\_\_nav-bar\--Color=
\--active,var(\--pfe-theme\--color\--text,#151515)); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a\[aria-expanded=3D\"true\"\],
.pfe-navig= ation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--processed \[=
slot=3D\"secondary-links\"\] \> button\[aria-expanded=3D\"true\"\],
.pfe-navigation= \--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> a\[aria-expanded=3D\"true\"\],
.pfe-navigation\--collaps= e-secondary-links
pfe-navigation.pfe-navigation\--processed \[slot=3D\"seconda=
ry-links\"\] \> button\[aria-expanded=3D\"true\"\] { background: 0px
0px; box-shad= ow: none; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown\_= \_wrapper\--single-column,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_custom-dropdown\_\_wrapper\--single-column { position:
relative; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown\_= \_wrapper,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_custom-=
dropdown\_\_wrapper { display: block; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe-n=
avigation\_\_dropdown-wrapper\[class\],
pfe-navigation.pfe-navigation\--processe= d
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class\] { hei= ght: 0px;
transition: var(\--pfe-navigation\--accordion-transition,height .25= s
ease-in-out); } \@media (prefers-reduced-motion) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe=
-navigation\_\_dropdown-wrapper\[class\],
pfe-navigation.pfe-navigation\--proces= sed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class\] { t= ransition: none; } }
\@media (min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe=
-navigation\_\_dropdown-wrapper\[class\],
pfe-navigation.pfe-navigation\--proces= sed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class\] { p= osition: absolute;
right: 0px; top: var(\--pfe-navigation\_\_nav-bar\--Height,7= 2px); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class= \],
.pfe-navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation-= -processed
\[slot=3D\"secondary-links\"\] .pfe-navigation\_\_dropdown-wrapper\[cla=
ss\] { position: static; } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe=
-navigation\_\_dropdown-wrapper\[class\]\[aria-hidden=3D\"false\"\],
pfe-navigation= .pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe-navigation\_\_drop=
down-wrapper\[class\]\[aria-hidden=3D\"false\"\] { height: auto; } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class=
\]\[aria-hidden=3D\"false\"\],
.pfe-navigation\--collapse-secondary-links pfe-nav=
igation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
.pfe-navigatio=
n\_\_dropdown-wrapper\[class\]\[aria-hidden=3D\"false\"\] { height: 0px;
} #pfe-navigation.pfe-navigation\--processed\[breakpoint=3D\"mobile\"\]
\[slot=3D\"s= econdary-links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wrapper, pfe-navi=
gation.pfe-navigation\--processed\[breakpoint=3D\"mobile\"\]
\[slot=3D\"secondary-= links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wrapper { left: calc(100vw= -
var(\--pfe-navigation\_\_mobile-dropdown\--PaddingHorizontal,32px));
positio= n: absolute; top: 0px; width: 100vw; }
#pfe-navigation.pfe-navigation\--processed\[breakpoint=3D\"mobile\"\]
\[slot=3D\"s= econdary-links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wrapper\[aria-hidd= en=3D\"false\"\],
pfe-navigation.pfe-navigation\--processed\[breakpoint=3D\"mobil= e\"\]
\[slot=3D\"secondary-links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wra= pper\[aria-hidden=3D\"false\"\] {
height: calc(100vh - var(\--pfe-navigation\_\_na= v-bar\--Height,72px));
overflow-y: scroll; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-w= rapper\--default-styles,
#pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_site-switcher .pfe-navigation\_\_dropdown-wrapper,
pfe-navigation.pfe= -navigation\--processed
.pfe-navigation-item\_\_tray\--container, pfe-navigatio=
n.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styl= es,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher= .pfe-navigation\_\_dropdown-wrapper {
background: var(\--pfe-navigation\_\_drop=
down\--Background,var(\--pfe-theme\--color\--surface\--lightest,#fff));
padding:= 0
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--mobile,24px);
} \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--con= tainer,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown=
-wrapper\--default-styles, #pfe-navigation.pfe-navigation\--processed
.pfe-na= vigation\_\_site-switcher .pfe-navigation\_\_dropdown-wrapper,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation-item\_\_tray\--container, pfe-navigat=
ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switch= er .pfe-navigation\_\_dropdown-wrapper {
padding: 0 var(\--pfe-navigation\_\_dro=
pdown\--full-width\--spacing\--desktop,64px)
var(\--pfe-navigation\_\_dropdown\--f=
ull-width\--spacing\--mobile,24px); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation-item\_\_tray\--container, .pfe-navigation\--collapse-s=
econdary-links #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_d= ropdown-wrapper\--default-styles,
.pfe-navigation\--collapse-secondary-links =
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown-wrapper,
.pfe-navigation\--collapse-secondary-links =
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner,
.pfe-navigation\--collapse-secondary-links pfe-navigation.pfe-navigatio=
n\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles,
.pfe-naviga= tion\--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_site-switcher .pfe-navigation\_\_dropdown-wrapper {
padding: 0 =
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--mobile,24px);
} #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown=
-wrapper\--default-styles a, pfe-navigation.pfe-navigation\--processed
.pfe-n= avigation-item\_\_tray\--container a,
pfe-navigation.pfe-navigation\--processed=
.pfe-navigation\_\_dropdown-wrapper\--default-styles a { border: 1px
solid tr= ansparent; color:
var(\--pfe-navigation\_\_dropdown\--link\--Color,var(\--pfe-the=
me\--color\--link,#06c)); display: inline-block; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-ite=
m\_\_tray\--container a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-=
navigation\_\_dropdown-wrapper\--default-styles a:focus,
#pfe-navigation.pfe-n= avigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a:ho= ver,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--c= ontainer a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-=
item\_\_tray\--container a:hover,
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_dropdown-wrapper\--default-styles a:focus,
pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a:h= over { color:
var(\--pfe-navigation\_\_dropdown\--link\--Color\--hover,#036); tex=
t-decoration: underline; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dr=
opdown-wrapper\--default-styles a:focus,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container a:focus,
pfe-navigation.pfe-nav= igation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a:focu= s { border:
1px dashed; outline: 0px; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header,
#pfe-navigation.pfe-navigation\--processed .pfe=
-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading-level\], #=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner h2,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tra=
y\--container h3, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-= item\_\_tray\--container h4,
#pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation-item\_\_tray\--container h5,
#pfe-navigation.pfe-navigation\--processe= d
.pfe-navigation-item\_\_tray\--container h6,
#pfe-navigation.pfe-navigation-= -processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles .pfe-link-list=
\--header, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdo= wn-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-level\], #pfe-nav=
igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles h2,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dro=
pdown-wrapper\--default-styles h3,
#pfe-navigation.pfe-navigation\--processed=
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4,
#pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5,=
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h6,
pfe-navigation.pfe-navigation\--processed .pfe-navigat=
ion-item\_\_tray\--container .pfe-link-list\--header,
pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation-item\_\_tray\--container \[role=3D\"heading\"\]\[ar=
ia-heading-level\], pfe-navigation.pfe-navigation\--processed
.pfe-navigation= -item\_\_tray\--container h2,
pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation-item\_\_tray\--container h3,
pfe-navigation.pfe-navigation\--processed=
.pfe-navigation-item\_\_tray\--container h4,
pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation-item\_\_tray\--container h5, pfe-navigation.pfe-navig=
ation\--processed .pfe-navigation-item\_\_tray\--container h6,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles =
.pfe-link-list\--header, pfe-navigation.pfe-navigation\--processed
.pfe-navig= ation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-lev= el\],
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wra= pper\--default-styles h2,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_dropdown-wrapper\--default-styles h3,
pfe-navigation.pfe-navigation-= -processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4, pfe-naviga=
tion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-s= tyles h5,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles h6 { margin:
var(\--pfe-navigation\--gutter,32px) 0= .75em; padding: 0px;
break-inside: avoid; color: var(\--pfe-navigation\_\_dro=
pdown\--headings\--Color,#464646); font-family:
var(\--pfe-navigation\--FontFam= ilyHeadline,Red Hat
Display,RedHatDisplay,Arial,Helvetica,sans-serif); font= -size:
var(\--pf-global\--FontSize\--lg,1.125rem); font-weight: 500; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner
.pfe-link-list\--header:first-child,
#pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-headi= ng-level\]:first-child,
#pfe-navigation.pfe-navigation\--processed .pfe-navig=
ation-item\_\_tray\--container h2:first-child,
#pfe-navigation.pfe-navigation-= -processed
.pfe-navigation-item\_\_tray\--container h3:first-child, #pfe-navig=
ation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h4:fi= rst-child,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_=
tray\--container h5:first-child,
#pfe-navigation.pfe-navigation\--processed .=
pfe-navigation-item\_\_tray\--container h6:first-child,
#pfe-navigation.pfe-na= vigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles .pfe-=
link-list\--header:first-child,
#pfe-navigation.pfe-navigation\--processed .p=
fe-navigation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-hea= ding-level\]:first-child,
#pfe-navigation.pfe-navigation\--processed .pfe-nav=
igation\_\_dropdown-wrapper\--default-styles h2:first-child,
#pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles = h3:first-child,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_=
dropdown-wrapper\--default-styles h4:first-child,
#pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5:first-= child,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown-=
wrapper\--default-styles h6:first-child,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container
.pfe-link-list\--header:first-ch= ild,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--c= ontainer
\[role=3D\"heading\"\]\[aria-heading-level\]:first-child,
pfe-navigation= .pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h2:first-c= hild,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--= container h3:first-child,
pfe-navigation.pfe-navigation\--processed .pfe-nav=
igation-item\_\_tray\--container h4:first-child,
pfe-navigation.pfe-navigation= \--processed
.pfe-navigation-item\_\_tray\--container h5:first-child, pfe-navig=
ation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h6:fi= rst-child,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdo=
wn-wrapper\--default-styles .pfe-link-list\--header:first-child,
pfe-navigati= on.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-sty= les
\[role=3D\"heading\"\]\[aria-heading-level\]:first-child,
pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2:= first-child,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_drop=
down-wrapper\--default-styles h3:first-child,
pfe-navigation.pfe-navigation-= -processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4:first-child= ,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h5:first-child,
pfe-navigation.pfe-navigation\--processed =
.pfe-navigation\_\_dropdown-wrapper\--default-styles h6:first-child {
margin-t= op: 0px; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header a,
#pfe-navigation.pfe-navigation\--processed .p=
fe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading-level\] = a,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--co= ntainer h2 a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-ite=
m\_\_tray\--container h3 a, #pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation-item\_\_tray\--container h4 a,
#pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation-item\_\_tray\--container h5 a,
#pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation-item\_\_tray\--container h6 a, #pfe-navigation.p=
fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles =
.pfe-link-list\--header a, #pfe-navigation.pfe-navigation\--processed
.pfe-na= vigation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-= level\] a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdo=
wn-wrapper\--default-styles h2 a,
#pfe-navigation.pfe-navigation\--processed =
.pfe-navigation\_\_dropdown-wrapper\--default-styles h3 a,
#pfe-navigation.pfe= -navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4= a,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wra= pper\--default-styles h5 a,
#pfe-navigation.pfe-navigation\--processed .pfe-n=
avigation\_\_dropdown-wrapper\--default-styles h6 a,
pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation-item\_\_tray\--container .pfe-link-list\--heade= r a,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--c= ontainer
\[role=3D\"heading\"\]\[aria-heading-level\] a,
pfe-navigation.pfe-navig= ation\--processed
.pfe-navigation-item\_\_tray\--container h2 a, pfe-navigation=
.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container h3
a, pfe-= navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container = h4 a,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--= container h5 a,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-it=
em\_\_tray\--container h6 a, pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation\_\_dropdown-wrapper\--default-styles
.pfe-link-list\--header a, pfe-nav= igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a,
pfe-navigation.pfe-navig= ation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2 a, pf=
e-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--d= efault-styles h3 a,
pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--default-styles h4 a,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5 a, pfe-navigat=
ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles h6 a { border:
1px solid transparent; color: var(\--pfe-navigation\_\_dro=
pdown\--headings\--Color,#464646); text-decoration: underline; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header
a:focus, #pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation-item\_\_tray\--container .pfe-link-list\--header
a:hover, #= pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner
\[role=3D\"heading\"\]\[aria-heading-level\] a:focus,
#pfe-navigation.pfe-nav= igation\--processed
.pfe-navigation-item\_\_tray\--container \[role=3D\"heading\"\]=
\[aria-heading-level\] a:hover,
#pfe-navigation.pfe-navigation\--processed .pf=
e-navigation-item\_\_tray\--container h2 a:focus,
#pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation-item\_\_tray\--container h2 a:hover, #pfe-naviga=
tion.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
h3 a:f= ocus, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray-= -container h3 a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-navig=
ation-item\_\_tray\--container h4 a:focus,
#pfe-navigation.pfe-navigation\--pro= cessed
.pfe-navigation-item\_\_tray\--container h4 a:hover, #pfe-navigation.pf=
e-navigation\--processed .pfe-navigation-item\_\_tray\--container h5
a:focus, #= pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner h5 a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-i=
tem\_\_tray\--container h6 a:focus,
#pfe-navigation.pfe-navigation\--processed =
.pfe-navigation-item\_\_tray\--container h6 a:hover,
#pfe-navigation.pfe-navig= ation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles .pfe-lin=
k-list\--header a:focus, #pfe-navigation.pfe-navigation\--processed
.pfe-navi= gation\_\_dropdown-wrapper\--default-styles
.pfe-link-list\--header a:hover, #p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--= default-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a:focus, #pfe-navigat=
ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles
\[role=3D\"heading\"\]\[aria-heading-level\] a:hover,
#pfe-navigation.pfe-na= vigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2 a:= focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown-=
wrapper\--default-styles h2 a:hover,
#pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h3 a:focus,
#pfe-navig= ation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-= styles h3 a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--default-styles h4 a:focus,
#pfe-navigation.pfe-navigat= ion\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4 a:hover= ,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapp= er\--default-styles h5 a:focus,
#pfe-navigation.pfe-navigation\--processed .p=
fe-navigation\_\_dropdown-wrapper\--default-styles h5 a:hover,
#pfe-navigation= .pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-style= s h6 a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dr=
opdown-wrapper\--default-styles h6 a:hover,
pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation-item\_\_tray\--container .pfe-link-list\--header a:foc=
us, pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--co= ntainer .pfe-link-list\--header
a:hover, pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading= -level\] a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-i=
tem\_\_tray\--container \[role=3D\"heading\"\]\[aria-heading-level\]
a:hover, pfe-na= vigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h2= a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tr=
ay\--container h2 a:hover, pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation-item\_\_tray\--container h3 a:focus,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation-item\_\_tray\--container h3 a:hover, pfe-navigation.pf=
e-navigation\--processed .pfe-navigation-item\_\_tray\--container h4
a:focus, p= fe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contain= er h4 a:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-ite=
m\_\_tray\--container h5 a:focus,
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation-item\_\_tray\--container h5 a:hover,
pfe-navigation.pfe-navigatio= n\--processed
.pfe-navigation-item\_\_tray\--container h6 a:focus, pfe-navigati=
on.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
h6 a:hov= er, pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrap= per\--default-styles
.pfe-link-list\--header a:focus, pfe-navigation.pfe-navi=
gation\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
.pfe-li= nk-list\--header a:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-le= vel\] a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dro=
pdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a:hove= r,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapp= er\--default-styles h2 a:focus,
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_dropdown-wrapper\--default-styles h2 a:hover,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles = h3 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropd=
own-wrapper\--default-styles h3 a:hover,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4 a:focus,
pfe-nav= igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles h4 a:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navigati=
on\_\_dropdown-wrapper\--default-styles h5 a:focus,
pfe-navigation.pfe-navigat= ion\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5 a:hover= ,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h6 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe=
-navigation\_\_dropdown-wrapper\--default-styles h6 a:hover { color:
var(\--pfe= -navigation\_\_dropdown\--link\--Color\--hover,#036);
text-decoration: none; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header
a:focus, #pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading-l= evel\] a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-it=
em\_\_tray\--container h2 a:focus,
#pfe-navigation.pfe-navigation\--processed .=
pfe-navigation-item\_\_tray\--container h3 a:focus,
#pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation-item\_\_tray\--container h4 a:focus, #pfe-navi=
gation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h5 a= :focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tra=
y\--container h6 a:focus, #pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation\_\_dropdown-wrapper\--default-styles
.pfe-link-list\--header a:focus, #=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper-= -default-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a:focus, #pfe-naviga=
tion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-s= tyles h2 a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation=
\_\_dropdown-wrapper\--default-styles h3 a:focus,
#pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4 a:focus,=
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h5 a:focus,
#pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_dropdown-wrapper\--default-styles h6 a:focus,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation-item\_\_tray\--container .pfe-link-li= st\--header
a:focus, pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n-item\_\_tray\--container \[role=3D\"heading\"\]\[aria-heading-level\]
a:focus, pfe= -navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container= h2 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_=
\_tray\--container h3 a:focus, pfe-navigation.pfe-navigation\--processed
.pfe-= navigation-item\_\_tray\--container h4 a:focus,
pfe-navigation.pfe-navigation-= -processed
.pfe-navigation-item\_\_tray\--container h5 a:focus, pfe-navigation=
.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container h6
a:focus= , pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles
.pfe-link-list\--header a:focus, pfe-navigation.pfe-naviga=
tion\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
\[role=3D\"= heading\"\]\[aria-heading-level\] a:focus,
pfe-navigation.pfe-navigation\--proce= ssed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2 a:focus,
pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default= -styles h3 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--default-styles h4 a:focus,
pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5 a:focus,=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--default-styles h6 a:focus {
border: 1px dashed; outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner li,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles li, pfe-navigation.pfe-navigation\--processed
.pfe= -navigation-item\_\_tray\--container li,
pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation\_\_dropdown-wrapper\--default-styles li { margin: 0px
0px = 16px; break-inside: avoid; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tra=
y\--container pfe-card, #pfe-navigation.pfe-navigation\--processed
.pfe-navig= ation-item\_\_tray\--container pfe-cta,
#pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a,
#pfe-navigation.pf= e-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles p= fe-card,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles pfe-cta,
pfe-navigation.pfe-navigation\--processed=
.pfe-navigation-item\_\_tray\--container a,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation-item\_\_tray\--container pfe-card, pfe-navigation.pfe-=
navigation\--processed .pfe-navigation-item\_\_tray\--container pfe-cta,
pfe-na= vigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defau= lt-styles a,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_drop=
down-wrapper\--default-styles pfe-card,
pfe-navigation.pfe-navigation\--proce= ssed
.pfe-navigation\_\_dropdown-wrapper\--default-styles pfe-cta {
break-insi= de: avoid; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner
pfe-cta\[pfe-priority=3D\"primary\"\],
#pfe-navigation.pfe-navigation\--pro= cessed
.pfe-navigation-item\_\_tray\--container
pfe-cta\[priority=3D\"primary\"\],=
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles
pfe-cta\[pfe-priority=3D\"primary\"\], #pfe-navigation.pfe-na=
vigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles pfe-c=
ta\[priority=3D\"primary\"\], pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation-item\_\_tray\--container
pfe-cta\[pfe-priority=3D\"primary\"\], pfe-naviga=
tion.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
pfe-ct= a\[priority=3D\"primary\"\],
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-priority=3D\"primary\"\],=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--default-styles
pfe-cta\[priority=3D\"primary\"\] { \--pfe-cta\--BackgroundColor= :
var(\--pfe-navigation\_\_dropdown\--pfe-cta\--BackgroundColor,#e00);
\--pfe-cta= \--BackgroundColor\--hover:
var(\--pfe-navigation\_\_dropdown\--pfe-cta\--hover\--B=
ackgroundColor,#c00); \--pfe-theme\--ui\--border-width: 0; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner
pfe-cta\[pfe-priority=3D\"primary\"\]:focus,
#pfe-navigation.pfe-navigatio= n\--processed
.pfe-navigation-item\_\_tray\--container pfe-cta\[pfe-priority=3D\"=
primary\"\]:hover, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-= item\_\_tray\--container
pfe-cta\[priority=3D\"primary\"\]:focus, #pfe-navigation.=
pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
pfe-cta\[pri= ority=3D\"primary\"\]:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-priority=3D\"primary\"= \]:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles pfe-cta\[pfe-priority=3D\"primary\"\]:hover,
#pfe-nav= igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles
pfe-cta\[priority=3D\"primary\"\]:focus, #pfe-navigation.pfe-navigatio=
n\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[prio= rity=3D\"primary\"\]:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation-item\_\_tray\--container
pfe-cta\[pfe-priority=3D\"primary\"\]:focus, pfe-n=
avigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container p=
fe-cta\[pfe-priority=3D\"primary\"\]:hover,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container
pfe-cta\[priority=3D\"primary\"\]:f= ocus,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--= container
pfe-cta\[priority=3D\"primary\"\]:hover, pfe-navigation.pfe-navigatio=
n\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-= priority=3D\"primary\"\]:focus,
pfe-navigation.pfe-navigation\--processed .pfe-=
navigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-priority=3D\"primar= y\"\]:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdo=
wn-wrapper\--default-styles pfe-cta\[priority=3D\"primary\"\]:focus,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles
pfe-cta\[priority=3D\"primary\"\]:hover { \--pfe-cta\--BackgroundColor:
var(=
\--pfe-navigation\_\_dropdown\--pfe-cta\--hover\--BackgroundColor,#c00);
} pfe-card #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tr= ay\--container pfe-cta, pfe-card
#pfe-navigation.pfe-navigation\--processed .=
pfe-navigation\_\_dropdown-wrapper\--default-styles pfe-cta, pfe-card
pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container pfe-= cta, pfe-card
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dro=
pdown-wrapper\--default-styles pfe-cta { margin-top: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner li,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tr=
ay\--container ul, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation= \_\_dropdown-wrapper\--default-styles li,
#pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_dropdown-wrapper\--default-styles ul,
pfe-navigation.= pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container li, pfe-nav=
igation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container ul,=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--default-styles li,
pfe-navigation.pfe-navigation\--processed .pfe-navigati=
on\_\_dropdown-wrapper\--default-styles ul { list-style: none; margin:
0px; pa= dding: 0px; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-grid, #pfe-naviga= tion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles, p=
fe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigatio= n.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { col= or:
var(\--pfe-navigation\_\_dropdown\--Color,#151515); column-count: auto;
dis= play: block; font-size: var(\--pf-global\--FontSize\--md,1rem);
gap: 0px; marg= in-left: auto; margin-right: auto; max-width:
var(\--pfe-navigation\--content= -max-width,1136px); padding-bottom:
12px; padding-top: 12px; width: calc(10= 0% + 32px); } \@media
(min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-grid, #pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles,=
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { c= olumn-count: 3;
display: block; gap: var(\--pfe-navigation\--gutter,32px); pa=
dding-bottom: 12px; padding-top: 12px; } } \@media (min-width: 1200px) {
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
#pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles,=
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { c= olumn-count: auto;
display: flex; flex-wrap: wrap; padding-bottom: 32px; pa= dding-top:
32px; } \@supports (display:grid) {
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
#pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles,=
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { d= isplay: grid; gap:
var(\--pfe-navigation\--gutter,32px); grid-auto-flow: row;=
grid-template-columns: repeat(4, minmax(0px, 1fr)); } } }
.pfe-navigation\--collapse-main-menu
#pfe-navigation.pfe-navigation\--process= ed .pfe-navigation-grid,
.pfe-navigation\--collapse-main-menu #pfe-navigatio=
n.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles, .pfe=
-navigation\--collapse-main-menu
pfe-navigation.pfe-navigation\--processed .p= fe-navigation-grid,
.pfe-navigation\--collapse-main-menu pfe-navigation.pfe-=
navigation\--processed .pfe-navigation\_\_dropdown\--default-styles {
column-co= unt: 3; display: block; gap:
var(\--pfe-navigation\--gutter,32px); padding-bo= ttom: 12px;
padding-top: 12px; } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed .pfe-navigation-grid,
.pfe-navigation\--collapse-secondary-links #p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-= styles,
.pfe-navigation\--collapse-secondary-links pfe-navigation.pfe-naviga=
tion\--processed .pfe-navigation-grid,
.pfe-navigation\--collapse-secondary-l= inks
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--de= fault-styles { column-count: auto;
display: block; gap: 0px; margin-left: -= 16px; margin-right: -16px;
max-width: var(\--pfe-navigation\--content-max-wid= th,1136px);
padding-bottom: 12px; padding-top: 12px; width: calc(100% + 32p= x); }
.pfe-navigation\_\_menu-item\--open
#pfe-navigation.pfe-navigation\--processed = .pfe-navigation-grid,
.pfe-navigation\_\_menu-item\--open #pfe-navigation.pfe-=
navigation\--processed .pfe-navigation\_\_dropdown\--default-styles,
.pfe-navig= ation\_\_menu-item\--open
pfe-navigation.pfe-navigation\--processed .pfe-naviga= tion-grid,
.pfe-navigation\_\_menu-item\--open pfe-navigation.pfe-navigation\--=
processed .pfe-navigation\_\_dropdown\--default-styles {
transition-delay: 0s;= visibility: visible; }
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*,
#pfe-na= vigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-style= s \> \*,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*, p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-= styles \> \* { margin: 0px 0px
18px; break-inside: avoid; } \@media (min-width: 1200px) {
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*,
#pfe-= navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-sty= les \> \*,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*,=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--defaul= t-styles \> \* { margin: 0px; } }
.pfe-navigation\--collapse-main-menu
#pfe-navigation.pfe-navigation\--process= ed .pfe-navigation-grid \> \*,
.pfe-navigation\--collapse-main-menu #pfe-navig=
ation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles \>= \*,
.pfe-navigation\--collapse-main-menu
pfe-navigation.pfe-navigation\--proc= essed .pfe-navigation-grid \> \*,
.pfe-navigation\--collapse-main-menu pfe-nav=
igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles= \> \* { margin: 0px 0px
18px; } #pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed .pfe-navigation-grid {
max-width: 100%; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--1-x, p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--1-x { di= splay: block; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_site-switcher .pfe-navigation\_\_dropdown { background:
rgb(255, 255,= 255); } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown
site-switcher, pfe-navigation.pfe-navigation\--proce= ssed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switcher= { margin-left: auto; margin-right: auto; max-width:
var(\--pfe-navigation\--= content-max-width,1136px); padding: 12px
var(\--pfe-navigation\_\_dropdown\--fu=
ll-width\--spacing\--mobile,24px); } \@media (min-width: 1200px) {
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher = .pfe-navigation\_\_dropdown
site-switcher, pfe-navigation.pfe-navigation\--pro= cessed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switch= er { padding: 32px
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--des=
ktop,64px); } } .pfe-navigation\--collapse-main-menu
#pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switcher, = .pfe-navigation\--collapse-main-menu
pfe-navigation.pfe-navigation\--processe= d
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switcher { = padding: 12px
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--mobile,2=
4px); } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown
site-switcher .container, pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown si=
te-switcher .container { margin: 0px; padding: 0px; width: auto; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--invisible\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--invisible\[class\] { padding: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--invisible
pfe-navigation-dropdown, pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation\_\_dropdown-wrapper\--invisible pfe-navigation-dropdown
{ v= isibility: hidden; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown-= -single-column\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-naviga=
tion\_\_custom-dropdown\--single-column\[class\] { padding: 0px; }
\@media (min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdow= n\--single-column\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_custom-dropdown\--single-column\[class\] { box-shadow:
var(\--pfe-navig= ation\_\_dropdown\--BoxShadow,0 1px 2px
rgba(0,0,0,.12)); max-width: 100%; min= -width: 13em; padding: 0px 32px;
position: absolute; top: 100%; } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation\_\_custom-dropdown\--single-column\[class\], .pfe-navig=
ation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed .p=
fe-navigation\_\_custom-dropdown\--single-column\[class\] { box-shadow:
none; ma= x-width: 100%; position: static; } \@media (min-width: 768px)
{ #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdow= n\--single-column\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_custom-dropdown\--single-column\[class\] { right: 0px; } }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown-= -full\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_cus=
tom-dropdown\--full\[class\] { width: 100%; } \@media (min-width: 768px)
{ #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdow= n\--full\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_c=
ustom-dropdown\--full\[class\] { left: 0px; position: absolute; right:
0px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation\_\_custom-dropdown\--full\[class\],
.pfe-navigation\--co= llapse-secondary-links
pfe-navigation.pfe-navigation\--processed .pfe-naviga=
tion\_\_custom-dropdown\--full\[class\] { position: static; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown-= -full\[class\]
.pfe-navigation\_\_dropdown, pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_custom-dropdown\--full\[class\]
.pfe-navigation\_\_dropdo= wn { width: 100%; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_search\--d=
efault-styles { padding-left: 16px; padding-right: 16px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles form,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_sear=
ch\--default-styles form { align-items: center; display: flex; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_s=
earch\--default-styles input, pfe-navigation.pfe-navigation\--processed
.pfe-= navigation\_\_search\--default-styles button,
pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation\_\_search\--default-styles input { padding: 10px; tra=
nsition: box-shadow 0.2s; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_sea=
rch\--default-styles input { border-width: 1px; border-style: solid;
border-= color: rgb(240, 240, 240) rgb(240, 240, 240) rgb(139, 142,
145); border-ima= ge: initial; color: rgb(113, 117, 121); flex: 1 1 0%;
font-size: var(\--pf-g= lobal\--FontSize\--md,1rem); margin-right: 8px;
} #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input::placeholder,
pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation\_\_search\--default-styles input::placeholder { color: rgb(113,
117, = 121); } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_se=
arch\--default-styles button { background-color: rgb(238, 0, 0); border:
1px= solid rgb(238, 0, 0); border-radius: 2px; color: rgb(255, 255,
255); flex:= 0 1 auto; font-size:
var(\--pf-global\--FontSize\--md,1rem); }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigati=
on\_\_search\--default-styles input:hover,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_search\--default-styles input:focus,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_search\--default-styles input:hove= r { outline: 0px;
} #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input:focus::after,
#pfe-navigation.pfe-navigation\--processed .pfe-n=
avigation\_\_search\--default-styles input:hover::after,
pfe-navigation.pfe-na= vigation\--processed
.pfe-navigation\_\_search\--default-styles input:focus::af= ter,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--defa= ult-styles input:hover::after {
border: 1px dashed rgb(0, 0, 0); inset: 0px= ; content: \"\"; display:
block; position: absolute; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigat=
ion\_\_search\--default-styles button:hover,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation\_\_search\--default-styles button:focus, pfe-navigatio=
n.pfe-navigation\--processed .pfe-navigation\_\_search\--default-styles
button:= hover { outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button:focus::after,
#pfe-navigation.pfe-navigation\--processed .pfe-=
navigation\_\_search\--default-styles button:hover::after,
pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_search\--default-styles button:focus:= :after,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_search\--d=
efault-styles button:hover::after { border: 1px dashed rgb(255, 255,
255); = inset: 0px; content: \"\"; display: block; position: absolute; }
#pfe-navigation .pfe-navigation\_\_site-switcher\_\_back-wrapper,
pfe-navigatio= n .pfe-navigation\_\_site-switcher\_\_back-wrapper {
border-bottom: var(\--pfe-n=
avigation\_\_dropdown\--separator\--Border,1px solid
var(\--pfe-theme\--color\--ui= \--border\--lighter,#d2d2d2)); display:
block; } \@media (min-width: 768px) { #pfe-navigation
.pfe-navigation\_\_site-switcher\_\_back-wrapper, pfe-navigat= ion
.pfe-navigation\_\_site-switcher\_\_back-wrapper { display: none; } }
.pfe-navigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_= site-switcher\_\_back-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-= navigation
.pfe-navigation\_\_site-switcher\_\_back-wrapper { display: block; }
#pfe-navigation .pfe-navigation\_\_site-switcher\_\_back-button,
pfe-navigation= .pfe-navigation\_\_site-switcher\_\_back-button {
background-color: transparen= t; border: 1px solid transparent; color:
var(\--pfe-navigation\_\_dropdown\--li=
nk\--Color,var(\--pfe-theme\--color\--link,#06c)); cursor: pointer;
font-size: = var(\--pf-global\--FontSize\--md,1rem); padding: 21px 21px
21px 45px; position= : relative; text-align: left; width: 100%; }
#pfe-navigation .pfe-navigation\_\_site-switcher\_\_back-button::before,
pfe-na= vigation .pfe-navigation\_\_site-switcher\_\_back-button::before
{ border-botto= m-color: ; border-bottom-style: ; border-bottom-width: ;
border-left-color:= ; border-left-style: ; border-left-width: ;
border-image-source: ; border-= image-slice: ; border-image-width: ;
border-image-outset: ; border-image-re= peat: ; border-right: 0px;
border-top: 0px; content: \"\"; display: block; he= ight: 8px; left:
35px; position: absolute; right: auto; top: 27px; transfor= m:
rotate(45deg); transform-origin: left top; width: 8px; } #pfe-navigation
.pfe-navigation\_\_site-switcher\_\_back-button:focus, #pfe-nav= igation
.pfe-navigation\_\_site-switcher\_\_back-button:hover, pfe-navigation .=
pfe-navigation\_\_site-switcher\_\_back-button:focus, pfe-navigation
.pfe-navig= ation\_\_site-switcher\_\_back-button:hover { border: 1px
dashed var(\--pfe-navi= gation\_\_dropdown\--Color,#151515); color:
var(\--pfe-navigation\_\_dropdown\--li= nk\--Color\--hover,#036);
outline: 0px; } #pfe-navigation.pfe-navigation\--processed
site-switcher, pfe-navigation.pfe= -navigation\--processed site-switcher
{ columns: auto; display: block; }
#pfe-navigation.pfe-navigation\--stuck,
pfe-navigation.pfe-navigation\--stuck= { left: 0px; position: fixed;
top: 0px; width: 100%; z-index: var(\--pfe-th=
eme\--zindex\--navigation,95); }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_outer-me= nu-wrapper\_\_inner,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-na=
vigation\_\_outer-menu-wrapper\_\_inner { opacity: 1 !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
pfe-navigation-account, #=
pfe-navigation.pfe-navigation\--in-crusty-browser rh-account-dropdown,
pfe-n= avigation.pfe-navigation\--in-crusty-browser
pfe-navigation-account, pfe-nav=
igation.pfe-navigation\--in-crusty-browser rh-account-dropdown {
display: no= ne !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser\[open-toggle=3D\"pfe-naviga=
tion\_\_account-toggle\"\] pfe-navigation-account,
#pfe-navigation.pfe-navigati=
on\--in-crusty-browser\[open-toggle=3D\"pfe-navigation\_\_account-toggle\"\]
rh-ac= count-dropdown,
pfe-navigation.pfe-navigation\--in-crusty-browser\[open-toggl=
e=3D\"pfe-navigation\_\_account-toggle\"\] pfe-navigation-account,
pfe-navigatio=
n.pfe-navigation\--in-crusty-browser\[open-toggle=3D\"pfe-navigation\_\_account-=
toggle\"\] rh-account-dropdown { display: block !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-ite= m,
pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-i= tem { display: block; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-lin= k\[aria-expanded=3D\"true\"\],
pfe-navigation.pfe-navigation\--in-crusty-browser=
.pfe-navigation\_\_menu-link\[aria-expanded=3D\"true\"\] {
\--pfe-icon\--color: va=
r(\--pfe-navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme\--color\--text,#15=
1515)); background:
var(\--pfe-navigation\_\_nav-bar\--toggle\--BackgroundColor-=
-active,var(\--pfe-theme\--color\--surface\--lightest,#fff)); color:
var(\--pfe-=
navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme\--color\--text,#151515));
= } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-lin= k\[aria-expanded=3D\"true\"\]:focus,
pfe-navigation.pfe-navigation\--in-crusty-b= rowser
.pfe-navigation\_\_menu-link\[aria-expanded=3D\"true\"\]:focus {
outline: = 0px; } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-lin= k\[aria-expanded=3D\"true\"\]:focus::after,
pfe-navigation.pfe-navigation\--in-c= rusty-browser
.pfe-navigation\_\_menu-link\[aria-expanded=3D\"true\"\]:focus::aft= er
{ border: 1px dashed; inset: 0px; content: \"\"; display: block;
position:= absolute; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= ,
pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdow= n { display: flex; flex-wrap: wrap; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= \> .style-scope,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navi=
gation\_\_dropdown \> .style-scope { flex-basis: 25%; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= .pfe-navigation\_\_footer.style-scope,
pfe-navigation.pfe-navigation\--in-cru= sty-browser
.pfe-navigation\_\_dropdown .pfe-navigation\_\_footer.style-scope {=
flex-basis: 100%; } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= .pfe-navigation\_\_footer.style-scope \>
.style-scope, pfe-navigation.pfe-nav= igation\--in-crusty-browser
.pfe-navigation\_\_dropdown .pfe-navigation\_\_foote= r.style-scope \>
.style-scope { margin-right: 16px; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= \--single-column,
#pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-nav=
igation\_\_dropdown\--single-column ul,
#pfe-navigation.pfe-navigation\--in-cru= sty-browser
.pfe-navigation\_\_dropdown\--single-column \> .style-scope, pfe-na=
vigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown\--singl= e-column,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigation\_=
\_dropdown\--single-column ul,
pfe-navigation.pfe-navigation\--in-crusty-brows= er
.pfe-navigation\_\_dropdown\--single-column \> .style-scope { display:
flex;= flex-flow: column; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= \--single-column \> .style-scope,
pfe-navigation.pfe-navigation\--in-crusty-br= owser
.pfe-navigation\_\_dropdown\--single-column \> .style-scope {
flex-basis:= auto; } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_search-t= oggle,
#pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigation\_\_s=
econdary-link, #pfe-navigation.pfe-navigation\--in-crusty-browser
\[slot=3D\"s= econdary-links\"\] \> a,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe=
-navigation\_\_search-toggle,
pfe-navigation.pfe-navigation\--in-crusty-browse= r
.pfe-navigation\_\_secondary-link,
pfe-navigation.pfe-navigation\--in-crusty= -browser
\[slot=3D\"secondary-links\"\] \> a { color: rgb(255, 255, 255) !import=
ant; justify-content: center !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_search-t= oggle\[aria-expanded=3D\"true\"\],
#pfe-navigation.pfe-navigation\--in-crusty-br= owser
.pfe-navigation\_\_secondary-link\[aria-expanded=3D\"true\"\],
#pfe-navigat= ion.pfe-navigation\--in-crusty-browser
\[slot=3D\"secondary-links\"\] \> a\[aria-e= xpanded=3D\"true\"\],
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-na=
vigation\_\_search-toggle\[aria-expanded=3D\"true\"\],
pfe-navigation.pfe-navigat= ion\--in-crusty-browser
.pfe-navigation\_\_secondary-link\[aria-expanded=3D\"tru= e\"\],
pfe-navigation.pfe-navigation\--in-crusty-browser
\[slot=3D\"secondary-li= nks\"\] \> a\[aria-expanded=3D\"true\"\] {
color: rgb(21, 21, 21) !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_account-= wrapper\--logged-in
.pfe-navigation\_\_log-in-link, #pfe-navigation.pfe-naviga=
tion\--in-crusty-browser .pfe-navigation\_\_search-toggle
.secondary-link\_\_ico= n-wrapper,
#pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigatio=
n\_\_search-toggle pfe-icon,
#pfe-navigation.pfe-navigation\--in-crusty-browse= r
.pfe-navigation\_\_secondary-link .secondary-link\_\_icon-wrapper,
#pfe-navig= ation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_secondary-link pfe= -icon,
#pfe-navigation.pfe-navigation\--in-crusty-browser \[slot=3D\"secondary=
-links\"\] \> a .secondary-link\_\_icon-wrapper,
#pfe-navigation.pfe-navigation-= -in-crusty-browser
\[slot=3D\"secondary-links\"\] \> a pfe-icon, pfe-navigation.=
pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_account-wrapper\--logged-= in
.pfe-navigation\_\_log-in-link,
pfe-navigation.pfe-navigation\--in-crusty-b= rowser
.pfe-navigation\_\_search-toggle .secondary-link\_\_icon-wrapper,
pfe-na= vigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_search-toggle p= fe-icon,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigation\_\_=
secondary-link .secondary-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation= \--in-crusty-browser
.pfe-navigation\_\_secondary-link pfe-icon, pfe-navigatio=
n.pfe-navigation\--in-crusty-browser \[slot=3D\"secondary-links\"\] \> a
.seconda= ry-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation\--in-crusty-browser \[sl=
ot=3D\"secondary-links\"\] \> a pfe-icon { display: none !important; }
\[id=3D\"pfe-navigation\_\_account-dropdown\"\]\[class\]\[class\] {
display: block; h= eight: auto; left: 0px; padding: 0px; position:
absolute; top: var(\--pfe-na= vigation\_\_nav-bar\--Height,72px); width:
100%; }
\[id=3D\"pfe-navigation\_\_account-dropdown\"\].pfe-navigation\_\_dropdown-wrapper-=
-invisible\[class\] { display: none; }
.pfe-navigation\_\_dropdown-wrapper { overflow: hidden; } \@media
(min-width: 768px) { .pfe-navigation\_\_custom-dropdown\--single-column
{ min-width: 25em; } } .pfe-navigation\--collapse-secondary-links
.pfe-navigation\_\_custom-dropdown-= -single-column { min-width: 0px; }
.secondary-link\_\_icon-wrapper { align-items: center; display: flex;
justify= -content: center; } .secondary-link\_\_alert-count {
background: var(\--pfe-navigation\_\_nav-bar\--a=
lert-color,var(\--pfe-theme\--color\--link,#06c)); border-radius: 20px;
color:=
var(\--pfe-navigation\_\_nav-bar\--Color\--on-highlight,var(\--pfe-theme\--color-=
-text\--on-saturated,#fff)); display: block; font-size:
var(\--pfe-navigation= \--FontSize\--xs,12px); line-height: 20px;
margin: 0px 4px 0px 2px; min-width= : 23px; overflow: hidden; padding:
0px 8px; } .secondary-link\_\_alert-count:empty { display: none; }
#pfe-navigation\_\_1x-skip-links { left: 0px; position: absolute; top:
0px; } #pfe-navigation\_\_1x-skip-links,
#pfe-navigation\_\_1x-skip-links li { height:= 0px; list-style: none;
margin: 0px; padding: 0px; width: 0px; } .skip-link\[class\]\[class\] {
font-size: var(\--pf-global\--FontSize\--sm,.875rem= ); line-height:
18px; } .skip-link\[class\]\[class\]:focus { border-radius: 0.21429em;
height: auto; le= ft: 50%; padding: 0.42857em 0.57143em; position:
fixed; top: 8px; transform= : translate(-50%); width: auto; z-index:
99999; clip: auto; background: var=
(\--pfe-navigation\_\_skip-link\--BackgroundColor,var(\--pfe-theme\--color\--surfa=
ce\--lightest,#fff)); color:
var(\--pfe-navigation\_\_skip-link\--Color,var(\--pf=
e-theme\--color\--link,#06c)); text-decoration: none; } pfe-navigation
pfe-navigation-account\[slot=3D\"account\"\] { background: var(-=
-pfe-navigation\_\_dropdown\--Background,var(\--pfe-theme\--color\--surface\--ligh=
test,#fff)); width: 100%; }
.pfe-navigation-default-container\[data-v-b258bd1d\] { position: sticky;
top:= 0px; z-index: 100; }
pfe-navigation\[data-v-b258bd1d\]::part(pfe-navigation\_\_search-wrapper\--md),
=
pfe-navigation\[data-v-b258bd1d\]::part(secondary-links\_\_button\--search)
{ di= splay: none; } .search-btn\[data-v-b258bd1d\] { align-items:
center; background-color: var(-= -rh-color-canvas-black,#151515);
border: 3px solid var(\--rh-color-canvas-bl= ack,#151515); cursor:
pointer; display: flex; flex-direction: column; heigh= t: 100%;
justify-content: center; outline: none; padding: 14px var(\--rh-spa=
ce-md,8px); } .search-btn\[data-v-b258bd1d\]:focus { border-top: 3px
solid var(\--rh-color-a= ccent-brand-on-light,#e00); outline: 2px dotted
var(\--rh-color-white,#fff);= } .search-btn
.search-icon\[data-v-b258bd1d\] { height: 26px; padding: 2px 0 va=
r(\--rh-space-xs,4px); width: 20px; } .search-btn
.search-icon\[data-v-b258bd1d\], .search-icon-helper-text\[data-v-=
b258bd1d\] { color: var(\--rh-color-white,#fff); }
.search-mobile\[data-v-b258bd1d\] { margin-bottom:
var(\--rh-space-2xl,32px); = } .search-mobile form\[data-v-b258bd1d\] {
display: flex; gap: var(\--rh-space-m= d,8px); margin: auto; }
.search-box\[data-v-b258bd1d\] { width: 35rem; } nav\[data-v-b258bd1d\]
{ background-color: rgb(21, 21, 21); justify-content: = space-between;
width: 100%; } a\[data-v-b258bd1d\], a\[data-v-b258bd1d\]:visited {
color: rgb(255, 255, 255);= display: inline-block; font-size:
var(\--rh-font-size-body-text-md,1rem); }
.skip-link\[class\]\[class\]\[data-v-b258bd1d\] { font-size:
var(\--pf-global\--Fon= tSize\--sm,.875rem); line-height: 18px; }
.skip-link\[class\]\[class\]\[data-v-b258bd1d\]:focus { border-radius:
0.21429em;= height: auto; left: 50%; padding: 0.42857em 0.57143em;
position: fixed; to= p: 8px; transform: translate(-50%); width: auto;
z-index: 99999; clip: auto= ; background: var(
\--pfe-navigation\_\_skip-link\--BackgroundColor,var(\--pfe-t=
heme\--color\--surface\--lightest,#fff) ); color: var(
\--pfe-navigation\_\_skip-=
link\--Color,var(\--pfe-theme\--color\--link,#06c) ); text-decoration:
none; } .visually-hidden\[data-v-b258bd1d\] { border: 1px solid rgb(0,
102, 204); hei= ght: 1px; overflow: hidden; padding: 0px; position:
absolute; width: 1px; c= lip: rect(0px, 0px, 0px, 0px); white-space:
nowrap; } h3\[data-v-b258bd1d\] { color:
light-dark(var(\--rh-color-text-primary-on-ligh=
t,#151515),var(\--rh-color-text-primary-on-dark,#fff)); font-family:
var( \--= rh-font-family-heading,\"Red Hat
Display\",Helvetica,Arial,sans-serif ); font= -size:
var(\--rh-font-size-body-text-lg,1.125rem); }
.language-picker\[data-v-b258bd1d\] { align-items: center;
background-color: =
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-dar=
ker,#1f1f1f)); display: flex; flex-direction: column; padding:
var(\--rh-spa= ce-xl,24px); width: 100%; } .language-picker
h3\[data-v-b258bd1d\] { margin: 0px; padding: 0px 1rem 1rem;= }
.language-picker ul\[data-v-b258bd1d\] { margin: 0px; padding: 0px; }
.language-picker a\[data-v-b258bd1d\] { color:
light-dark(var(\--rh-color-inte=
ractive-primary-default-on-light,#06c),var(\--rh-color-interactive-primary-d=
efault-on-dark,#92c5f9)); } .language-picker a\[data-v-b258bd1d\]:hover
{ color: light-dark(var(\--rh-colo=
r-interactive-primary-hover-on-light,#036),var(\--rh-color-interactive-prima=
ry-hover-on-dark,#b9dafc)); } .language-picker li\[data-v-b258bd1d\] {
list-style: none; } .language-dropdown\[data-v-b258bd1d\] { background:
rgb(255, 255, 255); box-s= hadow: rgba(0, 0, 0, 0.098) 0px 3px 6px;
position: absolute; right: 0px; wi= dth: 100%; z-index: 104; display:
block !important; } .pfe-navigation.pfe-navigation\--processed \>
\[slot=3D\"secondary-links\"\]\[data= -v-b258bd1d\] { height: auto;
overflow: visible; visibility: visible; width:= auto; }
\[slot=3D\"secondary-links\"\]\[data-v-b258bd1d\] { background-color:
light-dark(=
var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f=
)); } .upper-navigation\[data-v-b258bd1d\] { padding: 0
var(\--rh-space-2xl,32px); } .upper-nav-container\[data-v-b258bd1d\] {
border-bottom: 1px solid rgb(64, 64= , 64); margin: 0px; }
.upper-nav-hidden\[data-v-b258bd1d\]:not(:focus):not(:active) { clip:
rect(0p= x, 0px, 0px, 0px); clip-path: inset(50%); height: 1px;
overflow: hidden; po= sition: absolute; white-space: nowrap; width: 1px;
} .upper-nav-menu\[data-v-b258bd1d\] { align-items: center; display:
flex; just= ify-content: flex-end; line-height: 1.444; list-style: none;
margin-bottom:= 0px; margin-top: 0px; padding-left: 0px; }
.upper-nav-menu\[data-v-b258bd1d\], .upper-nav-menu \>
li\[data-v-b258bd1d\] { p= osition: relative; } .upper-nav-menu \>
li:not(:first-child) \> a\[data-v-b258bd1d\]::before, .upper= -nav-menu
\> li:not(:first-child) \> button\[data-v-b258bd1d\]::before { backgr=
ound-color: rgb(64, 64, 64); content: \"\"; height: 40%; left: 0px;
position:= absolute; top: 30%; width: 1px; } li\[data-v-b258bd1d\] {
display: list-item; margin: 0px; padding: 0px; text-a= lign:
-webkit-match-parent; } .upper-nav-menu
button.upper-nav-links\[data-v-b258bd1d\] { border-width: 3px= 0px 0px;
border-right-style: initial; border-bottom-style: initial; border=
-left-style: initial; border-right-color: initial; border-bottom-color:
ini= tial; border-left-color: initial; border-image: initial;
border-top-style: = solid; border-top-color: transparent; cursor:
pointer; line-height: 1.444; = } .upper-nav-menu
button.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258b= d1d\]
{ outline-color: rgb(21, 21, 21); } .upper-nav-menu
button.upper-nav-links\[aria-expanded=3D\"true\"\] .upper-nav-a=
rrow\[data-v-b258bd1d\] { filter: invert(0) sepia(2%) saturate(21%)
hue-rotat= e(257deg) brightness(108%) contrast(100%); transform:
rotate(270deg); } .upper-nav-menu
button.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258b=
d1d\]::before { display: none; } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\] { background-color: var( =
\--pfe-navigation\--BackgroundColor,var(\--pfe-theme\--color\--surface\--darkest,=
#151515) ); border-top: 3px solid transparent; color: rgb(255, 255,
255); d= isplay: block; font-family: var(
\--rh-font-family-body-text,\"Red Hat Text\",=
\"RedHatText\",Arial,sans-serif ); font-size:
var(\--rh-font-size-body-text-sm= ,.875rem); outline: none; padding:
12px 12px 14px; text-decoration: none; } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\]:hover { border-top-color:= rgb(184,
187, 190); } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\]:focus-within { outline: 1= px dashed
var(\--rh-color-white,#fff); outline-offset: -1px; } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\]:focus-within::before { di= splay:
none; } .upper-nav-dropdown-container\[data-v-b258bd1d\] { background:
light-dark(var=
(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));=
box-shadow: rgba(0, 0, 0, 0.098) 0px 3px 6px; display: none; padding:
5px = 30px 24px; position: absolute; right: 0px; top: 100%; width:
500px; z-index= : 105; } .upper-nav-dropdown-container \>
ul\[data-v-b258bd1d\] { column-count: 2; list= -style-type: none;
padding: 0px; width: auto; } .upper-nav-dropdown-container \> ul
li\[data-v-b258bd1d\] { color: rgb(21, 21,= 21); font-family: var(
\--rh-font-family-heading,\"Red Hat Display\",Helvetic=
a,Arial,sans-serif ); font-size:
var(\--rh-font-size-body-text-sm,.875rem); = list-style-type: none;
margin-bottom: 0px; } .upper-nav-dropdown-container \> ul li
span\[data-v-b258bd1d\] { color: light-=
dark(var(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-text-prim=
ary-on-dark,#fff)); font-weight:
var(\--rh-font-weight-body-text-medium,500)= ; }
.upper-nav-dropdown-container \> ul ul\[data-v-b258bd1d\] {
padding-left: 0px;= padding-top: 9px; } .upper-nav-dropdown-container \>
ul \> li\[data-v-b258bd1d\] { padding-top: 19p= x; break-inside: avoid;
} .upper-nav-dropdown-container \> ul \> li \> ul \>
li\[data-v-b258bd1d\] { line-h= eight: 1.45; padding: 4px 0px; }
.upper-nav-menu .upper-nav-arrow\[data-v-b258bd1d\] { display:
inline-block; = filter: invert(100%) sepia(8%) saturate(7%)
hue-rotate(1turn) brightness(10= 0%) contrast(93%); height: 18px;
margin-left: 5px; transform: rotate(90deg)= ; vertical-align: middle;
width: 8px; } #pfe-navigation\_\_secondary-links
.show\[data-v-b258bd1d\], .upper-navigation = .show\[data-v-b258bd1d\] {
display: block; } .upper-nav-menu
.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258bd1d\]:a=
ctive, .upper-nav-menu
.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258= bd1d\]:focus,
.upper-nav-menu .upper-nav-links\[aria-expanded=3D\"true\"\]\[data-=
v-b258bd1d\]:hover { background-color: rgb(255, 255, 255); color:
rgb(21, 21= , 21); } .upper-nav-menu
.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258bd1d\] {=
background-color: rgb(255, 255, 255); border-top-color: rgb(184, 187,
190)= ; color: rgb(0, 0, 0); position: relative; z-index: 1; }
.upper-nav-dropdown-container \> ul a\[data-v-b258bd1d\] { color:
light-dark(v=
ar(\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh-color-int=
eractive-primary-default-on-dark,#92c5f9)); font-family: var(
\--rh-font-fam= ily-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif ); font-size: 14= px;
text-decoration: none; } select\[data-v-b258bd1d\] { background-image:
url(\"data:image/svg+xml;charset= =3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'10\' height=3D= \'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%23151515\'
d=3D\'M.= 678 0h8.644c.596 0 .895.797.497 1.195l-4.372
4.58c-.298.3-.695.3-.993 0L.18= 1.196C-.216.797.081 0 .678
0\'/%3E%3C/svg%3E\"); } .pfe-navigation\_\_search\[data-v-b258bd1d\] {
background-color: var(\--rh-color= -white,#fff); }
.pfe-navigation\_\_search form\[data-v-b258bd1d\] { display: flex; gap:
var(\--r= h-space-md,8px); margin: auto; max-width: 992px; }
pfe-navigation \[slot=3D\"secondary-links\"\]
.buttons\[data-v-b258bd1d\] { displ= ay: flex; flex-wrap: wrap; gap:
var(\--rh-space-md,8px); margin-top: 4px; } pfe-navigation
\[slot=3D\"secondary-links\"\] .buttons\[data-v-b258bd1d\] :first-=
child { flex: 1 0 100%; } pfe-navigation \[slot=3D\"secondary-links\"\]
.buttons a\[data-v-b258bd1d\] { bor= der: 1px solid
light-dark(#d2d2d2,var(\--rh-color-border-subtle-on-dark,#707= 070));
border-radius: 3px; color: light-dark(var(\--rh-color-interactive-pri=
mary-default-on-light,#06c),var(\--rh-color-interactive-primary-default-on-d=
ark,#92c5f9)); cursor: pointer; flex-basis: calc(50% - 5px);
font-family: v= ar( \--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif= ); font-weight:
var(\--rh-font-weight-code-regular,400); padding: 1em; text= -align:
center; text-decoration: none; } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select\[data-v-b258bd= 1d\]
{ border-top-color: ; border-top-style: ; border-top-width: ; border-ri=
ght-color: ; border-right-style: ; border-right-width: ;
border-bottom-styl= e: ; border-bottom-width: ; border-left-color: ;
border-left-style: ; borde= r-left-width: ; border-image-source: ;
border-image-slice: ; border-image-w= idth: ; border-image-outset: ;
border-image-repeat: ; border-bottom-color: =
light-dark(#3c3f42,var(\--rh-color-gray-50,#707070)); cursor: pointer;
displ= ay: flex; margin: 3rem 0px; position: relative; } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select label\[data-v-=
b258bd1d\] { bottom: 100%; font-size: 14px; font-weight: 500;
margin-bottom:= 5px; position: absolute; } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select label\[data-v-=
b258bd1d\], pfe-navigation \[slot=3D\"secondary-links\"\]
.mobile-lang-select se= lect\[data-v-b258bd1d\] { color:
light-dark(var(\--rh-color-text-primary-on-li=
ght,#151515),var(\--rh-color-text-primary-on-dark,#fff)); font-family:
var( = \--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif ); = } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select select\[data-v=
-b258bd1d\] { appearance: none; background-color:
light-dark(#fff,var(\--rh-c= olor-gray-80,#292929)); border-style: none;
flex-basis: 100%; font-size: 16= px; line-height: 24px; padding: 6px
24px 6px 8px; } select\[data-v-b258bd1d\] { background-image:
var(\--header-select); backgroun= d-position: 98% 50%;
background-repeat: no-repeat; } #inputLabel\[data-v-b258bd1d\] {
align-items: center; display: flex; position= : relative; } #inputLabel
form\[data-v-b258bd1d\] { width: 100%; } .input-box\[data-v-b258bd1d\] {
font-family: var( \--rh-font-family-body-text,= \"Red Hat
Text\",\"RedHatText\",Arial,sans-serif ); font-size: var(\--rh-font-si=
ze-body-text-md,1rem); height: 36px; padding: 0px 8px; width: 100%; }
.input-box\[data-v-b258bd1d\]::placeholder { color: rgb(106, 110, 115);
font-= family: var( \--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,s= ans-serif ); font-size:
var(\--rh-font-size-body-text-md,1rem); font-weight:=
var(\--rh-font-weight-code-regular,400); line-height: 24px; }
.pfe-navigation\_\_custom-nav-container\[data-v-b258bd1d\] { padding: 0
0 var(-= -rh-space-lg,16px) 0; } .spacing-32\[data-v-b258bd1d\] { gap:
var(\--rh-space-2xl,32px); } h2.pfe-menu-item-heading\[data-v-b258bd1d\]
{ color: light-dark(var(\--rh-colo=
r-text-primary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff))=
; font-size: var(\--rh-font-size-body-text-lg,1.125rem); line-height:
27px; = margin: 0px; padding: 0px; }
ul.menu\_\_products-container\[data-v-b258bd1d\] { grid-auto-flow:
column; grid= -template-rows: repeat(3, auto); }
ul.menu\_\_products-container\[data-v-b258bd1d\],
ul.menu\_\_products-container-l= earn\[data-v-b258bd1d\] { display:
grid; gap: var(\--rh-space-2xl,32px); list-= style: none; margin:
var(\--rh-space-2xl,32px) 0 0; padding: 0px; }
ul.menu\_\_products-container-learn\[data-v-b258bd1d\] { grid-auto-flow:
row; g= rid-template-columns: repeat(3, auto); }
a.pfe-navigation\_\_custom-nav-link\[data-v-b258bd1d\] { border: 1px
solid tran= sparent; color:
light-dark(var(\--rh-color-interactive-primary-default-on-li=
ght,#06c),var(\--rh-color-interactive-primary-default-on-dark,#92c5f9));
dis= play: inline-block; }
a.pfe-navigation\_\_custom-nav-link\[data-v-b258bd1d\]:hover {
background: ligh=
t-dark(var(\--rh-color-surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,=
#383838)); outline: 8px solid
light-dark(var(\--rh-color-surface-lighter,#f2=
f2f2),var(\--rh-color-surface-dark,#383838)); }
a.pfe-navigation\_\_custom-nav-link\[data-v-b258bd1d\]:focus { border:
1px dash= ed
light-dark(var(\--rh-color-interactive-primary-default-on-light,#06c),var=
(\--rh-color-interactive-primary-default-on-dark,#92c5f9)); outline:
0px; } .pfe-navigation\_\_custom-nav-title\[data-v-b258bd1d\] { display:
inline-block;= } a.pfe-navigation\_\_custom-nav-link:hover
.pfe-navigation\_\_custom-nav-title\[d= ata-v-b258bd1d\] { color:
light-dark(var(\--rh-color-interactive-primary-hove=
r-on-light,#036),var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc))=
; text-decoration: underline; }
.pfe-navigation\_\_custom-nav-body\[data-v-b258bd1d\] { color:
light-dark(var(-=
-rh-color-text-primary-on-light,#151515),var(\--rh-color-text-primary-on-dar=
k,#fff)); display: inline-block; font-size:
var(\--rh-font-size-body-text-sm= ,.875rem); margin-top:
var(\--rh-space-md,8px); }
ul.menu\_\_use-cases-container\[data-v-b258bd1d\] { list-style: none;
margin: v= ar(\--rh-space-lg,16px) 0 0; padding: 0px; }
a.pfe-list-link\[data-v-b258bd1d\] { border: 1px solid transparent;
color: li=
ght-dark(var(\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh=
-color-interactive-primary-default-on-dark,#92c5f9)); display:
inline-block= ; margin-top: var(\--rh-space-lg,16px); }
a.pfe-list-link\[data-v-b258bd1d\]:hover { color:
light-dark(var(\--rh-color-i=
nteractive-primary-hover-on-light,#036),var(\--rh-color-interactive-primary-=
hover-on-dark,#b9dafc)); text-decoration: underline; }
a.pfe-list-link\[data-v-b258bd1d\]:focus { border: 1px dashed
light-dark(var(=
\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh-color-intera=
ctive-primary-default-on-dark,#92c5f9)); outline: 0px; }
.pfe-navigation\--footer\[data-v-b258bd1d\] { border-top: 1px solid
var(\--rh-c= olor-gray-60,#4d4d4d); margin-top:
var(\--rh-space-3xl,48px); padding-top: v= ar(\--rh-space-3xl,48px); }
pfe-navigation\[data-v-b258bd1d\]::part(mobile\_\_dropdown),
pfe-navigation\[dat=
a-v-b258bd1d\]::part(pfe-navigation\_\_dropdown-wrapper) {
background-color: l=
ight-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-dark=
er,#1f1f1f)); } rh-account-dropdown\[data-v-b258bd1d\] {
\--pfe-navigation\_\_dropdown\--link\--Co= lor:
light-dark(var(\--rh-color-interactive-primary-default-on-light,#06c),v=
ar(\--rh-color-interactive-primary-default-on-dark,#92c5f9));
\--pfe-navigati= on\_\_dropdown\--Color\--secondary:
light-dark(var(\--rh-color-text-primary-on-l=
ight,#151515),var(\--rh-color-text-primary-on-dark,#fff));
\--pfe-navigation\_= \_dropdown\--headings\--Color:
light-dark(var(\--rh-color-text-primary-on-light=
,#151515),var(\--rh-color-text-primary-on-dark,#fff));
\--pfe-navigation\_\_dro= pdown\--link\--Color\--hover:
light-dark(var(\--rh-color-interactive-primary-ho=
ver-on-light,#036),var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc=
)); \--pfe-navigation\_\_dropdown\--highlight-color:
light-dark(#c9190b,#fe5142= ); } \@media (min-width: 767px) {
.pfe-navigation\_\_search form\[data-v-b258bd1d\] { padding:
var(\--rh-space-2= xl,32px) 0; }
\[slot=3D\"secondary-links\"\]\[data-v-b258bd1d\] { background-color:
var(\--rh-= color-surface-darkest,#151515); } } \@media (max-width:
767px) { .right-navigation\[data-v-b258bd1d\],
.upper-navigation\[data-v-b258bd1d\] { = display: none; }
ul.menu\_\_products-container\[data-v-b258bd1d\],
ul.menu\_\_products-container= -learn\[data-v-b258bd1d\] { gap:
var(\--rh-space-2xl,32px); grid-auto-flow: ro= w; grid-template-columns:
1fr; } } \@media (max-width: 960px) { .search-box\[data-v-b258bd1d\] {
width: 28rem; } } \@media (min-width: 768px) and (max-width: 810px) {
.search-box\[data-v-b258bd1d\] { width: 24rem; } } \@media (max-width:
1199px) { .pfe-navigation\_\_custom-nav-container\[data-v-b258bd1d\] {
padding: 0px; } } \@media (min-width: 992px) {
.pfe-navigation-content-page-container\[data-v-b258bd1d\] { position:
stick= y; top: 0px; z-index: 100; } } \@media (min-width: 1200px) {
pfe-navigation\[data-v-b258bd1d\]::part(mobile\_\_dropdown) {
background-colo= r: var(\--rh-color-surface-darkest,#151515); } }
.status-legal .status-page-widget\[data-v-5f538988\] { display: block;
margin= : 0.5rem 0px; width: max-content; }
.status-page-widget\[data-v-5f538988\] { align-items: center; display:
flex; = flex-direction: row; } .status-legal .status-page-widget
.status-description\[data-v-5f538988\] { co= lor: rgb(204, 204, 204);
font-weight: 600; letter-spacing: 0.0125rem; line-= height: 1.5;
margin-right: 0.5rem; } .status-good\[data-v-5f538988\] {
background-color: rgb(62, 133, 54); }
.status-critical\[data-v-5f538988\] { background-color: rgb(163, 1, 0);
} .status-partial\[data-v-5f538988\] { background-color: rgb(245, 193,
45); } .status-maintentance\[data-v-5f538988\] { background-color:
rgb(49, 109, 193)= ; } .status-minor\[data-v-5f538988\] {
background-color: rgb(184, 92, 0); }
.status-description\[data-v-5f538988\] { color: rgb(204, 204, 204);
font-weig= ht: 500; letter-spacing: 0.2px; line-height: 1.5; }
.current-status-indicator\[data-v-5f538988\] { border-radius: 6px;
display: i= nline-block; height: 12px; margin: 0px 0px 0px 5px; width:
12px; } .current-status-indicator.small\[data-v-5f538988\] {
border-radius: 4px; disp= lay: inline-block; height: 8px; margin: 0px
0px 0px 5px; width: 8px; } :is(rh-footer, rh-footer-universal) a {
color: light-dark(var(\--rh-color-in=
teractive-primary-default-on-light,#06c),var(\--rh-color-interactive-primary=
-default-on-dark,#92c5f9)); text-decoration: none; } :is(rh-footer,
rh-footer-universal) a:hover { color: light-dark(var(\--rh-co=
lor-interactive-primary-hover-on-light,#036),var(\--rh-color-interactive-pri=
mary-hover-on-dark,#b9dafc)); text-decoration: underline; }
:is(rh-footer, rh-footer-universal) a:is(:focus, :focus-within) { color:
li=
ght-dark(var(\--rh-color-interactive-primary-hover-on-light,#036),var(\--rh-c=
olor-interactive-primary-hover-on-dark,#b9dafc)); text-decoration:
underlin= e; } :is(rh-footer, rh-footer-universal) a:visited { color:
light-dark(var(\--rh-=
color-interactive-primary-hover-on-light,#036),var(\--rh-color-interactive-p=
rimary-hover-on-dark,#b9dafc)); text-decoration: none; } :is(rh-footer,
rh-footer-universal) a\[slot\^=3D\"logo\"\] { display: block; }
:is(rh-footer) a\[slot\^=3D\"logo\"\] \> img { display: block; height:
var(\--rh-s= ize-icon-04,40px); width: auto; } :is(rh-footer,
rh-footer-universal) :is(h1, h2, h3, h4, h5, h6) { color: li=
ght-dark(var(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-text-=
primary-on-dark,#fff)); font-family:
var(\--rh-font-family-heading,RedHatDis= play,\"Red Hat
Display\",Helvetica,Arial,sans-serif); line-height: var(\--rh-l=
ine-height-heading,1.3); } rh-footer \[slot=3D\"links\"\]:is(h1, h2, h3,
h4, h5):nth-of-type(n+5) { \--\_lin= k-header-margin:
calc(var(\--rh-space-2xl, 32px) - var(\--rh-space-lg, 16px))= ; }
rh-footer \[slot\^=3D\"links\"\] a { gap:
var(\--rh-footer-links-gap,var(\--rh-spa= ce-md,8px)); } :is(rh-footer,
rh-footer-universal) \[slot\^=3D\"links\"\] li { display: content= s;
margin: 0px; padding: 0px; } :is(rh-footer, rh-footer-universal)
\[slot\^=3D\"links\"\] a { display: block; f= ont-size:
var(\--rh-footer-link-font-size,var(\--rh-font-size-body-text-sm,.8=
75rem)); width: fit-content; color:
light-dark(var(\--rh-color-text-primary-=
on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff))
!important; } rh-footer-universal \[slot\^=3D\"links\"\] a { font-size:
inherit; } :is(rh-footer, rh-footer-universal) {
\--rh-footer-section-side-gap: var(\--r= h-space-lg,16px); overflow-y:
auto; } :is(rh-footer, rh-footer-universal) \> :not(\[slot=3D\"logo\"\],
rh-footer-unive= rsal) { animation-delay: 0s; animation-duration: 5s;
animation-name: var(\--= \_fallback-animation,deopacitize-footer);
animation-timing-function: ease; o= pacity: var(\--\_fallback-opacity);
} \@media screen and (min-width: 768px) { :is(rh-footer,
rh-footer-universal) { \--rh-footer-section-side-gap: var(-=
-rh-space-2xl,32px); } } \@media screen and (min-width: 1440px) {
:is(rh-footer, rh-footer-universal) { \--rh-footer-section-side-gap:
var(-= -rh-space-4xl,64px); } } rh-footer:not(:defined) {
background-color: var(\--rh-color-surface-darker,#= 1f1f1f); display:
grid; grid-template-areas: \"footer\" \"global\"; grid-templa= te-rows:
1fr auto; min-height: var(\--rh-footer-nojs-min-height,750px); widt= h:
100%; } \@keyframes deopacitize-footer {=20 0% { \--\_fallback-opacity:
0; } 99% { \--\_fallback-opacity: 0; } 100% { \--\_fallback-opacity: 1;
} } rh-footer-universal:not(:defined) { background-color:
var(\--rh-color-surfac= e-darkest,#151515); display: block; min-height:
176px; width: 100%; } rh-footer-universal:not(:defined)::before {
grid-area: global; } rh-footer-universal rh-footer-copyright {
grid-column: -1 / 1; } :is(rh-footer-block) a\[data-v-81a16915\] {
text-decoration: underline; } .reddit-span a img\[data-v-81a16915\] {
transition: filter 0.3s; padding-bott= om: 3px !important; }
.reddit-span a:hover img\[data-v-81a16915\] { filter: brightness(0)
saturate(= 100%) invert(87%) sepia(0) saturate(0) hue-rotate(154deg)
brightness(94%) c= ontrast(84%); } \@keyframes fade-in {=20 0% {
opacity: 0; visibility: hidden; } 1% { visibility: visible; } 100% {
opacity: 1; visibility: visible; } } \@media (min-height: 48em) {
.rhdocs { \--rh-table\--maxHeight: calc(100vh - 12.5rem); } } \*,
.rhdocs \*, .rhdocs ::after, .rhdocs ::before, ::after, ::before {
box-si= zing: border-box; } .rhdocs img, .rhdocs object, .rhdocs svg,
img, object, svg { display: inlin= e-block; max-width: 100%;
vertical-align: middle; } .rhdocs hr { border-right: 0px; border-bottom:
0px; border-left: 0px; borde= r-image: initial; border-top: .0625rem
solid light-dark(#d2d2d2,var(\--rh-co=
lor-border-subtle-on-dark,#707070)); clear: both; margin: 1rem 0px; }
.rhdocs a { color:
light-dark(var(\--rh-color-interactive-primary-default-on=
-light,#06c),var(\--rh-color-interactive-primary-default-on-dark,#92c5f9));
= text-decoration: underline; } .rhdocs a:focus, .rhdocs a:hover {
color: light-dark(var(\--rh-color-interac=
tive-primary-hover-on-light,#036),var(\--rh-color-interactive-primary-hover-=
on-dark,#b9dafc)); } .rhdocs a.anchor-heading { color:
light-dark(var(\--rh-color-gray-95,#151515=
),var(\--rh-color-white,#fff)); cursor: pointer; text-decoration: none;
word= -break: break-word; } .rhdocs p { margin: 1.49963rem 0px; }
.rhdocs li \> p { margin: 0px; } .rhdocs h1 { font-weight:
var(\--rh-font-weight-heading-regular,400); } .rhdocs h1, .rhdocs h2,
.rhdocs h3, .rhdocs h4, .rhdocs h5, .rhdocs h6 { fo= nt-family:
RedHatDisplay, \"Red Hat Display\", \"Helvetica Neue\", Arial, sans-=
serif; margin: 0px 0px 0.625rem; } .rhdocs h2, .rhdocs h3, .rhdocs h4,
.rhdocs h5, .rhdocs h6 { font-weight: v=
ar(\--rh-font-weight-heading-medium,500); } .rhdocs h1 { font-size:
var(\--rh-font-size-heading-xl,2.5rem); margin: 2rem= 0px; } .rhdocs h2
{ font-size: var(\--rh-font-size-heading-md,1.75rem); margin: 2re= m
0px; } .rhdocs h3 { font-size: var(\--rh-font-size-heading-sm,1.5rem); }
.rhdocs h4 { font-size: var(\--rh-font-size-heading-xs,1.25rem); }
.rhdocs h5 { font-size: 18px; } .rhdocs ol ::marker, .rhdocs ul ::marker
{ font: inherit; } .rhdocs li { margin: 0px 0px 0.5em; padding: 0px; }
.rhdocs li \> p { margin: 0.5rem 0px; } .rhdocs li \> ol, .rhdocs li \>
ul { margin: 0px; } .rhdocs dl dd { margin: 0.5rem 0px 0.5rem 1rem; }
.rhdocs dl dd \> p { margin: 0.5rem 0px; } .rhdocs .informaltable,
.rhdocs .table-contents, .rhdocs .table-wrapper { m= ax-height:
var(\--rh-table\--maxHeight); overflow: auto; } .rhdocs table { border:
0px; font-size: 1rem; line-height: 1.6667; table-la= yout: fixed;
\--rh-table\--hoveredCol\--Background: light-dark(rgba(from var(-=
-rh-color-blue-50,#0066cc) r g b/.1),rgba(from
var(\--rh-color-blue-70,#0033= 66) r g b/.3));
\--rh-table\--hoveredRow\--Background: light-dark(rgba(from va=
r(\--rh-color-gray-40,#a3a3a3) r g b/.1),rgba(from
var(\--rh-color-white,#fff= fff) r g b/.1));
\--rh-table\--hoveredIntersection\--Background: light-dark(#e=
0edf4,#2f3d54); background-color:
light-dark(var(\--rh-color-surface-lightes=
t,#fff),var(\--rh-color-surface-darker,#1f1f1f)); } .rhdocs table
caption { color: rgb(88, 88, 88); margin-bottom: 0.5rem; marg= in-top:
0.5rem; text-align: left; } .rhdocs table td, .rhdocs table th {
border-top: 0px; border-right: 0px; bo= rder-left: 0px; border-image:
initial; border-bottom: .0625rem solid var(\--=
pfe-table\--Border,#d2d2d2); padding: 0.5em 1rem; } .rhdocs table
td.halign-left, .rhdocs table th.halign-left { text-align: le= ft; }
.rhdocs table td.halign-center, .rhdocs table th.halign-center, table
td.ha= lign-center, table th.halign-center { text-align: center; }
.rhdocs table td.halign-right, .rhdocs table th.halign-right {
text-align: = right; } .rhdocs table td.valign-top, .rhdocs table
th.valign-top { vertical-align: = top; } .rhdocs table td.valign-middle,
.rhdocs table th.valign-middle { vertical-a= lign: middle; } .rhdocs
table td.valign-bottom, .rhdocs table th.valign-bottom { vertical-a=
lign: bottom; } .rhdocs table thead td, .rhdocs table thead th {
background: rgb(245, 245, = 245); font-weight: 600; } .rhdocs rh-table
table, .rhdocs rh-table.rh-table\--expanded-vertically { ma= x-height:
max-content; } .rhdocs pre.nowrap { overflow: auto; overflow-wrap:
normal; white-space: pr= e; word-break: normal; } .rhdocs
.codeblock\_\_wrapper pre { background: transparent; }
.rh-table\--full-screen code, .rhdocs .content\--md code, .rhdocs
.content\--s= m code, .rhdocs .rh-table\--full-screen code {
overflow-wrap: normal; word-b= reak: normal; } .rhdocs\[class\] pre
code, \[class\] pre code { background: inherit; color: inh= erit;
font-family: inherit; font-size: inherit; font-weight: inherit; line-=
height: inherit; padding: 0px; } .rhdocs .keycap, .rhdocs kbd {
background-color: rgb(238, 238, 238); backgr= ound-image:
linear-gradient(rgb(221, 221, 221), rgb(238, 238, 238), rgb(255= , 255,
255)); border-radius: 0.1875rem; box-shadow: rgb(255, 255, 255) 0px =
-0.0625rem, rgb(170, 170, 170) 0px 0.0625rem 0px 0.1875rem; color:
rgb(21, = 21, 21); font-family: RedHatMono, \"Red Hat Mono\", Consolas,
monospace; font= -size: 90%; font-weight: 400; margin: 0px 0.25rem;
padding: 0.125rem 0.375r= em; } .keycap strong, .rhdocs .keycap strong {
font-weight: inherit; } .rhdocs kbd.keyseq, kbd.keyseq { background:
transparent; border: 0px; box-= shadow: none; padding: 0px; } .rhdocs
kbd.keyseq kbd, kbd.keyseq kbd { display: inline-block; margin: 0px=
0.375rem; } .rhdocs kbd.keyseq kbd:first-child, kbd.keyseq
kbd:first-child { margin-lef= t: 0px; } .rhdocs b.button { font-size:
90%; font-weight: 700; padding: 0.1875rem; } .rhdocs b.button::before {
content: \"\[\"; } .rhdocs b.button::after { content: \"\]\"; } html {
font-family: sans-serif; text-size-adjust: 100%; } body { margin: 0px; }
.rhdocs audio, .rhdocs canvas, .rhdocs progress, .rhdocs video {
display: i= nline-block; vertical-align: baseline; } .rhdocs
audio:not(\[controls\]) { display: none; height: 0px; } \[hidden\],
template { display: none; } .rhdocs a { background: transparent; }
.rhdocs a:active, .rhdocs a:hover { outline: 0px; } .rhdocs
a.anchor-heading:focus-visible { color: light-dark(var(\--rh-color-g=
ray-95,#151515),var(\--rh-color-white,#fff)); } .rhdocs abbr\[title\] {
border-bottom: 0.0625rem dotted; } .rhdocs dfn { font-style: italic; }
.rhdocs h1 { margin: 0.67em 0px; } .rhdocs mark { background: rgb(255,
255, 0); color: rgb(0, 0, 0); } .rhdocs small { font-size: 80%; }
.rhdocs sub, .rhdocs sup { font-size: 75%; line-height: 0; position:
relati= ve; vertical-align: baseline; } .rhdocs sup { top: -0.5em; }
.rhdocs sub { bottom: -0.25em; } .rhdocs img { background-color:
light-dark(transparent,var(\--rh-color-surfa= ce-lightest,#fff));
border: 0px; padding: 20px; } .rhdocs .inlinemediaobject img { padding:
2px; } .rhdocs svg:not(:root) { overflow: hidden; } .rhdocs figure {
margin: 1em 2.5rem; } .rhdocs hr { box-sizing: content-box; height: 0px;
} .rhdocs code, .rhdocs kbd, .rhdocs pre, .rhdocs samp { font-family:
monospa= ce, monospace; font-size: 1em; } .rhdocs button, .rhdocs
optgroup, .rhdocs select, .rhdocs textarea, .rhdocs= input { color:
inherit; font: inherit; margin: 0px; } .rhdocs rh-button.copy-link-btn {
border: 2px solid light-dark(var(\--rh-col=
or-white,#fff),var(\--rh-color-surface-darker,#1f1f1f)); cursor:
pointer; di= splay: flex; } .rhdocs rh-button.copy-link-btn:hover {
background-color: light-dark(var(\--=
rh-color-surface-lighter,#f2f2f2),var(\--rh-color-gray-60,#4d4d4d));
border-= radius: var(\--rh-border-radius-default,3px); } .rhdocs
rh-button.copy-link-btn .link-icon { color: light-dark(var(\--rh-col=
or-canvas-black,#151515),var(\--Core-color-palette-Gray-white,#fff)); }
.rhdocs button { overflow: visible; } .rhdocs button, .rhdocs select {
text-transform: none; } .rhdocs button, .rhdocs html
input\[type=3D\"button\"\], .rhdocs input\[type=3D\"= reset\"\], .rhdocs
input\[type=3D\"submit\"\] { appearance: button; cursor: point= er; }
.rhdocs button\[disabled\], .rhdocs html input\[disabled\] { cursor:
default; } .rhdocs input { line-height: normal; } .rhdocs
input\[type=3D\"checkbox\"\], .rhdocs input\[type=3D\"radio\"\] {
box-sizin= g: border-box; padding: 0px; } .rhdocs
input\[type=3D\"number\"\]::-webkit-inner-spin-button, .rhdocs
input\[ty= pe=3D\"number\"\]::-webkit-outer-spin-button { height: auto;
} .rhdocs input\[type=3D\"search\"\] { appearance: textfield;
box-sizing: content= -box; } .rhdocs
input\[type=3D\"search\"\]::-webkit-search-cancel-button, .rhdocs input=
\[type=3D\"search\"\]::-webkit-search-decoration { appearance: none; }
.rhdocs fieldset { border: 0.0625rem solid silver; margin: 0px 0.125rem;
pa= dding: 0.35em 0.625em 0.75em; } .rhdocs legend { border: 0px;
padding: 0px; } .rhdocs textarea { overflow: auto; } .rhdocs optgroup {
font-weight: 700; } .rhdocs table { border-collapse: collapse;
border-spacing: 0px; } .rhdocs td, .rhdocs th { padding: 0px; } .rhdocs
.\_additional-resources\[class\]\[class\], .rhdocs
.\_additional-resource= s\[class\]\[class\]\[id\]:last-child {
background: light-dark(var(\--rh-color-surf=
ace-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f)); border:
0.0625r= em solid rgb(210, 210, 210); border-radius: 0.1875rem; margin:
2em 0px 4em;= padding: 2rem 2rem 1rem; } .rhdocs
.\_additional-resources\[class\]\[class\]\[id\]:last-child { margin-top:
-= 2rem; } .rhdocs .\_additional-resources\[class\]\[class\]:only-child
{ grid-column: 1 / = -1; } .\_additional-resources\[class\]\[class\]
.additional-resources\_\_heading, .\_addi=
tional-resources\[class\]\[class\] .heading,
.\_additional-resources\[class\]\[clas= s\] h1,
.\_additional-resources\[class\]\[class\] h2,
.\_additional-resources\[clas= s\]\[class\] h3,
.\_additional-resources\[class\]\[class\] h4, .\_additional-resourc=
es\[class\]\[class\] h5, .\_additional-resources\[class\]\[class\] h6,
.\_additional-= resources\[class\]\[class\] p.title { display: block;
font-family: RedHatDispla= y, \"Red Hat Display\", \"Helvetica Neue\",
Arial, sans-serif; font-size: 1.125= rem; font-weight: 700; line-height:
1.5rem; margin: 0px 0px 0.5rem; padding= : 0px; text-transform:
uppercase; } .\_additional-resources\[class\]\[class\] ul { border: 0px;
list-style: none; ma= rgin: 0px; padding: 0px; position: relative; }
.related-topic-content\_\_wrapper
.\_additional-resources\[class\]\[class\] ul { d= isplay: block; }
.\_additional-resources\[class\]\[class\] ul::after { background-color:
light-da=
rk(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1=
f1f)); bottom: 0px; content: \"\"; display: block; height: 0.125rem;
position= : absolute; width: 100%; }
.\_additional-resources\[class\]\[class\] li { border-bottom: 0.0625rem
solid rg= b(210, 210, 210); box-sizing: content-box; margin: 0px;
padding: 1rem 1.5re= m 1rem 0px; break-inside: avoid; }
.\_additional-resources\[class\]\[class\] li:only-child { grid-column: 1
/ -1; } .\_additional-resources\[class\]\[class\] li:last-child {
border: 0px; } \@media (min-width: 1100px) {
.\_additional-resources\[class\]\[class\] li:last-child { border-bottom:
0.062= 5rem solid rgb(210, 210, 210); } }
.\_additional-resources\[class\]\[class\] li p:only-child { margin: 0px;
padding= : 0px; } .\_additional-resources\[class\]\[class\] li a {
text-decoration: none; } .\_additional-resources\[class\]\[class\] li
a:focus, .\_additional-resources\[cla= ss\]\[class\] li a:hover {
text-decoration: underline; } .rhdocs table .admonitionblock \>
div:nth-child(2), .rhdocs table .caution \>= div:nth-child(2), .rhdocs
table .important \> div:nth-child(2), .rhdocs tab= le .note \>
div:nth-child(2), .rhdocs table .tip \> div:nth-child(2), .rhdocs= table
.warning \> div:nth-child(2) { margin: 0.5rem 0px; } .rhdocs table
.admonitionblock \> div:nth-child(2) \> :first-child, .rhdocs t= able
.caution \> div:nth-child(2) \> :first-child, .rhdocs table .important
\>= div:nth-child(2) \> :first-child, .rhdocs table .note \>
div:nth-child(2) \> = :first-child, .rhdocs table .tip \>
div:nth-child(2) \> :first-child, .rhdocs= table .warning \>
div:nth-child(2) \> :first-child { margin-top: 0px; } .rhdocs table
.admonitionblock \> div:nth-child(2) \> :last-child, .rhdocs ta= ble
.caution \> div:nth-child(2) \> :last-child, .rhdocs table .important \>
d= iv:nth-child(2) \> :last-child, .rhdocs table .note \>
div:nth-child(2) \> :la= st-child, .rhdocs table .tip \>
div:nth-child(2) \> :last-child, .rhdocs tabl= e .warning \>
div:nth-child(2) \> :last-child { margin-bottom: 0px; } .rhdocs
.codeblock\_\_wrapper + .codeblock\_\_wrapper, .rhdocs pre + pre, .rhdo=
cs pre\[class\] + pre\[class\] { margin-top: 2rem; } .rhdocs
.codeblock\_\_wrapper { background: light-dark(var(\--rh-color-surface=
-lighter,#f2f2f2),var(\--rh-color-gray-80,#292929)); overflow: visible;
posi= tion: relative; transform: translate(0px); z-index: 0; }
.codeblock\_\_wrapper::before { background-repeat: no-repeat;
background-size= : 6.25rem 100%; bottom:
var(\--scrollbar\_\_height,1px); content: \"\"; display:= block; height:
7.125rem; max-height: calc(100% - var(\--scrollbar\_\_height, = 2px));
position: absolute; right: var(\--scrollbar\_\_width,6px); top: 0.0625r=
em; width: 4.0625rem; z-index: 1; } .rhdocs .codeblock\_\_inner-wrapper,
.rhdocs pre { max-height: calc(-6.25rem = + 100vh); } \@media
(min-height: 48em) { .rhdocs .codeblock\_\_inner-wrapper, .rhdocs pre {
max-height: calc(-12.5re= m + 100vh); } } .rhdocs
.codeblock\_\_inner-wrapper { display: grid; grid-template-columns: 1=
fr 4.375rem; } .rhdocs .codeblock\_\_wrapper\--expanded
.codeblock\_\_inner-wrapper { max-heigh= t: max-content; }
.codeblock\_\_copy span { display: block; height: 0px; position:
absolute; vi= sibility: hidden; width: 0px; } .codeblock\_\_copy:focus {
outline: currentcolor dashed 0.0625rem; } .codeblock\_\_copy
svg#icon\--copy { height: 1rem; width: 1rem; } .codeblock\_\_expand {
appearance: none; background: rgb(240, 239, 239); bord= er: 0px; cursor:
pointer; height: 1.75rem; left: calc(100% - 2.75rem - var(=
\--scrollbar\_\_width, 0px)); position: absolute; text-indent: -9999em;
top: 3= .25rem; width: 1.75rem; z-index: 2; }
.codeblock\_\_expand::before { background: rgb(106, 110, 115); content:
\"\"; h= eight: 100%; left: 0px; mask-image:
url(\"data:image/svg+xml;charset=3Dutf-8= ,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' viewBox=3D\'0 0 320 512\'%3E%3C!=
\--! Font Awesome Pro 6.2.0 by \@fontawesome - https://fontawesome.com
Licens= e - https://fontawesome.com/license (Commercial License)
Copyright 2022 Fon= ticons, Inc.\--%3E%3Cpath d=3D\'M182.6
9.4c-12.5-12.5-32.8-12.5-45.3 0l-96 96= c-12.5 12.5-12.5 32.8 0
45.3s32.8 12.5 45.3 0l41.4-41.4v293.4l-41.4-41.3c-1=
2.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l96 96c12.5 12.5 32.8 12.5
45.3 = 0l96-96c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192
402.7V109.3l41.4 4= 1.4c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8
0-45.3l-96-96z\'/%3E%3C/svg%3E\"); m= ask-position: center center;
mask-repeat: no-repeat; mask-size: auto 1rem; = position: absolute; top:
0px; width: 100%; } .codeblock\_\_wrapper\--expanded
.codeblock\_\_expand { background: rgb(43, 154,= 243); }
.codeblock\_\_wrapper\--expanded .codeblock\_\_expand::before {
background: rgb(= 255, 255, 255); } .codeblock\_\_expand:focus::before,
.codeblock\_\_expand:hover::before { backgr= ound: rgb(0, 102, 204); }
.codeblock\_\_wrapper\--expanded .codeblock\_\_expand:focus::before,
.codeblock\_= \_wrapper\--expanded .codeblock\_\_expand:hover::before {
background: rgb(255, = 255, 255); } .codeblock\_\_expand:focus {
outline: currentcolor dashed 0.0625rem; } .rhdocs .callout, .rhdocs
.colist \> ol \> li::before, .rhdocs .conum { backg= round:
light-dark(var(\--rh-color-status-info-on-light,#5e40be) var(\--rh-col=
or-status-info-on-dark,#b6a6e9)); height: 24px; width: 24px; } .rhdocs
.calloutlist \> ol, .rhdocs .colist \> ol { counter-reset: colist 0; =
list-style: none; margin: 1rem 0px 2rem; padding: 0px; } .rhdocs
.calloutlist \> ol \> li, .rhdocs .colist \> ol \> li { counter-increme=
nt: colist 1; font-size: 1rem; margin: 0.5rem 0px; padding-left:
1.75rem; p= osition: relative; } .rhdocs .calloutlist \> ol \> li
.colist-num, .rhdocs .colist \> ol \> li .coli= st-num { display: none;
} .calloutlist \> ol \> li::before, .colist \> ol \> li::before {
content: counte= r(colist); left: 0px; position: absolute; top:
0.1875rem; } .calloutlist dt { clear: left; float: left; margin: 0px;
padding: 0px 0.5re= m 0px 0px; } .included-in-guides\[class\],
.included-in-guides\[class\]\[id\]:last-child { bac= kground: rgb(255,
255, 255); border: 0.0625rem solid rgb(210, 210, 210); bo= rder-radius:
0.1875rem; margin: 2em 0px 4em; padding: 2rem 2rem 1rem; }
.included-in-guides\[class\]\[id\]:last-child { margin-top: -2rem; }
.included-in-guides\[class\]:only-child { grid-column: 1 / -1; }
.included-in-guides\[class\] .additional-resources\_\_heading,
.included-in-gui= des\[class\] .heading, .included-in-guides\[class\]
h1, .included-in-guides\[cla= ss\] h2, .included-in-guides\[class\] h3,
.included-in-guides\[class\] h4, .incl= uded-in-guides\[class\] h5,
.included-in-guides\[class\] h6, .included-in-guide= s\[class\] p.title
{ display: block; font-family: RedHatDisplay, \"Red Hat Dis= play\",
\"Helvetica Neue\", Arial, sans-serif; font-size: 1.125rem; font-weigh=
t: 700; line-height: 1.5rem; margin: 0px 0px 0.5rem; padding: 0px;
text-tra= nsform: uppercase; } .included-in-guides\[class\] ul { border:
0px; list-style: none; margin: 0px;= padding: 0px; position: relative; }
.related-topic-content\_\_wrapper .included-in-guides\[class\] ul {
display: bl= ock; } .included-in-guides\[class\] ul::after {
background-color: rgb(255, 255, 255)= ; bottom: 0px; content: \"\";
display: block; height: 0.125rem; position: abs= olute; width: 100%; }
.included-in-guides\[class\] li { border-bottom: 0.0625rem solid
rgb(210, 210= , 210); box-sizing: content-box; margin: 0px; padding:
1rem 1.5rem 1rem 0px= ; break-inside: avoid; }
.included-in-guides\[class\] li:only-child { grid-column: 1 / -1; }
.included-in-guides\[class\] li:last-child { border: 0px; } \@media
(min-width: 1100px) { .included-in-guides\[class\] li:last-child {
border-bottom: 0.0625rem solid= rgb(210, 210, 210); } }
.included-in-guides\[class\] li p:only-child { margin: 0px; padding:
0px; } .included-in-guides\[class\] li a { text-decoration: none; }
.included-in-guides\[class\] li a:focus, .included-in-guides\[class\] li
a:hove= r { text-decoration: underline; } .menuseq { display:
inline-flex; overflow: hidden; text-indent: -9999em; } .menuseq .menu,
.menuseq .menuitem, .menuseq .submenu { display: block; pos= ition:
relative; text-indent: 0px; } .menuseq .menu + .menu::before, .menuseq
.menu + .menuitem::before, .menuse= q .menu + .submenu::before, .menuseq
.menuitem + .menu::before, .menuseq .m= enuitem + .menuitem::before,
.menuseq .menuitem + .submenu::before, .menuse= q .submenu +
.menu::before, .menuseq .submenu + .menuitem::before, .menuseq=
.submenu + .submenu::before { content: \"\>\"; display: inline-block;
font-we= ight: 700; padding: 0px 0.25em; }
.related-topic-content\_\_wrapper { margin: 2em 0px; }
.related-topic-content\_\_wrapper\--for-guide { margin-bottom: -2.5rem;
paddin= g-bottom: 0.0625rem; position: relative; z-index: 1; }
.related-topic-content\_\_wrapper\--for-guide::before { background:
rgb(240, 2= 40, 240); content: \"\"; display: block; height: 100%; left:
-3rem; position:= absolute; right: -4.5rem; top: 0px; width: auto;
z-index: -1; } \@media (min-width: 1100px) {
.related-topic-content\_\_wrapper\--for-guide::before { left: -2.5rem;
right= : -3.625rem; } } .related-topic-content\_\_wrapper\--for-guide
summary { padding: 1em 2em 1em 2= .1875rem; } \@media (min-width: 950px)
{ .related-topic-content\_\_inner-wrapper { display: grid; gap: 2em;
grid-tem= plate-columns: repeat(2, minmax(0px, 1fr)); } } .local-render
.rhdocs-content { margin: 0px auto; } .rhdocs cp-documentation {
display: block; padding-bottom: 2.5rem; } .rhdocs
cp-documentation.PFElement, .rhdocs cp-documentation\[pfelement\] { p=
adding: 0px; } rh-table { display: block; } ::-webkit-scrollbar, :host
.rhdocs ::-webkit-scrollbar { height: 0.625rem; = width: 0.625rem; }
::-webkit-scrollbar, ::-webkit-scrollbar-track, :host .rhdocs
::-webkit-scr= ollbar, :host .rhdocs ::-webkit-scrollbar-track {
background-color: rgb(214= , 214, 214); } ::-webkit-scrollbar-thumb,
:host .rhdocs ::-webkit-scrollbar-thumb { backgr= ound-color: rgb(142,
142, 142); } \*, :host .rhdocs \* { scrollbar-color: rgb(142, 142, 142)
rgb(214, 214, 214)= ; } .rhdocs p:empty, p:empty { display: none; }
.rhdocs\[class\] h1 code, .rhdocs\[class\] h2 code, .rhdocs\[class\] h3
code, .rh= docs\[class\] h4 code, .rhdocs\[class\] h5 code,
.rhdocs\[class\] h6 code, \[class= \] h1 code, \[class\] h2 code,
\[class\] h3 code, \[class\] h4 code, \[class\] h5 co= de, \[class\] h6
code { background: transparent; border: 0px; color: inherit;= font:
inherit; margin: 0px; padding: 0px; } .pane-page-title h1,
.rhdocs\_\_header\_\_primary-wrapper h1 { font-family: Red= HatDisplay,
\"Red Hat Display\", \"Helvetica Neue\", Arial, sans-serif; font-si= ze:
2.25rem; line-height: 1.333; } .rhdocs details\[class\] { list-style:
none; margin: 1rem 0px 3rem; padding: = 0px; } .rhdocs-toc\[class\] {
background: rgb(242, 242, 242); margin: 1rem 0px 2rem;= padding: 1rem; }
.rhdocs-toc\[class\] \> :last-child { margin-bottom: 0px; }
.rhdocs-toc\[class\] .rhdocs-toctitle { font-size: 1.25rem; font-weight:
400;= line-height: 1.6667; margin-top: 0px; text-transform: none; }
.rhdocs-toc\[class\] li { margin-bottom: 0.25em; padding-left: 0.5em; }
.preamble { margin: 0px 0px 2rem; } .sect1 { margin: 2rem 0px 1rem; }
:host .sect1, cp-documentation .sect1 { margin: 0px 0px 2rem; padding:
0.06= 25rem 0px 0px; } :host(.cp-documentation\--has-external-header)
.sect1:first-child \> h2:first= -child,
:host(.cp-documentation\--has-external-header) .sect1:first-child \> =
h3:first-child { margin-top: 0px; } .listingblock, .literalblock {
margin: 1rem 0px; } .quoteblock, .verseblock { border-left: 0.25rem
solid rgb(210, 210, 210); m= argin: 1rem 0px; padding: 1rem 1rem 1rem
2rem; } .quoteblock.pullleft, .verseblock.pullleft { float: left;
margin-right: 3re= m; width: 25rem; } \@media (min-width: 768px) {
.quoteblock.pullleft, .verseblock.pullleft { margin-left: -1rem; } }
.quoteblock.pullright, .verseblock.pullright { float: right;
margin-left: 3= rem; width: 25rem; } \@media (min-width:768) {
.quoteblock.pullright, .verseblock.pullright { margin-right: -2rem; } }
\@media (min-width: 1100px) { .quoteblock.pullright,
.verseblock.pullright { margin-right: -10rem; } } .quoteblock \>
:first-child, .verseblock \> :first-child { margin-top: 0px; }
.quoteblock .content, .verseblock .content { font-family: RedHatText,
\"Red = Hat Text\", \"Helvetica Neue\", Arial, sans-serif; font-size:
1.25rem; line-he= ight: 1.6667; } .quoteblock .attribution, .verseblock
.attribution { font-size: 0.875rem; f= ont-style: italic; font-weight:
600; line-height: 1.6667; text-transform: u= ppercase; } .quoteblock
.attribution .citetitle, .verseblock .attribution .citetitle { = color:
rgb(88, 88, 88); } .quoteblock .attribution cite, .verseblock
.attribution cite { font-size: 1= em; } .quoteblock blockquote {
font-style: italic; margin: 0px; padding: 0px; } .quoteblock blockquote
.content \> :first-child { margin-top: 0px; } .quoteblock blockquote
.content \> :first-child::before { color: light-dark(=
#e00,var(\--rh-color-text-secondary-on-dark,#c7c7c7)); content:
\"=C3=A2=E2= =82=AC=C5=93\"; display: block; float: left; font-size:
2.75rem; font-style:= normal; line-height: 1.125em; margin-right:
0.5rem; } .quoteblock blockquote .content \> :first-child .content \>
:first-child::bef= ore { content: none; } .imageblock { margin: 1rem
0px; } .imageblock.pullleft { float: left; margin-right: 3rem; width:
25rem; } \@media (min-width: 768px) { .imageblock.pullleft {
margin-left: -1rem; } } .imageblock.pullright { float: right;
margin-left: 3rem; width: 25rem; } \@media (min-width:768) {
.imageblock.pullright { margin-right: -2rem; } } \@media (min-width:
1100px) { .imageblock.pullright { margin-right: -10rem; } }
.imageblock.interrupter { margin: 2rem 0px; } \@media (min-width: 768px)
{ .imageblock.interrupter { margin-left: -1rem; margin-right: -2rem; }
.imageblock.interrupter .caption { margin-left: 1rem; margin-right:
2rem;= } } \@media (min-width: 1100px) { .imageblock.interrupter {
margin-right: -10rem; } .imageblock.interrupter .caption { margin-right:
10rem; } } .imageblock.interrupter img { max-width: 100%; } .imageblock
.caption { color: rgb(88, 88, 88); display: block; font-size: 0=
.875rem; line-height: 1.6667; margin: 0.5rem 0px 0px; }
.rhdocs-footnotes { border-top: 0.0625rem solid rgb(210, 210, 210);
margin:= 3rem 0px 1rem; padding: 1rem 0px 0px; } .rhdocs-footnotes \> ol
{ margin: 0px; padding: 0px 0px 0px 1.5rem; } \@supports
(counter-reset:footnotenum) { .rhdocs-footnotes \> ol { counter-reset:
footnotenum 0; list-style: none; = padding: 0px; } .rhdocs-footnotes \>
ol \> li { counter-increment: footnotenum 1; } .rhdocs-footnotes \> ol
\> li::before { color: rgb(88, 88, 88); content: \"\[= \"
counter(footnotenum) \"\]\"; display: inline-block; margin-right:
0.25rem; } } .rhdocs-footer { background: rgb(237, 237, 237); color:
rgb(21, 21, 21); fo= nt-size: 0.875rem; line-height: 1.6667; margin:
3rem 0px 0px; padding: 1rem= ; } .center { margin-left: auto;
margin-right: auto; } .stretch { width: 100%; } .visually-hidden {
overflow: hidden; position: absolute; clip: rect(0px, 0p= x, 0px, 0px);
border: 0px; height: 0.0625rem; margin: -0.0625rem; padding: = 0px;
width: 0.0625rem; } .rh-docs-legal-notice { margin-top: 4em; } pre,
pre\[class\] { margin: 0px; padding: 1.25em 1em; position: relative; }
code\[class\*=3D\"language-\"\], pre\[class\*=3D\"language-\"\] { color:
rgb(21, 21, = 21); tab-size: 4; } code.language-none,
code.language-text, code.language-txt, pre.language-non= e,
pre.language-text, pre.language-txt { color: rgb(21, 21, 21); }
code\[class\*=3D\"language-\"\] ::selection,
code\[class\*=3D\"language-\"\]::selecti= on,
pre\[class\*=3D\"language-\"\] ::selection,
pre\[class\*=3D\"language-\"\]::selec= tion {
\--\_selected-text-background: light-dark(#b4d7ff,#395676); } :not(pre)
\> code\[class\*=3D\"language-\"\] { border-radius: 0.2em; padding: 0.1=
em; white-space: normal; } .rhdocs.local-render { margin: 0px auto;
max-width: 45.8125rem; padding: 0p= x 1.5rem; } \@media print { .field
code, .field pre, code\[class\*=3D\"language-\"\], pre,
pre\[class\*=3D\"l= anguage-\"\] { white-space: pre-wrap !important;
overflow-wrap: break-word !i= mportant; word-break: break-word
!important; } } .book-nav\_\_list\[class\] { display: flex;
justify-content: space-between; lin= e-height:
var(\--jupiter\_\_lineHeight\--xs,1.3333); list-style: none; margin: =
5rem 0px 0px; padding: 0px; } \@media (min-width: 1200px) {
.book-nav\_\_list\[class\] { display: grid; gap: 2rem;
grid-template-columns:= repeat(2, minmax(0px, 1fr)); } }
.book-nav\_\_item a { display: inline-block; font-size: 0.875rem;
font-weight= : 500; padding-left: 1.25rem; position: relative;
text-transform: uppercase= ; } .book-nav\_\_item a::before { background:
url(\"/sites/dxp-docs/penumbra-dist/=
jupiter/images/arrow-down-solid.svg\") 0% 0% / contain no-repeat;
content: \"= \"; display: block; height: 0.875rem; left: 0px; position:
absolute; top: 0.= 125rem; transform: rotate(90deg); width: 0.875rem; }
.book \> .titlepage:not(:last-child), .rhdocs .chapter, section\[id\] {
paddin= g-bottom: 3.75rem; } .book \> .titlepage .chapter:last-child,
.book \> .titlepage section\[id\]:last= -child, .chapter
.chapter:last-child, .chapter section\[id\]:last-child, sect= ion\[id\]
.chapter:last-child, section\[id\] section\[id\]:last-child { margin-bo=
ttom: -3.75rem; } .rhdocs .codeblock\_\_wrapper + section\[id\], pre +
section\[id\] { padding-top:= 3.75rem; } .rhdocs .cta-link { font-size:
inherit; } .rhdocs a { overflow-wrap: break-word; } .rhdocs .caution,
.rhdocs .important, .rhdocs .note, .rhdocs .tip, .rhdocs = .warning {
padding: 0.888889em; position: relative; } .rhdocs .QSIPopOver { bottom:
18.75rem !important; top: auto !important; } .rhdocs .alert { position:
relative; } .rhdocs button.dismiss-button { background: none; border:
0px; cursor: poin= ter; height: 2.5rem; margin-top: -1.25rem; padding:
0px; position: absolute= ; right: 0.3125rem; text-align: center; top:
50%; width: 2.5rem; z-index: 5= 0; } .rhdocs
button.dismiss-button::after { content: \"=EF=84=89\"; display: inlin=
e-block; font-family: rh-web-iconfont; font-size: 1.3125rem; font-style:
no= rmal; font-variant: normal; font-weight: 400; line-height: 2.5rem;
opacity:= 0.3; text-decoration: inherit; text-rendering:
optimizelegibility; -webkit= -font-smoothing: antialiased;
text-transform: none !important; } .rhdocs .book \> .titlepage, .rhdocs
.chapter, .rhdocs section\[id\] { padding= -bottom:
var(\--rh-space-4xl,64px); } .rhdocs .alert { border: 0px;
border-radius: 0px; } .rhdocs .alert \> h2:first-child, .rhdocs .alert
\> h3:first-child, .rhdocs .= alert \> h4:first-child, .rhdocs .alert \>
h5:first-child, .rhdocs .alert \> h= 6:first-child, .rhdocs .alert \>
p:first-child { margin-top: 0px !important;= } .rhdocs .alert \>
p:last-child { margin-bottom: 0px !important; } .rhdocs
.alert-w-icon\[class\] { padding-left: 2.8125rem; } .rhdocs
.alert-w-icon .alert-icon { float: left; font-size: 1.125rem; margi=
n-left: -1.875rem; margin-right: 0.625rem; } .rhdocs .alert-w-icon
.alert-icon\[class\*=3D\" rh-icon-\"\], .rhdocs .alert-w-i= con
.alert-icon\[class\^=3D\"rh-icon-\"\] { font-size: 2.25rem; line-height:
1em= ; margin-left: -2.5rem; margin-top: -0.375rem; } .rhdocs
.alert-w-icon .alert-icon\[class\*=3D\" icon-innov-prev\"\], .rhdocs
.al= ert-w-icon .alert-icon\[class\^=3D\"icon-innov-prev\"\] {
font-size: 1.3125rem; = margin-top: 0.25rem; } .rhdocs
.alert-w-icon.alert-plain { background: none; color: rgb(21, 21, 21= );
padding-left: 5rem; } .rhdocs .alert-w-icon.alert-plain .alert-icon {
font-size: 3rem; margin-lef= t: -4.375rem; margin-right: 0px; } .rhdocs
.alert-w-icon.alert-plain.alert-success .alert-icon { color: rgb(63= ,
156, 53); } .rhdocs .alert-w-icon.alert-plain.alert-info .alert-icon {
color: rgb(0, 13= 6, 206); } .rhdocs
.alert-w-icon.alert-plain.alert-warning .alert-icon { color: rgb(24= 0,
171, 0); } .rhdocs .alert-w-icon.alert-plain.alert-danger .alert-icon {
color: rgb(238= , 0, 0); } #target_banner .copy-url { float: right;
margin-top: 0px; } #target_banner .dropdown-menu { font-size: inherit; }
.titlepage .svg-img\[data\*=3D\"title_logo.svg\"\] { margin: 1.5rem 0px;
width: = 15rem; } .para { margin: 1.49963rem 0px; } .para\[class\] {
margin-bottom: 1.49963rem; } dd { margin-bottom: 2.5rem; } .rhdocs
.card-light, .rhdocs .card-light-gray, .rhdocs .card-light-grey { b=
ackground: rgb(240, 240, 240); border: 0.0625rem solid rgb(240, 240,
240); = color: rgb(21, 21, 21); } .rhdocs
.card-light-gray.push-bottom:first-child, .rhdocs .card-light-grey.=
push-bottom:first-child, .rhdocs .card-light.push-bottom:first-child {
marg= in-bottom: 3.125rem !important; } .rhdocs .card-light a.card-link,
.rhdocs .card-light h1, .rhdocs .card-ligh= t h2, .rhdocs .card-light
h3, .rhdocs .card-light h4, .rhdocs .card-light h= 5, .rhdocs
.card-light h6, .rhdocs .card-light-gray a.card-link, .rhdocs .c=
ard-light-gray h1, .rhdocs .card-light-gray h2, .rhdocs .card-light-gray
h3= , .rhdocs .card-light-gray h4, .rhdocs .card-light-gray h5, .rhdocs
.card-l= ight-gray h6, .rhdocs .card-light-grey a.card-link, .rhdocs
.card-light-gre= y h1, .rhdocs .card-light-grey h2, .rhdocs
.card-light-grey h3, .rhdocs .ca= rd-light-grey h4, .rhdocs
.card-light-grey h5, .rhdocs .card-light-grey h6 = { color: rgb(21, 21,
21); } .rhdocs .card-light-gray.card-active::after, .rhdocs
.card-light-grey.card-= active::after, .rhdocs
.card-light.card-active::after { border-top-color: r= gb(240, 240, 240);
} .rhdocs .card-md, .rhdocs .card-narrow { display: block; padding:
1.1875rem= ; white-space: normal; overflow-wrap: break-word; } .rhdocs
.card .card-heading.card-heading-sm, .rhdocs .card-sm .card .card-h=
eading { font-size: 1.0625em; font-weight: 500; line-height: 1.5; }
.rhdocs .card .card-heading.card-heading-flush { margin-bottom: 0.25rem;
} .rhdocs .card .card-heading.card-heading-red { color: rgb(209, 0, 0);
} .rhdocs .card \> p { margin-top: 0px; } .rhdocs .card \> p:last-child
{ margin-bottom: 0px; } .rhdocs .new-experience { background-color:
rgb(231, 241, 250); border: 0.0= 625rem solid rgb(190, 225, 244);
font-size: 1rem; margin: 1.5rem; padding: = 1.5rem; position: relative;
z-index: 1; } \@media (min-width: 48rem) { .new-experience { display:
flex; } .new-experience\--contained { left: 50%; position: relative;
transform: tr= anslate(-50%); width: calc(-2.5rem + 100vw); } }
.new-experience\_\_primary-content { flex-grow: 1; } \@media (min-width:
48rem) { .new-experience\_\_primary-content { margin-right: 1.25rem; } }
.new-experience\_\_title { font-size: inherit; font-weight: inherit;
line-hei= ght: 1.6; margin: 0px; padding: 0px; }
.new-experience\_\_title + a, .new-experience\_\_title + pfe-cta {
display: inl= ine-block; margin-top: 1.5em; }
.new-experience\_\_secondary-content { min-width: 12.5rem; } \@media
(min-width: 48rem) { .new-experience\_\_secondary-content { text-align:
right; } } .example { border-left: 0.3125rem solid rgb(204, 204, 204);
margin-bottom: = 2rem; padding: 1rem 0px 1rem 1rem; }
dl.calloutlist\[class\] { display: grid; gap: 1.25em 0.75em;
grid-template-co= lumns: min-content 1fr; } dl.calloutlist\[class\] dt {
float: none; margin: 0px; padding: 0px; } dl.calloutlist\[class\] dd {
margin: 0px; padding: 0px; } dl.calloutlist\[class\] dd \> :first-child
{ margin-top: 0px; } dl.calloutlist\[class\] dd \> :last-child {
margin-bottom: 0px; } .toast { background-color: rgba(0, 0, 0, 0.9);
bottom: 0.9375rem; box-shado= w: rgba(0, 0, 0, 0.26) 0px 0.125rem
0.3125rem; color: rgb(255, 255, 255); l= eft: 0.9375rem; max-width:
32.8125rem; min-width: 6.25rem; padding: 0.9375r= em; position: fixed;
right: 0.9375rem; transform: translate3d(0px, 150%, 0p= x); transition:
transform 0.2s cubic-bezier(0.465, 0.183, 0.153, 0.946); wi= ll-change:
transform; z-index: 999; } .toast.show { transform: translateZ(0px); }
.toast a { color: rgb(255, 255, 255); text-decoration: underline; }
.toast a:focus, .toast a:hover { color: rgb(43, 154, 243); } .toast
a.btn { text-decoration: none; } .toast .btn.btn-link { color: rgb(255,
255, 255); } .toast .close { color: rgb(255, 255, 255); opacity: 0.3;
text-decoration: n= one; } .toast .close:focus, .toast .close:hover {
color: rgb(255, 255, 255); opaci= ty: 0.5; }
.no-csstransforms3d.csstransitions .toast { transition: 0.2s
cubic-bezier(0= .465, 0.183, 0.153, 0.946); } .no-csstransforms3d .toast
{ opacity: 0; visibility: hidden; } .no-csstransforms3d .toast.show {
opacity: 1; visibility: visible; } .annotator-outer\[class\]\[class\] {
display: none; flex-direction: column; fle= x-grow: 1; height: auto;
margin: 0px; position: static; width: auto; } \@media (min-width:
1400px) { .annotator-outer\[class\]\[class\] { display: flex; } }
.annotator-frame\[class\] \* { height: auto; } \@media (min-width:
1400px) { .annotator-frame .h-sidebar-iframe\[class\] { position:
static; width: calc= (100% + 1.5rem); } }
.annotator-toolbar\[class\]\[class\] { position: static; width: auto; }
.annotator-toolbar \> ul, .annotator-toolbar \> ul \> li { display:
block; hei= ght: auto; list-style: none; margin: 0px; padding: 0px;
width: auto; } .annotator-toolbar \> ul \> li { display: flex;
justify-content: flex-end; } .annotator-frame\[class\]
.annotator-frame-button\--sidebar_toggle, .annotator= -outer
.annotator-frame-button\[class\]\[class\], .app-content-wrapper \* {
font= -family: RedHatText, \"Red Hat Text\", \"Helvetica Neue\", Arial,
sans-serif !i= mportant; } .annotator-outer
.annotator-frame-button\[class\]\[class\] { font-size: 0.9375r= em;
font-weight: 500; height: auto; line-height: 1.333; margin-right: 1.875=
rem; padding: 0.75em 1em; position: static; } \@media (min-width:
1400px) { .annotator-outer .annotator-frame-button\[class\]\[class\] {
margin-right: 0p= x; } } .annotator-outer iframe { flex-grow: 1;
margin-bottom: 1.25rem; } \@media (min-width: 1400px) { .annotator-outer
iframe { min-height: 37.5rem; } } .producttitle { color:
light-dark(var(\--rh-color-black,#000),var(\--rh-color= -white,#fff));
font-size: 1.25rem; text-transform: uppercase; } .producttitle
.productnumber { color: light-dark(var(\--jupiter\_\_palette\_\_re=
d\--50,#e00),var(\--rh-color-text-secondary-on-dark,#c7c7c7)); }
.cp-modal-open, .zoom-open { overflow: hidden; } .cp-modal,
.cp-video-modal, .zoom-modal { inset: 0px; display: none; opacit= y: 0;
outline: 0px; overflow: hidden; position: fixed; transition: 0.2s cub=
ic-bezier(0.465, 0.183, 0.153, 0.946); z-index: 1050; } .rhdocs
.in.cp-modal, .rhdocs .in.cp-video-modal, .rhdocs .in.zoom-modal { =
display: block; opacity: 1; overflow: hidden auto; } .rhdocs .cp-modal
.close, .rhdocs .cp-video-modal .close, .rhdocs .zoom-mod= al .close {
background-color: rgb(255, 255, 255); border-radius: 50%; color= :
rgb(26, 26, 26); font-size: 1.75rem; height: 1.75rem; line-height:
1.75re= m; margin-bottom: 0.375rem; margin-top: 0px; opacity: 0.9;
position: absolu= te; right: -0.5rem; text-shadow: none; top: 0px;
width: 1.75rem; } .cp-modal .close::after, .cp-video-modal
.close::after, .zoom-modal .close:= :after { line-height: 1.75rem; }
.cp-modal-wrap, .zoom-wrap { margin: 0.625rem; padding-top: 0.5rem;
positio= n: relative; } \@media (min-width: 48rem) { .rhdocs
.cp-modal-wrap, .rhdocs .zoom-wrap { margin: 2.8125rem auto; widt= h:
38.4375rem; } } \@media (min-width: 62rem) { .rhdocs .cp-modal-wrap,
.rhdocs .zoom-wrap { width: 49.8958rem; } } \@media (min-width: 75rem) {
.rhdocs .cp-modal-wrap, .rhdocs .zoom-wrap { width: 60.3125rem; } }
.rhdocs .cp-modal-body :last-child { margin-bottom: 0px; } .rhdocs
.cp-modal-backdrop, .rhdocs .zoom-backdrop { background-color: rgb(= 0,
0, 0); inset: 0px; display: none; opacity: 0; position: fixed;
transitio= n: opacity 0.2s cubic-bezier(0.465, 0.183, 0.153, 0.946);
z-index: 1040; } .rhdocs .in.cp-modal-backdrop, .rhdocs
.in.zoom-backdrop { display: block; = opacity: 0.8; } .rhdocs
.cp-modal-body { background: rgb(255, 255, 255); padding: 1.875rem;= }
.rhdocs .cp-modal\[data-cp-modal-video=3D\"true\"\] .cp-modal-body,
.rhdocs .cp= -video-modal .cp-modal-body { padding: 0px; } .rhdocs
\[data-action=3D\"zoom\"\] { position: relative; } .rhdocs
\[data-action=3D\"zoom\"\]::after { background: rgba(0, 0, 0, 0.4); bot=
tom: 0px; color: rgb(255, 255, 255); display: inline-block; font-family:
rh= -web-iconfont; font-style: normal; font-variant: normal;
font-weight: 400; = line-height: 1; padding: 0.375rem; position:
absolute; right: 0px; text-ren= dering: optimizelegibility;
-webkit-font-smoothing: antialiased; text-decor= ation: none !important;
text-transform: none !important; } .rhdocs
\[data-action=3D\"zoom\"\]:focus::after, .rhdocs
\[data-action=3D\"zoom\"\]= :hover::after { background: rgba(0, 0, 0,
0.9); } .rhdocs .zoom-wrap .zoom-larger { text-align: center; } .rhdocs
.zoom-wrap .zoom-larger a { color: rgb(255, 255, 255); } .rhdocs
.zoom-wrap .zoom-larger a:focus, .rhdocs .zoom-wrap .zoom-larger a:=
hover { color: rgb(255, 255, 255); text-decoration: underline; } .rhdocs
.zoom-wrap .zoom-larger a::after { content: \"=C3=A2=C2=BF=C2=BB\"; d=
isplay: inline-block; margin-left: 0.25rem; } .rhdocs .zoom-body {
background: rgb(255, 255, 255); border-radius: 0.5rem;= margin: 0px 0px
1rem; padding: 1rem; text-align: center; } .rhdocs .zoom-body
.video-wrapper { height: 0px; overflow: hidden; padding-= bottom:
56.25%; position: relative; } .rhdocs .zoom-body
.video-wrapper\[data-aspect-ratio=3D\"4:3\"\] { padding-bott= om: 75%; }
.rhdocs .zoom-body iframe { height: 100%; left: 0px; position: absolute;
to= p: 0px; width: 100%; } .rhdocs .para \> .title\[class\], .rhdocs
p.title\[class\] { font-size: 1rem; fo= nt-style: normal; font-weight:
700; line-height: 1.6667; margin: 1.25rem 0p= x 0px; text-transform:
none; } .rhdocs .para \> .title\[class\] + .content \> :first-child,
.rhdocs .para \> .t= itle\[class\] + p, .rhdocs p.title\[class\] +
.content \> :first-child, .rhdocs = p.title\[class\] + p { margin-top:
0px; } .rhdocs \[class\] pre .caution, .rhdocs \[class\] pre .important,
.rhdocs \[clas= s\] pre .note, .rhdocs \[class\] pre .tip, .rhdocs
\[class\] pre .warning { back= ground: transparent; border: 0px; color:
inherit; font: inherit; margin: 0p= x; padding: 0px; } .rhdocs \[class\]
pre .caution::after, .rhdocs \[class\] pre .important::after,= .rhdocs
\[class\] pre .note::after, .rhdocs \[class\] pre .tip::after, .rhdocs=
\[class\] pre .warning::after { content: none; } .rhdocs \[class\]
code.email { background-color: transparent; font: inherit; = padding:
0px; } .rhdocs \[class\] .author { margin-bottom: 1.5rem; } .rhdocs
\[class\] .author .author { margin-bottom: 0px; } .rhdocs table {
margin: 2rem 0px; } .rhdocs \[class\] table { width: auto; } .rhdocs
table .table-contents table { max-width: 100%; overflow: auto; } .rhdocs
rh-table table { margin: 0px; max-width: 9999em; overflow: visible;= }
.rhdocs td, .rhdocs th { border-left: 0px; padding: 0.5em 1rem;
transition:= background 0.25s ease-out; } .rhdocs
td.content\--md\[class\]\[class\], .rhdocs
th.content\--md\[class\]\[class\] = { min-width: 13em; } .rhdocs
td.content\--lg\[class\]\[class\], .rhdocs
th.content\--lg\[class\]\[class\] = { min-width: 20em; } .rhdocs thead
th { padding-top: 1.5em; } .rhdocs caption { color:
var(\--pfe-table\_\_caption\--Color,currentColor); fon= t-weight: 700;
margin-bottom: 0.5rem; margin-top: 0.5rem; text-align: cente= r; }
.rhdocs .revhistory table td, .rhdocs .revhistory table th {
border-color: = transparent; } .rhdocs .revhistory table td { padding:
0.625rem 0.875rem; } .rhdocs .revhistory table.simplelist { margin: 0px;
} \@media print { #masthead { display: none !important; } }
.rh-table\--is-full-screen #to-top { display: none; } .rhdocs {
\--rh-table\--maxHeight: calc(100vh - 6.25rem); color: rgb(21, 21, =
21); font-family: var(\--rh-font-family-body-text,RedHatText,\"Red Hat
Text\",= \"Noto Sans Arabic\",\"Noto Sans Hebrew\",\"Noto Sans
JP\",\"Noto Sans KR\",\"Noto S= ans Malayalam\",\"Noto Sans SC\",\"Noto
Sans TC\",\"Noto Sans Thai\",Helvetica,Ari= al,sans-serif); font-size:
var(\--rh-body-copy-lage,1.125rem); line-height: = 1.6667; tab-size: 4;
} .rhdocs rh-codeblock::slotted(#content) { border-radius: 0.25rem; }
.rhdocs rh-codeblock .screen { display: grid; grid-template-columns: 1fr
4.= 375rem; } .rhdocs
rh-codeblock\[class\]\[class\]\[class\]\[class\]\[class\] { max-width:
99999e= m; } .rhdocs .codeblock\_\_copy span { display: block; height:
0px; position: abso= lute; visibility: hidden; width: 0px; } .rhdocs
.codeblock\_\_copy:focus { outline: currentcolor dashed 0.0625rem; }
.rhdocs .codeblock\_\_copy svg#icon\--copy { height: 1rem; width: 1rem;
} .rhdocs pre { border: 0px; max-height: max-content; } .rhdocs pre,
pre\[class\] { margin: 0px; padding: 1.25em 1em; position: relat= ive; }
.rhdocs rh-code-block \> div.codeblock\_\_inner-wrapper \> pre, .rhdocs
rh-code= -block \> div.codeblock\_\_inner-wrapper \> pre\[class\] {
margin: 0px; padding: = 0px; position: relative; } .rhdocs rh-code-block
{ background: light-dark(var(\--rh-color-surface-light=
er,#f2f2f2),oklch(from var(\--rh-color-surface-dark,#383838)
calc(l\*.82) c h= )); } .rhdocs rh-code-block \> pre::after, .rhdocs
rh-code-block \> pre::before, .r= hdocs rh-code-block \> script::after,
.rhdocs rh-code-block \> script::before= { content: \"\"; display:
block; height: 10px; } .rhdocs rh-code-block pre:has(+ rh-badge)::after,
.rhdocs rh-code-block scr= ipt:has(+ rh-badge)::after { display: none; }
.rhdocs rh-code-block rh-badge + pre::before, .rhdocs rh-code-block
rh-badg= e + script::before { display: none; } .rhdocs
code\[class\*=3D\"language-\"\], pre\[class\*=3D\"language-\"\] { color:
rgb(= 21, 21, 21); tab-size: 4; } .rhdocs code.literal { background:
light-dark(#eee,var(\--rh-color-surface-d= ark,#383838)); border-radius:
0.25rem; color: light-dark(var(\--rh-color-bla=
ck,#000),var(\--rh-color-white,#fff)); font-size: 0.875rem; line-height:
1.6= 667; overflow-wrap: break-word; padding: 0.125em 0.5em; word-break:
break-w= ord; } .rhdocs code.literal, .rhdocs kbd, .rhdocs span.keycap {
font-family: RedHa= tMono, \"Red Hat Mono\", Consolas, monospace; }
.rhdocs kbd, .rhdocs span.keycap { background-color: rgb(238, 238, 238);
ba= ckground-image: linear-gradient(rgb(221, 221, 221), rgb(238, 238,
238), rgb= (255, 255, 255)); border-radius: 0.1875rem; box-shadow:
rgb(255, 255, 255) = 0px -0.0625rem, rgb(170, 170, 170) 0px 0.0625rem
0px 0.1875rem; font-size: = 90%; font-weight: 400; margin: 0px 0.25rem;
padding: 0.125rem 0.375rem; } .rhdocs ol, .rhdocs ul { margin: 1rem 0px;
padding: 0px 0px 0px 1.5rem; } .rhdocs
.\_additional-resources\[class\]\[class\] ul { border: 0px; list-style:
= none; margin: 0px; padding: 0px; position: relative; } .rhdocs
.\_additional-resources\[class\]\[class\] li { border-bottom: 0.0625rem
= solid rgb(210, 210, 210); box-sizing: content-box; margin: 0px;
padding: 1r= em 1.5rem 1rem 0px; break-inside: avoid; } .rhdocs
.\_additional-resources\[class\]\[class\] li:last-child { border: 0px; }
.rhdocs section.section#additional_resource
.additional-resources\_\_heading,= .rhdocs
section.section#additional_resource .heading, .rhdocs section.sect=
ion#additional_resource h1, .rhdocs section.section#additional_resource
h2,= .rhdocs section.section#additional_resource h3, .rhdocs
section.section#ad= ditional_resource h4, .rhdocs
section.section#additional_resource h5, .rhdo= cs
section.section#additional_resource h6, .rhdocs
section.section#addition= al_resource p.title { display: block;
font-family: RedHatDisplay, \"Red Hat = Display\", \"Helvetica Neue\",
Arial, sans-serif; font-size: 1.125rem; font-we= ight: 700; line-height:
1.5rem; margin: 0px 0px 0.5rem; padding: 0px; text-= transform:
uppercase; } .rhdocs section.section:first-of-type { margin-top:
var(\--rh-space-4xl,64px= ); } .rhdocs section.section p {
margin-bottom: var(\--rh-space-lg,16px); margin-= top: 0px;
overflow-wrap: break-word; } .rhdocs h1:first-of-type, .rhdocs
h2:first-of-type, .rhdocs h3:first-of-typ= e, .rhdocs h4:first-of-type,
.rhdocs h5:first-of-type, .rhdocs h6:first-of-= type { margin-top: 0px;
} .rhdocs dl { display: block; margin-block: 1em; margin-inline: 0px; }
.rhdocs .para { margin: 1.49963rem 0px; } .rhdocs
dl.calloutlist\[class\] dt { float: none; margin: 0px; padding: 0px; = }
.rhdocs dl.calloutlist\[class\] dd \> :last-child { margin-bottom: 0px;
} .rhdocs dl.calloutlist\[class\] { display: grid; gap: 1.25em 0.75em;
grid-tem= plate-columns: fit-content(40%) 1fr; } .rhdocs .calloutlist dt
{ clear: left; display: flex; flex-wrap: wrap; floa= t: left; margin:
0px; padding: 0px 0.5rem 0px 0px; } .rhdocs .calloutlist dt
a:not(:first-child) { padding-left: 4px; } .rhdocs
dl.calloutlist\[class\] dd { margin: 0px; padding: 0px; } .rhdocs
.callout, .rhdocs .colist \> ol \> li::before, .rhdocs .conum { backg=
round:
light-dark(var(\--rh-color-status-info-on-light,#5e40be),var(\--rh-col=
or-status-info-on-dark,#b6a6e9)); border-radius: 50%; color:
light-dark(var=
(\--rh-color-text-primary-on-dark,#fff),var(\--rh-color-text-primary-on-light=
,#151515)); display: inline-block; font-family:
var(\--rh-font-family-code,R= edHatMono,\"Red Hat Mono\",\"Courier
New\",Courier,monospace); font-size: 0.75r= em; font-style: normal;
font-weight: 600; line-height: 1.5rem; min-height: = 24px; min-width:
24px; padding: 0px; position: relative; text-align: center= ; top:
-0.125em; vertical-align: middle; } .rhdocs img, .rhdocs object, .rhdocs
svg { display: inline-block; max-width= : 100%; vertical-align: middle;
} .rhdocs .titlepage .svg-img\[data\*=3D\"title_logo.svg\"\] { margin:
1.5rem 0px;= width: 15rem; } .rhdocs\[class\] .author { margin-bottom:
1.5rem; } .rhdocs\[class\] .author .author { margin-bottom: 0px; }
.rhdocs .para \> .title\[class\], p.title\[class\] { font-size: 1rem;
font-style= : normal; font-weight: 700; line-height: 1.6667; margin:
1.25rem 0px 0px; } .rhdocs .example { border-left: 0.3125rem solid
rgb(204, 204, 204); margin-= bottom: 2rem; padding: 1rem 0px 1rem 1rem;
} .rhdocs code { background:
light-dark(#eee,var(\--rh-color-surface-dark,#383= 838)); font-family:
RedHatMono, \"Red Hat Mono\", Consolas, monospace; font-s= ize:
0.875rem; line-height: 1.6667; overflow-wrap: break-word; padding: 0.1=
25em 0.5em; word-break: break-word; } .rhdocs .para\[class\] {
margin-bottom: 1.49963rem; } .rhdocs\[class\] code.email {
background-color: transparent; font: inherit; p= adding: 0px; }
rh-alert.admonition #description, rh-alert.admonition p { font-size:
var(\--= rh-font-size-body-text-md,1rem); } rh-alert { width:
fit-content; } .rhdocs .producttitle { color:
light-dark(var(\--rh-color-black,#000),var(\--= rh-color-white,#fff));
font-size: 1.25rem; text-transform: uppercase; } .rhdocs dl { margin:
1rem 0px; } .rhdocs dl dt { font-weight: 600; margin: 0.5rem 0px; }
.rhdocs ol ol { list-style: lower-roman; } .rhdocs
.codeblock\--processed pf-clipboard-copy::part(input), .rhdocs .code=
block\--processed pf-clipboard-copy::part(span) { display: none; }
.calloutlist div.para { margin: 0px; } rh-alert.admonition {
margin-bottom: var(\--rh-space-lg,1rem); } .guibutton, .guimenu,
.guimenuitem { font-weight: 700; } .guibutton { font-size: 90%; padding:
0.1875rem; } .guibutton::before { content: \"\[\"; } .guibutton::after {
content: \"\]\"; } .docs-content-container, .rhdocs {
\--rh-table\--maxHeight: calc(100vh - 6.25= rem); color:
light-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-whit=
e,#fff)); font-family: RedHatText, \"Red Hat Text\", \"Helvetica Neue\",
Arial,= sans-serif; font-size: 1.125rem; line-height: 1.6667; tab-size:
4; } pre\[hidden\] { display: none; }
.codeblock\[class\]\[class\]\[class\]\[class\]\[class\] { max-width:
99999em; } .codeblock\_\_wrapper { background:
light-dark(var(\--rh-color-surface-lighter=
,#f2f2f2),var(\--rh-color-surface-dark,#383838)); margin: 1rem 0px;
overflow= : visible; position: relative; transform: translate(0px);
z-index: 0; } .codeblock\_\_inner-wrapper::after { content: \"\";
display: block; min-height:= 0.625rem; width: 4.375rem; }
.codeblock\_\_copy { \--pfe-clipboard\--icon\--Color\--hover: #06c;
appearance: n= one; background: rgb(240, 239, 239); height: 1.75rem;
left: calc(100% - 2.7= 5rem - var(\--scrollbar\_\_width, 0px)); padding:
0.3125rem 0.375rem; position= : absolute; top: 1rem; width: 1.75rem;
z-index: 2; } .codeblock\_\_inner-wrapper pre { border: 0px; max-height:
max-content; } .pfe-clipboard:not(\[copied\])
.pfe-clipboard\_\_text\--success, :host(:not(\[cop= ied\]))
.pfe-clipboard\_\_text\--success { display: none !important; }
.codeblock\[class\] { margin: 0px; overflow: visible; padding-right:
0px; } pre { display: inline; font-size: 0.8125rem; line-height:
1.42857; margin: = 0px 0px 0.625rem; word-break: break-all;
overflow-wrap: break-word; backgro= und-color:
light-dark(var(\--rh-color-surface-lighter,#f2f2f2),var(\--rh-colo=
r-surface-dark,#383838)); border: 0.0625rem solid rgb(204, 204, 204);
borde= r-radius: 0.25rem; } .docs-content-container pre, .rhdocs pre,
pre { color: light-dark(var(\--rh-=
color-gray-95,#151515),var(\--rh-color-white,#fff)); }
.docs-content-container pre, .rhdocs pre { background:
light-dark(var(\--rh-=
color-surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,#383838));
font-= family: RedHatMono, \"Red Hat Mono\", Consolas, monospace;
font-size: 0.875re= m; line-height: 1.6667; overflow-wrap: normal;
white-space: pre; word-break= : normal; } .rhdocs pre\[class\] {
line-height: 27px; overflow-x: auto; } rh-codeblock
pre\[class\]\[class\] { overflow-x: auto; }
.pfe-clipboard\_\_text\--success { background-color: rgb(221, 221, 221);
borde= r: 1px solid rgb(0, 0, 0); border-radius: 2px; }
.content-code-block-container { position: relative; }
.content-code-block-container .content-code-block-container-actions {
displ= ay: flex; flex-direction: column; height: auto; justify-content:
flex-start= ; position: absolute; right: 0px; top: 0px; width: 57px;
z-index: 2; } .content-code-block-container
.content-code-block-container-actions rh-tool= tip .shadow-fab {
align-items: center; background: rgba(0, 0, 0, 0); border= : none;
border-radius: var(\--rh-border-radius-default,3px); display: flex; =
height: var(\--rh-length-3xl,48px); justify-content: center; padding:
var(\--= rh-space-md,8px); width: var(\--rh-length-3xl,48px); }
.content-code-block-container .content-code-block-container-actions
rh-tool= tip .shadow-fab svg { color: var(\--rh-color-text-primary);
height: var(\--rh= -size-icon-02,24px); width:
var(\--rh-size-icon-02,24px); }
.content-code-block-container\[data-text-wrapped=3D\"true\"\]
rh-code-block pre= code { overflow-wrap: break-word; white-space:
pre-wrap; word-break: break= -word; }
.content-code-block-container\[data-text-wrapped=3D\"false\"\]
rh-code-block pr= e code { overflow-wrap: normal; white-space: pre;
word-break: normal; } \@media (max-width: 768px) { .rhdocs h1 {
font-size: 29px; line-height: 37.7px; } .rhdocs h2 { font-size: 24px;
line-height: 31.2px; } .rhdocs h3 { font-size: 20px; line-height: 26px;
} .rhdocs h4, .rhdocs h5 { font-size: 18px; line-height: 23.4px; } } \*,
::after, ::before { box-sizing: border-box; } :root { \--rh-space-xs:
4px; \--rh-space-sm: 6px; \--rh-space-md: 8px; \--rh-sp= ace-lg: 16px;
\--rh-space-xl: 24px; \--rh-space-2xl: 32px; \--rh-space-3xl: 48= px;
\--rh-space-4xl: 64px; \--rh-space-5xl: 80px; \--rh-space-6xl: 96px;
\--rh-= space-7xl: 128px; \--rh-font-size-body-text-xs: .75rem;
\--rh-font-size-body-= text-sm: .875rem; \--rh-font-size-body-text-md:
1rem; \--rh-font-size-body-te= xt-lg: 1.125rem;
\--rh-font-size-body-text-xl: 1.25rem; \--rh-font-size-body-= text-2xl:
1.5rem; \--rh-font-size-heading-xs: 1.25rem; \--rh-font-size-headin=
g-sm: 1.5rem; \--rh-font-size-heading-md: 1.75rem;
\--rh-font-size-heading-lg= : 2.25rem; \--rh-font-size-heading-xl:
2.5rem; \--rh-font-size-heading-2xl: 3= rem;
\--pfe-navigation\--logo\--maxWidth: 200px;
\--pfe-navigation\_\_logo\--heigh= t: 40px;
\--pfe-navigation\--fade-transition-delay: .5s; \--pfe-navigation\_\_na=
v-bar\--highlight-color: var( \--rh-color-brand-red-on-dark,#e00 );
\--pf-glob= al\--icon\--FontSize\--sm: .75rem; color-scheme: light dark;
} body, html { color:
light-dark(var(\--rh-color-text-primary-on-light,#151515=
),var(\--rh-color-text-primary-on-dark,#fff)); font-family: \"Red Hat
Text\", = sans-serif; font-size: var(\--rh-font-size-body-text-md,1rem);
line-height: = var(\--rh-line-height-body-text,1.5); margin: 0px; }
html.theme-light { color-scheme: light; \--header-select:
url(\"data:image/sv= g+xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'= 10\' height=3D\'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%2315= 1515\'
d=3D\'M.678 0h8.644c.596 0 .895.797.497 1.195l-4.372 4.58c-.298.3-.695=
.3-.993 0L.18 1.196C-.216.797.081 0 .678 0\'/%3E%3C/svg%3E\");
\--ai-foundatio= n-container: var(\--rh-color-surface-lighter,#f2f2f2);
\--ai-foundation-image= -wrapper:
url(./ai-training-hero-blocks-light.DgHphzNg.webp); \--certificate=
-container: var(\--rh-color-surface-lighter,#f2f2f2);
\--certificate-image-wr= apper:
url(./ai-training-hero-blocks-light.DgHphzNg.webp); \--select-dropdow=
n-image: url(\"data:image/svg+xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www= .w3.org/2000/svg\' width=3D\'10\' height=3D\'6\'
fill=3D\'none\' viewBox=3D\'0 0 10= 6\'%3E%3Cpath fill=3D\'%23151515\'
d=3D\'M.678 0h8.644c.596 0 .895.797.497 1.1= 95l-4.372
4.58c-.298.3-.695.3-.993 0L.18 1.196C-.216.797.081 0 .678 0\'/%3E%=
3C/svg%3E\"); \--expert-hub-footer: linear-gradient(327.3deg,#fff
58.63%,#f2f= 2f2 80.42%); \--expert-hub-footer-wrapper:
url(./bg-cta-band-desktop.B1GFcRC= k.webp);
\--expert-hub-footer-mobile-wrapper: url(./bg-cta-band-mobile.Ch8Sm=
Ky6.webp); \--home-welcome-section:
linear-gradient(0deg,var(\--rh-color-gray= -10,#f2f2f2)
0%,var(\--rh-color-white,#fff) 50%); \--home-dark-dots-bg: url(.=
/docs-new-hero-desktop-light.BvTdfw7R.webp); } html.theme-dark {
color-scheme: dark; \--header-select: url(\"data:image/svg+=
xml;charset=3Dutf-8,%3Csvg xmlns=3D\'http://www.w3.org/2000/svg\'
width=3D\'10= \' height=3D\'6\' fill=3D\'none\' viewBox=3D\'0 0 10
6\'%3E%3Cpath fill=3D\'%23fff\'= d=3D\'M.678 0h8.644c.596 0 .895.797.497
1.195l-4.372 4.58c-.298.3-.695.3-.9= 93 0L.18 1.196C-.216.797.081 0 .678
0\'/%3E%3C/svg%3E\"); \--ai-foundation-con= tainer:
linear-gradient(309deg,var(\--rh-color-purple-70,#21134d) 21.34%,var=
(\--rh-color-black,#000) 92.49%); \--ai-foundation-image-wrapper:
url(./ai-tr= aining-hero-blocks-dark.C-W6u3Az.webp);
\--certificate-container: linear-gra=
dient(309deg,var(\--rh-color-purple-70,#21134d)
21.34%,var(\--rh-color-black,= #000) 92.49%);
\--certificate-image-wrapper: url(./ai-training-hero-blocks-d=
ark.C-W6u3Az.webp); \--select-dropdown-image:
url(\"data:image/svg+xml;charse= t=3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'10\' height= =3D\'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%23fff\'
d=3D\'M.= 678 0h8.644c.596 0 .895.797.497 1.195l-4.372
4.58c-.298.3-.695.3-.993 0L.18= 1.196C-.216.797.081 0 .678
0\'/%3E%3C/svg%3E\"); \--expert-hub-footer: linear=
-gradient(90deg,#151515,#21134d); \--expert-hub-footer-wrapper:
url(./bg-cta= -band-desktop.B1GFcRCk.webp);
\--expert-hub-footer-mobile-wrapper: url(./bg-=
cta-band-mobile-dark.tRg-muK0.webp); \--home-welcome-section:
linear-gradien= t(270deg,var(\--rh-color-black,#000)
0%,var(\--rh-color-purple-80,#1b0d33) 10= 0%); \--home-dark-dots-bg:
url(./docs-new-hero-desktop-dark.Df7w36hb.webp); = } h1 { font-weight:
var(\--rh-font-weight-heading-regular,400); } h1, h2, h3, h4, h5, h6 {
font-family: \"Red Hat Display\", sans-serif; } h2, h3, h4, h5, h6 {
font-weight: var(\--rh-font-weight-heading-medium,500);= } h1 {
font-size: var(\--rh-font-size-heading-xl,2.5rem); line-height: 52px; }
h2 { font-size: var(\--rh-font-size-heading-md,1.75rem); line-height:
36.4px= ; } h3 { font-size: var(\--rh-font-size-heading-sm,1.5rem);
line-height: 31.2px;= } h4 { font-size:
var(\--rh-font-size-heading-xs,1.25rem); line-height: 26px; = } h5 {
font-size: 18px; line-height: 23.4px; } main { line-height: 30px; }
main#main-content { background-color:
light-dark(var(\--rh-color-surface-lig=
htest,#fff),var(\--rh-color-surface-darkest,#151515)); } section {
padding-bottom: 3rem; padding-top: 3rem; } img { height: auto;
max-width: 100%; } a { color:
light-dark(var(\--rh-color-interactive-blue-darker,#06c),var(\--rh=
-color-interactive-primary-default-on-dark,#92c5f9)); text-decoration:
none= ; } a:hover { color:
light-dark(var(\--rh-color-interactive-blue-darkest,#004080=
),var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc)); }
rh-alert.html-container a { text-decoration: underline; } .container {
padding-left: 12px; padding-right: 12px; } .container, .container-fluid
{ margin-left: auto; margin-right: auto; width= : 100%; }
.container-fluid { padding: 12px; } \@media (min-width: 576px) {
.container { max-width: 540px; } } \@media (min-width: 768px) {
.container { max-width: 720px; } } \@media (min-width: 992px) {
.container { max-width: 960px; } } \@media (min-width: 1200px) {
.container { min-width: 1140px; } } \@media (min-width: 1400px) {
.container { min-width: 1320px; } } .grid { display: grid; gap:
var(\--rh-space-xl,24px); } .grid-center { margin: auto; }
.grid.grid-col-2 { grid-template-columns: repeat(2, 1fr); }
.grid.grid-col-3 { grid-template-columns: repeat(3, 1fr); }
.grid.grid-col-4 { grid-template-columns: repeat(4, 1fr); }
.grid.grid-col-5 { grid-template-columns: repeat(5, 1fr); }
.grid.grid-col-6 { grid-template-columns: repeat(6, 1fr); }
.grid.grid-col-7 { grid-template-columns: repeat(7, 1fr); }
.grid.grid-col-8 { grid-template-columns: repeat(8, 1fr); }
.grid.grid-col-9 { grid-template-columns: repeat(9, 1fr); }
.grid.grid-col-10 { grid-template-columns: repeat(10, 1fr); }
.grid.grid-col-11 { grid-template-columns: repeat(11, 1fr); }
.grid.grid-col-12 { grid-template-columns: repeat(12, 1fr); } \@media
(min-width: 576px) { .grid.grid-col-sm-2 { grid-template-columns:
repeat(2, 1fr); } .grid.grid-col-sm-3 { grid-template-columns: repeat(3,
1fr); } .grid.grid-col-sm-4 { grid-template-columns: repeat(4, 1fr); }
.grid.grid-col-sm-5 { grid-template-columns: repeat(5, 1fr); }
.grid.grid-col-sm-6 { grid-template-columns: repeat(6, 1fr); }
.grid.grid-col-sm-7 { grid-template-columns: repeat(7, 1fr); }
.grid.grid-col-sm-8 { grid-template-columns: repeat(8, 1fr); }
.grid.grid-col-sm-9 { grid-template-columns: repeat(9, 1fr); }
.grid.grid-col-sm-10 { grid-template-columns: repeat(10, 1fr); }
.grid.grid-col-sm-11 { grid-template-columns: repeat(11, 1fr); }
.grid.grid-col-sm-12 { grid-template-columns: repeat(12, 1fr); } }
\@media (min-width: 768px) { .grid.grid-col-md-2 {
grid-template-columns: repeat(2, 1fr); } .grid.grid-col-md-3 {
grid-template-columns: repeat(3, 1fr); } .grid.grid-col-md-4 {
grid-template-columns: repeat(4, 1fr); } .grid.grid-col-md-5 {
grid-template-columns: repeat(5, 1fr); } .grid.grid-col-md-6 {
grid-template-columns: repeat(6, 1fr); } .grid.grid-col-md-7 {
grid-template-columns: repeat(7, 1fr); } .grid.grid-col-md-8 {
grid-template-columns: repeat(8, 1fr); } .grid.grid-col-md-9 {
grid-template-columns: repeat(9, 1fr); } .grid.grid-col-md-10 {
grid-template-columns: repeat(10, 1fr); } .grid.grid-col-md-11 {
grid-template-columns: repeat(11, 1fr); } .grid.grid-col-md-12 {
grid-template-columns: repeat(12, 1fr); } } \@media (min-width: 992px) {
.grid.grid-col-lg-2 { grid-template-columns: repeat(2, 1fr); }
.grid.grid-col-lg-3 { grid-template-columns: repeat(3, 1fr); }
.grid.grid-col-lg-4 { grid-template-columns: repeat(4, 1fr); }
.grid.grid-col-lg-5 { grid-template-columns: repeat(5, 1fr); }
.grid.grid-col-lg-6 { grid-template-columns: repeat(6, 1fr); }
.grid.grid-col-lg-7 { grid-template-columns: repeat(7, 1fr); }
.grid.grid-col-lg-8 { grid-template-columns: repeat(8, 1fr); }
.grid.grid-col-lg-9 { grid-template-columns: repeat(9, 1fr); }
.grid.grid-col-lg-10 { grid-template-columns: repeat(10, 1fr); }
.grid.grid-col-lg-11 { grid-template-columns: repeat(11, 1fr); }
.grid.grid-col-lg-12 { grid-template-columns: repeat(12, 1fr); } }
.span-1 { grid-column: span 1; } .span-2 { grid-column: span 2; }
.span-3 { grid-column: span 3; } .span-4 { grid-column: span 4; }
.span-5 { grid-column: span 5; } .span-6 { grid-column: span 6; }
.span-7 { grid-column: span 7; } .span-8 { grid-column: span 8; }
.span-9 { grid-column: span 9; } .span-10 { grid-column: span 10; }
.span-11 { grid-column: span 11; } .span-12 { grid-column: span 12; }
\@media (min-width: 399px) { .span-xs-1 { grid-column: span 1; }
.span-xs-2 { grid-column: span 2; } .span-xs-3 { grid-column: span 3; }
.span-xs-4 { grid-column: span 4; } .span-xs-5 { grid-column: span 5; }
.span-xs-6 { grid-column: span 6; } .span-xs-7 { grid-column: span 7; }
.span-xs-8 { grid-column: span 8; } .span-xs-9 { grid-column: span 9; }
.span-xs-10 { grid-column: span 10; } .span-xs-11 { grid-column: span
11; } .span-xs-12 { grid-column: span 12; } } \@media (min-width: 768px)
{ .span-md-1 { grid-column: span 1; } .span-md-2 { grid-column: span 2;
} .span-md-3 { grid-column: span 3; } .span-md-4 { grid-column: span 4;
} .span-md-5 { grid-column: span 5; } .span-md-6 { grid-column: span 6;
} .span-md-7 { grid-column: span 7; } .span-md-8 { grid-column: span 8;
} .span-md-9 { grid-column: span 9; } .span-md-10 { grid-column: span
10; } .span-md-11 { grid-column: span 11; } .span-md-12 { grid-column:
span 12; } } \@media (min-width: 992px) { .span-lg-1 { grid-column: span
1; } .span-lg-2 { grid-column: span 2; } .span-lg-3 { grid-column: span
3; } .span-lg-4 { grid-column: span 4; } .span-lg-5 { grid-column: span
5; } .span-lg-6 { grid-column: span 6; } .span-lg-7 { grid-column: span
7; } .span-lg-8 { grid-column: span 8; } .span-lg-9 { grid-column: span
9; } .span-lg-10 { grid-column: span 10; } .span-lg-11 { grid-column:
span 11; } .span-lg-12 { grid-column: span 12; } } \@media (min-width:
1025px) { .span-xl-1 { grid-column: span 1; } .span-xl-2 { grid-column:
span 2; } .span-xl-3 { grid-column: span 3; } .span-xl-4 { grid-column:
span 4; } .span-xl-5 { grid-column: span 5; } .span-xl-6 { grid-column:
span 6; } .span-xl-7 { grid-column: span 7; } .span-xl-8 { grid-column:
span 8; } .span-xl-9 { grid-column: span 9; } .span-xl-10 { grid-column:
span 10; } .span-xl-11 { grid-column: span 11; } .span-xl-12 {
grid-column: span 12; } } \@media (min-width: 1200px) { .span-2xl-1 {
grid-column: span 1; } .span-2xl-2 { grid-column: span 2; } .span-2xl-3
{ grid-column: span 3; } .span-2xl-4 { grid-column: span 4; }
.span-2xl-5 { grid-column: span 5; } .span-2xl-6 { grid-column: span 6;
} .span-2xl-7 { grid-column: span 7; } .span-2xl-8 { grid-column: span
8; } .span-2xl-9 { grid-column: span 9; } .span-2xl-10 { grid-column:
span 10; } .span-2xl-11 { grid-column: span 11; } .span-2xl-12 {
grid-column: span 12; } } \@media (min-width: 1440px) { .span-3xl-1 {
grid-column: span 1; } .span-3xl-2 { grid-column: span 2; } .span-3xl-3
{ grid-column: span 3; } .span-3xl-4 { grid-column: span 4; }
.span-3xl-5 { grid-column: span 5; } .span-3xl-6 { grid-column: span 6;
} .span-3xl-7 { grid-column: span 7; } .span-3xl-8 { grid-column: span
8; } .span-3xl-9 { grid-column: span 9; } .span-3xl-10 { grid-column:
span 10; } .span-3xl-11 { grid-column: span 11; } .span-3xl-12 {
grid-column: span 12; } } .flex { display: flex; flex-direction: column;
gap: var(\--rh-space-lg,16px)= ; } .flex-row { flex-direction: row; }
.flex-column { flex-direction: column; } \@media (min-width: 768px) {
.flex-md-row { flex-direction: row; } .flex-md-column { flex-direction:
column; } } .typography-h1 { font-size:
var(\--rh-font-size-heading-2xl,3rem); } .typography-h2 { font-size:
var(\--rh-font-size-heading-xl,2.5rem); } .typography-h3 { font-size:
var(\--rh-font-size-heading-lg,2.25rem); } .typography-h4 { font-size:
var(\--rh-font-size-heading-md,1.75rem); } .typography-h5 { font-size:
var(\--rh-font-size-heading-sm,1.5rem); } .typography-h6 { font-size:
var(\--rh-font-size-heading-xs,1.25rem); } .content section { padding:
0px; } .content h1, .content h2, .content h3, .content h4, .content h5,
.content h= 6 { margin: var(\--rh-space-lg,16px) 0; } .sr-only { height:
1px; margin: -1px; overflow: hidden; padding: 0px; posit= ion: absolute;
width: 1px; clip: rect(0px, 0px, 0px, 0px); border: 0px; }
.list-unstyled { list-style: none; padding-left: 0px; } .tooltip-content
{ align-items: center; display: flex; font-family: \"Red Ha= t Text\";
justify-content: center; text-transform: none; } .tooltip-content
.check-icon { margin-left: var(\--rh-space-md,8px); } .doc-image-link {
display: inline-block; text-decoration: none; } .modal-img { display:
block; width: 100%; } .modal-helper-text { margin-top: 0.5rem;
text-align: center; } .modal-helper-text a { color: rgb(0, 0, 0);
cursor: pointer; } .modal-helper-text a:hover { text-decoration:
underline; } .modal-helper-text a::after { content: \"=E2=BF=BB\";
margin-left: 0.25rem; } pf-modal.pf-img-modal {
\--pf-c-modal-box\--MaxHeight: 90vh; overflow-y: scro= ll; }
pf-modal.pf-img-modal::part(close-button) { background-color: rgb(255,
255,= 255); border-radius: 50%; color: rgb(0, 0, 0); margin-right:
-2rem; margin= -top: -2rem; }
pf-modal.pf-img-modal::part(close-button):hover { opacity: 0.7; }
rh-card { height: 100%; } h2.truste-title { line-height: normal;
margin-top: 0px; } rh-alert p\[slot=3D\"header\"\] { color: rgb(0, 41,
82); } section.rhdocs aside:target, section.rhdocs div:target,
section.rhdocs sect= ion:target { scroll-margin-top: 110px; } \@media
(max-width: 1439px) { html:has(div.content-wrapper) section.rhdocs
aside:target, html:has(div.c= ontent-wrapper) section.rhdocs div:target,
html:has(div.content-wrapper) se= ction.rhdocs section:target {
scroll-margin-top: 90px; } html:has(div.content-wrapper
rh-disclosure.tablet-jump-links-container) s= ection.rhdocs
aside:target, html:has(div.content-wrapper rh-disclosure.tabl=
et-jump-links-container) section.rhdocs div:target,
html:has(div.content-wr= apper
rh-disclosure.tablet-jump-links-container) section.rhdocs section:tar=
get { scroll-margin-top: 180px; } } \@media (max-width: 991px) {
html:has(nav.content-page-mobile-nav) section.rhdocs aside:target,
html:h= as(nav.content-page-mobile-nav) section.rhdocs div:target,
html:has(nav.con= tent-page-mobile-nav) section.rhdocs section:target {
scroll-margin-top: 60= px; }
html:has(nav.content-page-mobile-nav.hide-content-page-mobile-nav
rh-disc= losure.jump-links-container) section.rhdocs aside:target,
html:has(nav.cont= ent-page-mobile-nav.hide-content-page-mobile-nav
rh-disclosure.jump-links-c= ontainer) section.rhdocs div:target,
html:has(nav.content-page-mobile-nav.h= ide-content-page-mobile-nav
rh-disclosure.jump-links-container) section.rhd= ocs section:target {
scroll-margin-top: 20px; } html:has(nav.content-page-mobile-nav
rh-disclosure.jump-links-container) = section.rhdocs aside:target,
html:has(nav.content-page-mobile-nav rh-disclo=
sure.jump-links-container) section.rhdocs div:target,
html:has(nav.content-= page-mobile-nav
rh-disclosure.jump-links-container) section.rhdocs section:= target {
scroll-margin-top: 160px; } } .highlight { background: rgb(255, 244,
204); color: rgb(0, 0, 0); } \@media (max-width: 768px) { h1 {
font-size: 29px; line-height: 37.7px; } h2 { font-size: 24px;
line-height: 31.2px; } h3 { font-size: 20px; line-height: 26px; } h4, h5
{ font-size: 18px; line-height: 23.4px; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location: https://docs.redhat.com/\_nuxt/index.CMk9auDB.css
\@charset \"utf-8\"; .spinner-container\[data-v-7a282db7\] {
align-items: center; background-color= : rgba(0, 0, 0, 0.2); display:
flex; height: 100%; justify-content: center;= left: 0px; position:
fixed; top: 0px; width: 100%; z-index: 9999; } .item\[data-v-c61ac788\]
{ line-height: 22px; } #toc .link\[data-v-c61ac788\], #toc-mobile
.link\[data-v-c61ac788\] { color: li=
ght-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
} #toc .link\[data-v-c61ac788\], #toc-mobile .link\[data-v-c61ac788\],
.heading\[d= ata-v-c61ac788\], .sub-nav .link\[data-v-c61ac788\],
.sub-nav .link .link\[data= -v-c61ac788\] { display: block; padding-top:
; padding-bottom: ; padding-lef= t: ; padding-right: 2.5em;
text-decoration: none; transition: background-co= lor 0.25s; }
.heading\[data-v-c61ac788\]:hover, .link\[data-v-c61ac788\]:hover,
.sub-nav .li= nk\[data-v-c61ac788\]:hover { background:
light-dark(var(\--rh-color-surface-l=
ighter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow:
rgb(210,= 210, 210) 3px 0px inset; color:
light-dark(var(\--rh-color-gray-95,#151515)=
,var(\--rh-color-white,#fff)); } ol\[data-v-c61ac788\] { margin: 0px;
padding: 0px; } li\[data-v-c61ac788\], ol\[data-v-c61ac788\],
ul\[data-v-c61ac788\] { list-style:= none; margin: 0px; }
.chapter-title\[data-v-c61ac788\] { font-size: 1em; }
.sub-nav\[data-v-c61ac788\] { font-size: 1em; line-height: 24px;
list-style: = none; margin: 0px; padding-left: 16px; } .sub-nav
.link\[data-v-c61ac788\]:hover { color: rgb(21, 21, 21); }
.active\[data-v-c61ac788\] { background:
light-dark(var(\--rh-color-surface-li=
ghter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow: inset
3px= 0 0 0 var(\--rh-color-icon-primary-on-light,#e00); }
.sub-chapter-title\[data-v-c61ac788\], .sub-chapter-title
a\[data-v-c61ac788\] = { font-size: 0.875rem; }
summary\[data-v-c61ac788\] { cursor: pointer; list-style: none;
position: rel= ative; }
summary\[data-v-c61ac788\]::-webkit-details-marker { display: none; }
html\[data-v-c61ac788\] { \--details-transition-time: .4s; }
.chapter-landing-page\[data-v-c61ac788\] { font-weight: 500; }
details\[open\]:first-of-type \> .heading\[data-v-c61ac788\]::after {
transform:= rotate(135deg); } details\[data-v-c61ac788\] { max-height:
var(\--details-height-closed,auto); t= ransition: all ease-out
var(\--details-transition-time,0); } details\[open\]\[data-v-c61ac788\]
{ max-height: var(\--details-height-open,auto= ); } details
.heading.sub-chapter-title\[data-v-c61ac788\]::after, details .headin=
g\[data-v-c61ac788\]::after { border-right: 3px solid
light-dark(var(\--rh-col=
or-gray-95,#151515),var(\--rh-color-white,#fff)); border-top: 3px solid
ligh=
t-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
color: = rgb(21, 21, 21); content: \"\"; display: flex; float: right;
height: 9px; mar= gin-left: 16px; position: absolute; right:
var(\--rh-space-xl,24px); top: 14= px; transform: rotate(45deg); width:
9px; } details .heading.sub-chapter-title\[data-v-c61ac788\]::after {
height: 8px; w= idth: 8px; } ol\[data-v-2b26994c\] { margin: 0px;
padding: 0px; } li\[data-v-2b26994c\], ol\[data-v-2b26994c\],
ul\[data-v-2b26994c\] { list-style:= none; margin: 0px; }
.chapter-title\[data-v-2b26994c\] { font-size: 1em; }
.sub-chapter-title\[data-v-2b26994c\], .sub-chapter-title
a\[data-v-2b26994c\] = { font-size: 0.875rem; } #toc
.link\[data-v-2b26994c\], #toc-mobile .link\[data-v-2b26994c\],
.heading\[d= ata-v-2b26994c\], .sub-nav .link\[data-v-2b26994c\],
.sub-nav .link .link\[data= -v-2b26994c\] { display: block; padding-top:
; padding-bottom: ; padding-lef= t: ; padding-right: 2.5em;
text-decoration: none; transition: background-co= lor 0.25s; }
.heading\[data-v-2b26994c\]:hover, .link\[data-v-2b26994c\]:hover,
.sub-nav .li= nk\[data-v-2b26994c\]:hover { background:
light-dark(var(\--rh-color-surface-l=
ighter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow:
rgb(210,= 210, 210) 3px 0px inset; color:
light-dark(var(\--rh-color-gray-95,#151515)=
,var(\--rh-color-white,#fff)); } details\[open\]:first-of-type \>
.heading\[data-v-2b26994c\]::after { transform:= rotate(135deg); }
.item\[data-v-2b26994c\] { line-height: 22px; } #toc
.link\[data-v-2b26994c\], #toc-mobile .link\[data-v-2b26994c\] { color:
li=
ght-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
} .sub-nav\[data-v-2b26994c\], .toc-wrapper\[data-v-2b26994c\] {
list-style: none= ; margin: 0px; } .toc-wrapper\[data-v-2b26994c\] {
min-width: 100%; padding: 0px; } .sub-nav\[data-v-2b26994c\] {
font-size: 1em; line-height: 24px; padding-left= : 16px; } .sub-nav
.link\[data-v-2b26994c\]:hover { color: rgb(21, 21, 21); }
.active\[data-v-2b26994c\] { background:
light-dark(var(\--rh-color-surface-li=
ghter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow: inset
3px= 0 0 0 var(\--rh-color-icon-primary-on-light,#e00); }
.chapter-landing-page\[data-v-2b26994c\] { font-weight: 500; }
summary\[data-v-2b26994c\] { cursor: pointer; list-style: none;
position: rel= ative; }
summary\[data-v-2b26994c\]::-webkit-details-marker { display: none; }
\@keyframes slideDown-2b26994c {=20 0% { height: 0px; opacity: 0; } 100%
{ height: var(\--details-height-open,\"100%\"); opacity: 1; } }
html\[data-v-2b26994c\] { \--details-transition-time: .4s; }
details\[data-v-2b26994c\] { max-height:
var(\--details-height-closed,auto); t= ransition: all ease-out
var(\--details-transition-time,0); } details\[open\]\[data-v-2b26994c\]
{ max-height: var(\--details-height-open,auto= ); } details
.heading.sub-chapter-title\[data-v-2b26994c\]::after, details .headin=
g\[data-v-2b26994c\]::after { border-right: 3px solid
light-dark(var(\--rh-col=
or-gray-95,#151515),var(\--rh-color-white,#fff)); border-top: 3px solid
ligh=
t-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
color: =
light-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
con= tent: \"\"; display: flex; float: right; height: 9px; margin-left:
16px; posi= tion: absolute; right: var(\--rh-space-xl,24px); top: 14px;
transform: rotat= e(45deg); width: 9px; } details
.heading.sub-chapter-title\[data-v-2b26994c\]::after { height: 8px; w=
idth: 8px; } label\[for=3D\"page-format\"\]\[data-v-5cade871\] {
font-weight: 500; } .page-format-dropdown\[data-v-5cade871\] {
appearance: none; background-attac= hment: ; background-origin: ;
background-clip: ; background-color: ; backgr= ound-image:
var(\--select-dropdown-image); background-position: 97% center; =
background-repeat: no-repeat; background-size: auto; border: 1px solid
ligh=
t-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border=
-subtle-on-dark,#707070)); box-shadow: rgb(77, 77, 77) 0px -1px inset;
font= -family: \"Red Hat Text\"; font-size:
var(\--rh-font-size-body-text-md,1rem); = margin-top:
var(\--rh-space-xs,4px); max-width: 100%; min-height: 36px; over= flow:
hidden; padding: 0 var(\--rh-space-xl,24px) 0 var(\--rh-space-md,8px); =
text-overflow: ellipsis; white-space: nowrap; } \@media (max-width:
992px) { label\[for=3D\"page-format\"\]\[data-v-5cade871\] { display:
block; } } \@media (min-width: 1440px) {
.page-format-dropdown\[data-v-5cade871\] { background-position: 90%
center;= } } rh-cta\[variant=3D\"brick\"\]\[data-v-ca9eac59\]:hover {
text-decoration: underli= ne solid
light-dark(var(\--rh-color-interactive-primary-hover-on-light,#036)=
,var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc)); }
\[variant=3D\"brick\"\]\[data-v-ca9eac59\] { max-width: 150px; }
.pagination\[data-v-ca9eac59\] { display: flex; justify-content:
space-betwee= n; margin-bottom: var(\--rh-space-6xl,96px); margin-top:
var(\--rh-space-4xl,= 4rem); } .previous-btn\[data-v-ca9eac59\] {
margin-right: auto; } .next-btn\[data-v-ca9eac59\] { margin-left: auto;
} .next-btn\[data-v-ca9eac59\]:hover,
.previous-btn\[data-v-ca9eac59\]:hover { cu= rsor: pointer; }
.next-btn.disabled\[data-v-ca9eac59\],
.previous-btn.disabled\[data-v-ca9eac59= \] { background-color:
var(\--rh-color-bg-disabled,#f2f2f2); cursor: not-allo= wed;
pointer-events: none; } rh-code-block dd { margin: 0px; }
:host(\[size=3D\"sm\"\]) #container\[data-v-c6b48c1e\] { \--\_size:
var(\--pf-global= \--icon\--FontSize\--sm,12px); }
.content-wrapper\[data-v-c6b48c1e\] { background-color:
light-dark(var(\--rh-c=
olor-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
gap: 0= px; grid-template-columns: repeat(12, 1fr); height: auto;
margin: 0px auto;= min-height: 46vh; } .content\[data-v-c6b48c1e\] {
margin: 0 var(\--rh-space-lg,16px); } .line-below-chp\[data-v-c6b48c1e\]
{ border-right: 0px; border-bottom: 0px; b= order-left: 0px;
border-image: initial; border-top: .0625rem solid light-da=
rk(#d2d2d2,var(\--rh-color-border-subtle-on-dark,#707070)); margin:
var(\--rh= -space-xl,24px) 0 var(\--rh-space-3xl,48px); }
.docs-content-container\[data-v-c6b48c1e\] { font-size:
var(\--rh-font-size-bo= dy-text-lg,1.125rem); font-weight:
var(\--rh-font-weight-body-text-regular,4= 00); line-height: 1.6667;
padding-top: var(\--rh-space-xl,24px); }
.chapter-title\[data-v-c6b48c1e\] { font-family: \"Red Hat Display\"; }
h1.chapter-title\[data-v-c6b48c1e\] { margin: 0px; padding: 0px; }
.banner-wrapper\[data-v-c6b48c1e\] { padding: 0
var(\--rh-space-lg,16px); } .chapter .section
.simpara\[data-v-c6b48c1e\], .chapter .section p\[data-v-c6b= 48c1e\] {
font-family: \"Red Hat Text\"; font-size: var(\--rh-font-size-body-te=
xt-lg,1.125rem); font-weight:
var(\--rh-font-weight-body-text-regular,400); = line-height: 30px; }
.alert-section\[data-v-c6b48c1e\] { padding-bottom:
var(\--rh-space-2xl,32px);= } rh-alert\[data-v-c6b48c1e\] { width: auto;
} rh-back-to-top\[data-v-c6b48c1e\] { inset-block-end:
var(\--rh-space-lg,16px);= inset-inline-end: var(\--rh-space-lg,16px); }
.informaltable\[data-v-c6b48c1e\], .rhdocs
.informaltable\[data-v-c6b48c1e\], .= rhdocs
.table-contents\[data-v-c6b48c1e\], .rhdocs .table-wrapper\[data-v-c6b4=
8c1e\], .table-contents\[data-v-c6b48c1e\],
.table-wrapper\[data-v-c6b48c1e\] { = max-height:
var(\--rh-table\--maxHeight); overflow: auto; }
rh-table\[data-v-c6b48c1e\] { display: block; margin:
var(\--rh-space-2xl,32px= ) 0; max-width: 100%; }
.pvof-doc\_\_wrapper\[data-v-c6b48c1e\], .rhdocs\[data-v-c6b48c1e\] {
\--rh-table-= -maxHeight: calc(100vh - 12.5rem); }
.toc-filter\[data-v-c6b48c1e\] { display: none; }
.toc-filter-mobile\[data-v-c6b48c1e\] { padding:
var(\--rh-space-lg,16px); wid= th: 100%; } #text\[data-v-c6b48c1e\],
.toc-filter-mobile\[data-v-c6b48c1e\] { align-items: = center; display:
flex; } #text\[data-v-c6b48c1e\] { flex: 1 1 0%; flex-direction: row; }
#search-icon\[data-v-c6b48c1e\] { left: 2.5rem; position: absolute; top:
55%;= transform: translateY(-50%); z-index: 1; }
rh-icon\[data-v-c6b48c1e\] { \--rh-icon\--size: 16px; }
#text:focus-within #icon\[data-v-c6b48c1e\], #text:hover
#icon\[data-v-c6b48c1= e\] { color: rgb(21, 21, 21); }
#text\[data-v-c6b48c1e\]::after, #text\[data-v-c6b48c1e\]::before {
content: \"\"= ; inset: 0px; pointer-events: none; position: absolute; }
#text-input\[data-v-c6b48c1e\]:focus, #text-input:focus +
#utilities\[data-v-c= 6b48c1e\] { border-bottom: 2px solid rgb(0, 102,
204); outline: none; } #text-input\[data-v-c6b48c1e\] {
background-color: light-dark(var(\--rh-color-=
surface-lightest,#fff),var(\--rh-color-surface-darkest,#151515));
border-top= -color: ; border-top-style: ; border-top-width: ;
border-right-color: ; bor= der-right-style: ; border-right-width: ;
border-left-color: ; border-left-s= tyle: ; border-left-width: ;
border-image-source: ; border-image-slice: ; b= order-image-width: ;
border-image-outset: ; border-image-repeat: ; border-b= ottom: 1px solid
rgb(138, 141, 144); font-family: inherit; font-size: 100%;= grid-area:
text-input; line-height: 1.5; overflow: hidden; padding: 0.375r= em
0.25rem 0.375rem 0.5rem; position: relative; text-overflow: ellipsis;
wh= ite-space: nowrap; width: 100%; }
#text-input\[data-v-c6b48c1e\]::placeholder { color:
light-dark(#6a6e73,var(-= -rh-color-gray-30,#c7c7c7)); }
#utilities\[data-v-c6b48c1e\] { align-items: center; background-color:
light-=
dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darkest,#=
151515)); border-top-color: ; border-top-style: ; border-top-width: ;
borde= r-right-color: ; border-right-style: ; border-right-width: ;
border-image-s= ource: ; border-image-slice: ; border-image-width: ;
border-image-outset: ;= border-image-repeat: ; border-bottom: 1px solid
rgb(138, 141, 144); border= -left: 0px; display: flex; padding-bottom:
3px; padding-top: 3px; } #utilities rh-badge\[data-v-c6b48c1e\] {
border-radius: 80px; font-weight: va=
r(\--rh-font-weight-heading-medium,500); \--\_background-color: #e0e0e0;
} #clear-button\[data-v-c6b48c1e\], #utilities
rh-badge\[data-v-c6b48c1e\] { marg= in-right: var(\--rh-space-md,8px); }
#clear-button\[data-v-c6b48c1e\] { \--pf-c-button\--PaddingTop: .625rem;
\--pf-c= -button\--PaddingRight: .25rem; \--pf-c-button\--PaddingBottom:
.625rem; \--pf-= c-button\--PaddingLeft: .25rem; }
#text-input.no-right-border\[data-v-c6b48c1e\] { border-right: 0px; }
.focusable\[data-v-c6b48c1e\]:focus-visible { border: 2px solid
var(\--rh-colo= r-interactive-blue,#06c); }
.mobile-nav-wrapper\[data-v-c6b48c1e\] { align-items: center;
border-bottom: = 1px solid
light-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--r=
h-color-border-subtle-on-dark,#707070)); display: flex; height: auto;
justi= fy-content: space-between; padding: var(\--rh-space-sm,.5rem); }
.content-page-mobile-nav\[data-v-c6b48c1e\] { align-items: center;
background= -color:
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-sur=
face-darker,#1f1f1f)); min-height: 51px; position: sticky; top: 0px;
z-inde= x: 5; } .active-mobile-menu\[data-v-c6b48c1e\] { color:
light-dark(var(\--rh-color-gra=
y-95,#151515),var(\--rh-color-interactive-secondary-default-on-dark,#c7c7c7)=
); padding-left: 0.5rem; } .hidden\[data-v-c6b48c1e\] { display: none; }
.mobile-nav-btn\[data-v-c6b48c1e\] { background-color: transparent;
border: n= one; font-family: inherit; font-size: 0.875rem; font-weight:
500; margin: 0= px; min-height: 40px; min-width: 40px; }
.border-right\[data-v-c6b48c1e\] { border-right: 1px solid rgb(199, 199,
199)= ; } .product-container\[data-v-c6b48c1e\] { border-bottom: 1px
solid light-dark(v=
ar(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-=
on-dark,#707070)); padding: var(\--rh-space-2xl,32px)
var(\--rh-space-lg,16px= ); } .product-container
h1.product-title\[data-v-c6b48c1e\] { font-size: var(\--rh-=
font-size-code-xl,1.25rem); line-height: 30px; margin-bottom: 0px;
margin-t= op: 0px; } .product-container
.product-version\[data-v-c6b48c1e\] { align-items: center;= display:
flex; flex-wrap: wrap; margin-top: var(\--rh-space-lg,16px); }
.product-version .version-label\[data-v-c6b48c1e\] { font-family: \"Red
Hat Te= xt\"; font-size: var(\--rh-font-size-body-text-sm,.875rem);
font-weight: 500;= } .product-version
.version-select-dropdown\[data-v-c6b48c1e\] { margin: 0 var(=
\--rh-space-lg,16px); max-width: 9.75rem; min-height: 2rem; min-width:
3rem;= overflow: hidden; width: min-content; appearance: none;
background-size: ;= background-attachment: ; background-origin: ;
background-clip: ; backgroun= d-color: ; background-image:
var(\--select-dropdown-image); background-posit= ion: 85% 50%;
background-repeat: no-repeat; border-top-color: ; border-top-= style: ;
border-top-width: ; border-right-color: ; border-right-style: ; bo=
rder-right-width: ; border-left-color: ; border-left-style: ;
border-left-w= idth: ; border-image-source: ; border-image-slice: ;
border-image-width: ; = border-image-outset: ; border-image-repeat: ;
border-bottom: 0px; box-shado= w: 0 -1px 0 0
var(\--rh-color-gray-60,#4d4d4d) inset; cursor: pointer; font-= size:
var(\--rh-font-size-body-text-md,1rem); padding-top: ; padding-bottom:=
; padding-left: ; padding-right: var(\--rh-space-xl,24px);
text-overflow: e= llipsis; } pf-popover\[data-v-c6b48c1e\] { margin-top:
var(\--rh-space-md,8px); \--pf-c-po= pover\_\_arrow\--BackgroundColor:
var(\--rh-color-canvas-black,#151515); \--pf-c=
-popover\_\_content\--BackgroundColor: var(
\--rh-color-canvas-black,#151515 );= \--pf-c-popover\--BoxShadow: 0px
4px 8px 0px #15151540; \--pf-c-popover\_\_titl= e-text\--Color:
var(\--rh-color-white,#fff); \--pf-c-popover\--MaxWidth: 300px;=
\--pf-c-popover\--MinWidth: 300px; \--pf-c-popover\--c-button\--Top:
20px; \--pf= -c-popover\--c-button\--Right: 4px;
\--pf-c-button\--m-plain\--hover\--Color: var= (\--rh-color-white,#fff);
} pf-popover\[data-v-c6b48c1e\]::part(content) { padding:
var(\--rh-space-2xl,32= px); } pf-popover\[data-v-c6b48c1e\]::part(body)
{ margin-top: var(\--rh-space-lg,16p= x); }
pf-popover\[data-v-c6b48c1e\]::part(close-button) {
\--pf-c-button\--m-plain\--f= ocus\--Color:
var(\--rh-color-gray-30,#c7c7c7); \--pf-c-button\--m-plain\--Color= :
var(\--rh-color-gray-30,#c7c7c7); }
.popover-header-text\[data-v-c6b48c1e\] { color:
var(\--rh-color-white,#fff); = font-size:
var(\--rh-font-size-code-md,1rem); margin: 0px; max-width: 80%; p=
adding: 0px; } .popover-body-link\[data-v-c6b48c1e\] { color:
var(\--rh-color-blue-30,#92c5f9= ); text-decoration: none; }
.popover-trigger-btn\[data-v-c6b48c1e\] { align-items: center;
background: no= ne; border: none; cursor: pointer; display: flex;
justify-content: center; = } #first-button\[data-v-c6b48c1e\] { width:
80%; } #second-button\[data-v-c6b48c1e\] { text-align: right; width:
20%; } #toc-btn\[data-v-c6b48c1e\] { text-align: left; width: 100%; }
.toc-error\[data-v-c6b48c1e\] { margin: 0px; max-width: 100%; } #layout
label\[data-v-c6b48c1e\] { font-weight: 500; }
.page-layout-options\[data-v-c6b48c1e\] { display: flex; flex-direction:
colu= mn; max-width: 100%; padding-bottom: var(\--rh-space-lg,16px); }
.table-of-contents \> ol\[data-v-c6b48c1e\] { list-style: none; margin:
0px; p= adding: 0px; } nav.table-of-contents\[data-v-c6b48c1e\] {
z-index: 1; } nav.table-of-contents ol\[data-v-c6b48c1e\] { list-style:
none; margin: 0px; = padding: 0px; }
#mobile-browse-docs\[data-v-c6b48c1e\] { font-weight:
var(\--rh-font-weight-bo= dy-text-medium,500); padding-left:
var(\--rh-space-2xl,32px); }
#mobile-nav-content-wrapper\[data-v-c6b48c1e\] { border-bottom: 1px
solid lig=
ht-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-borde=
r-subtle-on-dark,#707070)); border-top: 1px solid
light-dark(var(\--rh-color=
-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-on-dark,#7070=
70)); } #page-content-options-mobile\[data-v-c6b48c1e\],
#toc-wrapper-mobile\[data-v-c= 6b48c1e\] { padding:
var(\--rh-space-md,8px); } nav#mobile-toc-menu\[data-v-c6b48c1e\] {
max-height: 50vh; overflow-y: scroll= ; }
rh-disclosure.jump-links-container\[data-v-c6b48c1e\] { margin:
var(\--rh-spac= e-xl,24px) var(\--rh-space-lg,16px) 0; }
.content-page-mobile-nav\[data-v-c6b48c1e\] { display: block;
transition: tra= nsform 0.3s ease-in-out; }
.hide-content-page-mobile-nav\[data-v-c6b48c1e\] { transform:
translateY(-100= %); transition: transform 0.3s ease-in-out; }
#breadcrumbs\[data-v-c6b48c1e\],
.content-format-selectors\[data-v-c6b48c1e\], =
.left-content\[data-v-c6b48c1e\], .tablet-jump-links\[data-v-c6b48c1e\],
.table= t-page-layout-options\[data-v-c6b48c1e\] { display: none; }
\@media (min-width: 768px) { .content\[data-v-c6b48c1e\] { margin: 0
var(\--rh-space-2xl,32px); }
rh-disclosure.jump-links-container\[data-v-c6b48c1e\] { margin:
var(\--rh-sp= ace-xl,24px) var(\--rh-space-2xl,32px) 0; } } \@media
(min-width: 992px) { #mobile-nav\[data-v-c6b48c1e\],
#toc-list-mobile\[data-v-c6b48c1e\] { display= : none; }
#breadcrumbs\[data-v-c6b48c1e\] { display: block; }
.content-wrapper\[data-v-c6b48c1e\] { grid-template-columns: repeat(2,
auto= ) repeat(10, 1fr); } .left-content\[data-v-c6b48c1e\] { display:
block; max-width: 320px; min-wi= dth: 320px; z-index: 6; }
.toc-container\[data-v-c6b48c1e\] { border-right: 1px solid
light-dark(var(=
\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-on-=
dark,#707070)); min-height: 100vh; position: sticky; top: 72px;
transition:= transform 0.3s ease-in-out; }
.toc-wrapper\[data-v-c6b48c1e\] { padding: 0px; }
.toc-focus-container\[data-v-c6b48c1e\] { position: sticky; top: 72px;
z-in= dex: 2; } .toc-focus-btn\[data-v-c6b48c1e\] { align-items: center;
background-color: =
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-dar=
ker,#1f1f1f)); border: 1px solid
light-dark(var(\--rh-color-border-interacti=
ve-on-light,#06c),var(\--rh-color-border-interactive-on-dark,#92c5f9));
bord= er-radius: 50%; cursor: pointer; display: flex; height: 40px;
justify-conte= nt: center; position: absolute; right: -20px; top: 15px;
width: 40px; } .toc-focus-btn\[data-v-c6b48c1e\]:focus-visible,
.toc-focus-btn\[data-v-c6b4= 8c1e\]:hover { background-color:
light-dark(var(\--rh-color-blue-10,#e0f0ff),=
var(\--rh-color-gray-70,#383838)); box-shadow: var(\--rh-box-shadow-sm,0
2px = 4px 0 hsla(0,0%,8%,.2)); }
.toc-focus-btn\[data-v-c6b48c1e\]:focus-visible { border: 2px solid
var(\--r= h-color-blue-50,#06c); }
.toc-focus-btn-icon\[data-v-c6b48c1e\] { color:
light-dark(var(\--rh-color-b=
lue-50,#06c),var(\--rh-color-blue-50,#92c5f9)); }
nav#toc\[data-v-c6b48c1e\] { height: auto; max-height:
var(\--toc-height,70v= h); overflow-y: auto; padding-bottom:
var(\--rh-space-2xl,32px); } .toc-filter\[data-v-c6b48c1e\] {
align-items: center; background-color: lig=
ht-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker=
,#1f1f1f)); display: flex; padding: var(\--rh-space-lg,16px)
var(\--rh-space-= 2xl,32px); position: sticky; top: 72px; width: 100%;
z-index: 1; } .product-container\[data-v-c6b48c1e\] { padding:
var(\--rh-space-xl,24px) va= r(\--rh-space-2xl,32px); }
.product-container.shrink-product-padding\[data-v-c6b48c1e\] { padding:
var= (\--rh-space-lg,16px); } .product-version
.version-select-dropdown\[data-v-c6b48c1e\] { margin: var(=
\--rh-space-md,8px) var(\--rh-space-sm,6px); }
.toc-filter\[data-v-c6b48c1e\] { display: block; }
#text-input\[data-v-c6b48c1e\] { padding: 0.375rem 0.25rem 0.375rem
2rem; } .page-layout-options\[data-v-c6b48c1e\] { max-width: 168px; }
.docs-content-container\[data-v-c6b48c1e\] { padding-top:
var(\--rh-space-3x= l,4rem); } .content\[data-v-c6b48c1e\] { margin: 0
var(\--rh-space-2xl,32px) 0 var(\--rh= -space-4xl,64px); max-width:
789px; } .expand-content\[data-v-c6b48c1e\] { max-width: 900px; }
.banner-wrapper\[data-v-c6b48c1e\] { padding: var(\--rh-space-3xl,48px)
var(= \--rh-space-6xl,96px) 0 var(\--rh-space-6xl,96px); }
.change-layout\[data-v-c6b48c1e\] { grid-template-columns: auto
repeat(11, = 1fr); } .collapse-left-content\[data-v-c6b48c1e\] {
max-width: 48px; min-width: 48p= x; }
.tablet-page-layout-options\[data-v-c6b48c1e\] { display: flex;
flex-direct= ion: column; max-width: 100%; padding-top:
var(\--rh-space-2xl,32px); } .tablet-jump-links\[data-v-c6b48c1e\] {
background-color: light-dark(var(\--=
rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
di= splay: flex; flex-direction: column; justify-content: flex-end;
position: s= ticky; top: 72px; z-index: 5; }
rh-disclosure.tablet-jump-links-container\[data-v-c6b48c1e\] {
margin-top: = var(\--rh-space-xl,24px); }
rh-back-to-top\[data-v-c6b48c1e\] { inset-inline-end:
var(\--rh-space-2xl,32= px); } \@keyframes slideaway-left-c6b48c1e {=20
0% { display: block; } 100% { opacity: 0; transform: translate(-40px); }
} \@keyframes slideaway-right-c6b48c1e {=20 0% { display: block; } 100%
{ opacity: 0; transform: translate(40px); } } \@keyframes
enter-left-c6b48c1e {=20 0% { display: none; transform:
translate(-40px); } 100% { opacity: 1; } } \@keyframes
enter-right-c6b48c1e {=20 0% { display: none; transform:
translate(40px); } 100% { opacity: 1; } } .hide-left\[data-v-c6b48c1e\]
{ animation: 0.2s ease 0s 1 normal none runni= ng
slideaway-left-c6b48c1e; display: none; } .enter-left\[data-v-c6b48c1e\]
{ animation: 0.3s ease 0s 1 normal none runn= ing enter-left-c6b48c1e;
border-right: none; display: block; } .enter-right\[data-v-c6b48c1e\] {
animation: 0.3s ease 0s 1 normal none run= ning enter-right-c6b48c1e;
display: block; } .hide-right\[data-v-c6b48c1e\] { animation: 0.2s ease
0s 1 normal none runn= ing slideaway-right-c6b48c1e; display: none; }
.toc-container.enter-toc-container-left\[data-v-c6b48c1e\] { transform:
tra= nslate(0px); } } \@media (min-width: 1100px) {
.expand-content\[data-v-c6b48c1e\] { margin: 0px auto; } } \@media
(min-width: 1200px) { .content\[data-v-c6b48c1e\] { margin: 0px auto; }
} \@media (min-width: 1440px) { .tablet-jump-links\[data-v-c6b48c1e\],
.tablet-page-layout-options\[data-v-c= 6b48c1e\] { display: none; }
.content-wrapper\[data-v-c6b48c1e\] { grid-template-columns: repeat(2,
auto= ) repeat(8, 1fr) repeat(2, auto); } .content\[data-v-c6b48c1e\] {
margin: 0 var(\--rh-space-4xl,64px); }
.expand-content\[data-v-c6b48c1e\] { margin: 0px auto; }
.change-layout\[data-v-c6b48c1e\] { grid-template-columns: auto
repeat(9, 1= fr) repeat(2, auto); }
.content-format-selectors\[data-v-c6b48c1e\] { color:
light-dark(var(\--rh-c=
olor-gray-95,#151515),var(\--rh-color-white,#fff)); display: block;
font-fam= ily: \"Red Hat Text\"; font-size:
var(\--rh-font-size-body-text-sm,.875rem); f= ont-weight:
var(\--rh-font-weight-body-text-medium,500); margin-right: var(-=
-rh-space-2xl,32px); max-width: 320px; min-width: 320px; padding-top:
var(-= -rh-space-2xl,32px); } summary\[data-v-c6b48c1e\] { cursor:
pointer; list-style: none; position: r= elative; }
summary\[data-v-c6b48c1e\]::-webkit-details-marker { display: none; }
details#jump-links-details .jump-links-heading\[data-v-c6b48c1e\] {
backgro= und-color:
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-=
surface-darker,#1f1f1f)); display: block; margin-top:
var(\--rh-space-lg,16p= x); padding: var(\--rh-space-lg,16px) 0 0
var(\--rh-space-xl,24px); position:= sticky; top: 72px; }
details#jump-links-details
.jump-links-heading\[data-v-c6b48c1e\]::before {= border-right: 3px
solid light-dark(var(\--rh-color-border-strong-on-light,#=
151515),var(\--rh-color-border-strong-on-dark,#fff)); border-top: 3px
solid =
light-dark(var(\--rh-color-border-strong-on-light,#151515),var(\--rh-color-bo=
rder-strong-on-dark,#fff)); color: var(\--rh-color-gray-95,#151515);
content= : \"\"; display: flex; height: 9px; left: 2px; position:
absolute; top: 26px;= transform: rotate(-135deg); width: 9px; }
details#jump-links-details\[open\]
.jump-links-heading\[data-v-c6b48c1e\]::be= fore { transform:
rotate(135deg); } .page-layout-sticky\[data-v-c6b48c1e\] { position:
sticky; top: 77px; } } \@media (min-width: 1600px) {
.content\[data-v-c6b48c1e\] { margin: 0px auto; } } \@media (min-width:
1920px) { .content-format-selectors\[data-v-c6b48c1e\] { margin-right:
var(\--rh-space= -4xl,64px); } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location: https://docs.redhat.com/\_nuxt/Alert.DqSuUj60.css
\@charset \"utf-8\"; .html-container\[data-v-b8fb6e74\] { padding: 2rem
1.5rem 0px; } rh-alert\[data-v-b8fb6e74\] { color: rgb(21, 21, 21); }
\@media (max-width: 772px) { .html-container\[data-v-b8fb6e74\] {
padding: 3rem 1rem 0px; } } rh-alert\[slot=3D\"header\"\]
h3\[data-v-ea3021fb\] { color: rgb(121, 86, 0); fon= t-family: \"Red Hat
Text\"; font-size: 14px; font-weight: 500; line-height: 2= 1px;
text-align: left; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location: https://docs.redhat.com/\_nuxt/JumpLinks.BohlAhoi.css
\@charset \"utf-8\"; .jump-links\[data-v-ebbf8b23\] { max-height: 50vh;
overflow-y: auto; } .jump-links ul\[data-v-ebbf8b23\] { align-items:
flex-start; border-left: 1px= solid
var(\--rh-color-border-subtle-on-light,#c7c7c7); display: flex; flex-=
direction: column; list-style: none; padding: 0px; }
.jump-link-item\[data-v-ebbf8b23\] { border-left: 3px solid transparent;
curs= or: pointer; } .jump-link-item\[data-v-ebbf8b23\]:hover {
border-left-color: light-dark(var(=
\--rh-color-interactive-secondary-hover-on-light,#4d4d4d),var(\--rh-color-int=
eractive-secondary-hover-on-dark,#c7c7c7)); } .jump-link-item
a\[data-v-ebbf8b23\] { color: light-dark(var(\--rh-color-gray-=
60,#4d4d4d),var(\--rh-color-white,#c7c7c7)); display: block;
font-family: \"R= ed Hat Text\"; font-weight: 400; line-height: 21px;
padding: var(\--rh-space-= md,8px) var(\--rh-space-lg,16px); }
.active_link\[data-v-ebbf8b23\] { border-left: 3px solid var(
\--rh-color-bran=
d-red,light-dark(var(\--rh-color-brand-red-on-light,#e00),var(\--rh-color-bra=
nd-red-on-dark,#e00)) ); } .active_link a\[data-v-ebbf8b23\],
.jump-link-item a\[data-v-ebbf8b23\]:focus-v= isible, .jump-link-item
a\[data-v-ebbf8b23\]:hover { color: light-dark(var(\--=
rh-color-gray-95,#151515),var(\--rh-color-white,#fff)); } \@media
(min-width: 992px) { .jump-links\[data-v-ebbf8b23\] { margin-top:
var(\--rh-space-lg,16px); max-h= eight: 80vh; } } \@media (min-width:
992px) and (max-width: 1439px) {
nav#contentPage-tablet-jumpLinks\[data-v-ebbf8b23\] { margin-top: 0px;
max-= height: 40vh; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
https://docs.redhat.com/\_nuxt/Breadcrumbs.Dc7QxJYj.css \@charset
\"utf-8\"; rh-breadcrumb { \--\_breadcrumb-caret-image-default:
var(\--rh-breadcrumb-care=
t-image,url(\"data:image/svg+xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www.= w3.org/2000/svg\' width=3D\'10\' height=3D\'15\'
fill=3D\'none\' viewBox=3D\'0 0 10= 15\'%3E%3Cg
clip-path=3D\'url(%23a)\'%3E%3Cpath fill=3D\'red\' d=3D\'m2.5 14.5-2= -2
5-5-5-5 2-2 7 7z\'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id=3D\'a\'%3E%3Cpath
fi= ll=3D\'%23fff\' d=3D\'M10
.5H0v14h10z\'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E= \"));
\--\_breadcrumb-link-color:
var(\--rh-breadcrumb-link-color,var(\--rh-colo=
r-interactive-primary-default));
\--\_breadcrumb-link-color-current-page: var=
(\--rh-color-text-primary);
\--\_breadcrumb-link-color-current-page-subtle: va=
r(\--rh-color-text-secondary); \--\_breadcrumb-link-color-hover:
var(\--rh-colo= r-interactive-primary-hover);
\--\_breadcrumb-link-color-visited: var(\--rh-co=
lor-interactive-primary-visited-hover);
\--\_breadcrumb-link-color-visited-ho= ver:
var(\--rh-color-interactive-primary-visited-hover);
\--\_breadcrumb-link-= focus-outline-color:
var(\--rh-color-border-interactive); display: block; } rh-breadcrumb ol
{ container: breadcrumbs-list / inline-size; font-size: va=
r(\--rh-font-size-body-text-sm,.875rem); line-height:
var(\--rh-line-height-b= ody-text,1.5); margin-block: 0px;
padding-inline-start: 0px; } rh-breadcrumb \> ol \> li { align-items:
center; display: inline-flex; gap: v= ar(\--rh-space-lg,16px);
margin-block-end: var(\--rh-space-md,8px); padding-i= nline-end:
var(\--rh-breadcrumb-li-padding-inline-end,var(\--rh-space-lg,16px= ));
vertical-align: bottom; } rh-breadcrumb \> ol \>
li:not(:first-of-type)::before { background-color: var=
(\--rh-color-icon-secondary); content: \"\"; display: inline-block;
height: va= r(\--rh-font-size-body-text-sm,.875rem); mask-image:
var(\--\_breadcrumb-caret= -image-default); mask-position: center
center; mask-repeat: no-repeat; widt= h:
var(\--rh-font-size-body-text-sm,.875rem); }
rh-breadcrumb\[variant=3D\"subtle\"\] \> ol \>
li:not(:first-of-type)::before { b= ackground-color:
var(\--rh-color-icon-subtle,#707070); } rh-breadcrumb \> ol \>
li:first-child { padding-inline-start: 0px; } rh-breadcrumb \> ol \>
li:last-child { background-image: none; } rh-breadcrumb \> ol \> li,
rh-breadcrumb \> ol \> li \> a { color: var(\--\_breadc=
rumb-link-color); } rh-breadcrumb \> ol \> li \> a { text-decoration:
underline; } rh-breadcrumb \> ol \> li \> a:is(:hover, :focus, :active)
{ color: var(\--\_bre= adcrumb-link-color-hover); } rh-breadcrumb \> ol
\> li \> a:is(:focus, :focus-visible) { border-radius: var=
(\--rh-border-radius-default,3px); outline: 2px solid
var(\--\_breadcrumb-link= -focus-outline-color); } rh-breadcrumb \> ol
\> li:first-child \> a { margin-inline-start: 0px; } rh-breadcrumb \> ol
\> li:last-child, rh-breadcrumb \> ol \> li \> a\[aria-curren=
t=3D\"page\"\] { color: var(\--\_breadcrumb-link-color-current-page);
text-decor= ation: none; } rh-breadcrumb \> ol \> li \>
a\[aria-current=3D\"page\"\] { cursor: default; point= er-events: none;
} rh-breadcrumb\[variant=3D\"subtle\"\] \> ol \> li:last-child,
rh-breadcrumb\[varia= nt=3D\"subtle\"\] \> ol \> li \>
a\[aria-current=3D\"page\"\] { color: var(\--\_breadcr=
umb-link-color-current-page-subtle); } rh-surface\[data-v-fa60319a\] {
\--rh-color-surface: transparent; } .breadcrumbs\[data-v-fa60319a\] {
background-color: light-dark(var(\--rh-color=
-surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,#383838));
padding: v= ar(\--rh-space-lg,16px) var(\--rh-space-2xl,32px); }
.main-breadcrumbs-container\[data-v-fa60319a\] { align-items: center;
display= : flex; gap: var(\--rh-space-xl,24px); }
rh-breadcrumb\[data-v-fa60319a\] { flex: 1 1 0%; } rh-breadcrumb \> ol
\> li\[data-v-fa60319a\] { margin-block-end: 0px; padding-b= ottom: 2px;
padding-top: 2px; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
https://docs.redhat.com/\_nuxt/SearchAutocomplete.Cvjafavi.css \@charset
\"utf-8\"; .search-container\[data-v-7ec4cdc4\] { height: 100%; }
.form-box\[data-v-7ec4cdc4\], .search-container\[data-v-7ec4cdc4\] {
align-item= s: center; display: flex; justify-content: center; width:
100%; } .form-box\[data-v-7ec4cdc4\] { border: 1px solid
light-dark(var(\--rh-color-bo=
rder-subtle-on-light,#c7c7c7),var(\--rh-color-surface-dark,#383838)); }
.search-box\[data-v-7ec4cdc4\] { align-items: center; display: flex;
justify-= content: space-between; position: relative; width: 100%; }
ul\[data-v-7ec4cdc4\] { list-style-type: none; }
#search-list\[data-v-7ec4cdc4\] { background:
light-dark(var(\--rh-color-surfa=
ce-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f)); border: 1px
soli= d
light-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-=
surface-dark,#383838)); box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 4px;
color:=
light-dark(var(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-te=
xt-primary-on-dark,#fff)); cursor: pointer; display: block; left: 0px;
marg= in: 0px; padding: 0px; position: absolute; top: 37px; width: 100%;
z-index:= 200; } #search-list li\[data-v-7ec4cdc4\] { align-items:
center; border-bottom: 1px = solid
light-dark(#f0f0f0,var(\--rh-color-surface-dark,#383838)); display: fl=
ex; justify-content: space-between; padding: 0.75rem; } #search-list
.active\[data-v-7ec4cdc4\], #search-list li\[data-v-7ec4cdc4\]:hov= er {
background: light-dark(#f0f0f0,var(\--rh-color-surface-dark,#383838)); =
} .group-title\[data-v-7ec4cdc4\] { border-top: 1px solid rgb(77, 77,
77); colo= r: rgb(77, 77, 77); cursor: default; font-size: 12px;
font-weight: 400; poi= nter-events: none; }
.group-title\[data-v-7ec4cdc4\], .group-title\[data-v-7ec4cdc4\]:hover {
backgr= ound: rgb(255, 255, 255); }
.search-item-text-elipsis\[data-v-7ec4cdc4\] { display: inline-block;
max-wid= th: 48%; overflow: hidden; text-overflow: ellipsis;
white-space: nowrap; } .search-item-text\[data-v-7ec4cdc4\] {
padding-left: 1.75rem; } .search-item-chip\[data-v-7ec4cdc4\] { float:
right; font-size: 12px; \--rh-fo= nt-size-body-text-sm: 12px; }
.search-icon-form\[data-v-7ec4cdc4\] { color:
light-dark(var(\--rh-color-gray-=
50,#707070),var(\--rh-color-status-neutral-on-dark,#c7c7c7)); left:
12px; po= sition: absolute; } .input-search-box\[data-v-7ec4cdc4\] {
appearance: none; background-color: li=
ght-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darke=
r,#1f1f1f)); border: 0px; font-family:
var(\--rh-font-family-body-text,\"Red = Hat
Text\",\"RedHatText\",Arial,sans-serif); font-size:
var(\--rh-font-size-bod= y-text-md,1rem); height: 36px; padding: 0px
40px; width: 100%; } .input-search-box\[data-v-7ec4cdc4\]::placeholder {
color: light-dark(var(\--r=
h-color-text-secondary-on-light,#4d4d4d),var(\--rh-color-text-secondary-on-d=
ark,#c7c7c7)); } .input-clear-btn\[data-v-7ec4cdc4\] { align-items:
center; background-color: = transparent; border: none; display: flex;
height: 36px; justify-content: ce= nter; margin-right: -30px; outline:
none; transform: translate(-30px); }
.input-clear-btn\[data-v-7ec4cdc4\]:focus { border: 1px solid
var(\--rh-color-= accent-base-on-light,#06c); } .input-clear-btn:focus
.input-clear-icon\[data-v-7ec4cdc4\] { color: var(\--rh=
-color-canvas-black,#151515); } .input-clear-icon\[data-v-7ec4cdc4\] {
color: rgb(107, 110, 114); cursor: poi= nter; }
.input-clear-icon\[data-v-7ec4cdc4\]:hover { color:
var(\--rh-color-canvas-bla= ck,#151515); }
.form-submit-btn\[data-v-7ec4cdc4\]::part(button) { align-items: center;
back= ground-color:
light-dark(var(\--rh-color-surface-light,#e0e0e0),var(\--rh-col=
or-interactive-secondary-default-on-light,#4d4d4d)); border-radius: 0px;
di= splay: flex; height: 36px; justify-content: center;
\--\_default-border-color= : var(\--rh-color-gray-20,#e0e0e0); margin:
0px; } .form-submit-icon\[data-v-7ec4cdc4\] { color:
light-dark(#151515,var(\--rh-col= or-surface-light,#e0e0e0)); }
.input-close-btn\[data-v-7ec4cdc4\] { background: none; border: none;
cursor:= pointer; margin: 0 var(\--rh-space-lg,16px); }
.input-close-icon\[data-v-7ec4cdc4\] { color:
var(\--rh-color-white,#fff); } \@media (max-width: 992px) {
.form-box\[data-v-7ec4cdc4\] { gap: var(\--rh-space-md,8px); margin:
auto; w= idth: 100%; } .input-search-box\[data-v-7ec4cdc4\]::placeholder
{ font-family: var(\--rh-f= ont-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif); font-si= ze:
var(\--rh-font-size-body-text-md,1rem); font-weight:
var(\--rh-font-weigh= t-code-regular,400); line-height: 24px; }
.search-item-text-elipsis\[data-v-7ec4cdc4\] { max-width: 60%; } }
\@media (max-width: 767px) { .input-close-btn\[data-v-7ec4cdc4\] {
display: none; } .input-search-box\[data-v-7ec4cdc4\] { border-radius:
0px; } .input-clear-btn\[data-v-7ec4cdc4\] { margin-right: -42px;
transform: trans= late(-42px); } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location: https://docs.redhat.com/\_nuxt/entry.Bo8DaSfU.css
\@charset \"utf-8\"; :root { \--pfe-navigation\_\_dropdown\--Color:
light-dark(var(\--rh-color-text-p=
rimary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff));
\--pfe-= navigation\_\_dropdown\--Background:
light-dark(var(\--rh-color-surface-lightes=
t,#fff),var(\--rh-color-surface-darker,#1f1f1f));
\--pfe-navigation\_\_nav-bar-= -toggle\--BackgroundColor\--active:
light-dark(var(\--rh-color-surface-lightes=
t,#fff),var(\--rh-color-surface-darker,#1f1f1f));
\--pfe-navigation\_\_nav-bar-= -Color\--active:
light-dark(var(\--rh-color-text-primary-on-light,#151515),va=
r(\--rh-color-text-primary-on-dark,#fff));
\--pfe-navigation\_\_dropdown\--separ= ator\--Border: 1px solid
light-dark(#d2d2d2,var(\--rh-color-border-subtle-on-= dark,#707070)); }
.section .titlepage { gap: 0.75rem; } .section .titlepage, div.edit {
align-items: center; display: flex; } div.edit { font-size: 0.9rem;
margin-bottom: 8px; } div.edit \> a { align-items: center; display:
flex; } .edit pf-icon { margin-right: 4px; }
rh-tile\[color-palette=3D\"darkest\"\] a { color:
var(\--rh-color-interactive-pr= imary-default-on-dark,#92c5f9); }
rh-tile\[color-palette=3D\"darkest\"\]:not(:defined) { background-color:
var(\--= rh-color-surface-darkest,#151515); border-color:
var(\--rh-color-border-subt= le-on-dark,#707070); color:
var(\--rh-color-text-primary-on-dark,#fff); }
rh-tile\[color-palette=3D\"darkest\"\]:not(:defined) img { aspect-ratio:
1 / 1;= width: 48px; }
rh-tile\[color-palette=3D\"darkest\"\]:not(:defined) img + h3 {
margin-block-st= art: var(\--rh-space-2xl,32px); } rh-tile a { color:
var(\--rh-color-interactive-primary-default,light-dark(va=
r(\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh-color-inte=
ractive-primary-default-on-dark,#92c5f9))); } rh-tile:not(:defined) {
background-color: light-dark(var(\--rh-color-surface=
-lightest,#fff),var(\--rh-color-surface-darkest,#151515)); border:
var(\--rh-= border-width-sm,1px) solid
var(\--rh-color-border-subtle,light-dark(var(\--rh=
-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-on-dark=
,#707070))); color:
var(\--rh-color-text-primary,light-dark(var(\--rh-color-t=
ext-primary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff)));
= padding: var(\--rh-space-2xl,32px) var(\--rh-space-2xl,32px)
var(\--rh-space-3= xl,48px) var(\--rh-space-2xl,32px); }
rh-tile:not(:defined) img { aspect-ratio: 1 / 1; width: 48px; }
rh-tile:not(:defined) img + h3 { margin-block-start:
var(\--rh-space-2xl,32p= x); } rh-card.explore-products { color:
var(\--rh-color-text-primary,light-dark(va=
r(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-text-primary-on-=
dark,#fff))); } rh-card.explore-products:not(:defined) { align-items:
center; display: flex= ; flex-direction: column; justify-content:
center; } rh-card.explore-products:not(:defined) h4 { font-size:
var(\--rh-font-size-h= eading-sm,1.5rem); padding-bottom:
var(\--rh-space-lg,16px); } rh-card.explore-products:not(:defined)
rh-cta\[variant=3D\"secondary\"\]:not(:d= efined) { border:
var(\--rh-border-width-sm,1px) solid var(\--rh-color-border=
-strong,light-dark(var(\--rh-color-border-strong-on-light,#151515),var(\--rh-=
color-border-strong-on-dark,#fff))); border-radius:
var(\--rh-border-radius-= default,3px); max-width: fit-content;
padding-block: var(\--rh-space-lg,16px= ); padding-inline:
var(\--rh-space-2xl,32px); } rh-card.explore-products:not(:defined)
rh-cta\[variant=3D\"secondary\"\]:not(:d= efined) a { color:
var(\--rh-color-text-primary,light-dark(var(\--rh-color-te=
xt-primary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff)));
} .theme-container\[data-v-9af16c28\] { height: 36px; position:
relative; } rh-button\[data-v-9af16c28\],
rh-button\[data-v-9af16c28\]::part(button) { heig= ht: 36px; }
rh-button\[variant=3D\"tertiary\"\]\[data-v-9af16c28\] {
\--rh-color-icon-secondar= y-on-dark:
var(\--rh-color-surface-darkest,#151515); \--rh-color-icon-seconda=
ry-on-light: var(\--rh-color-surface-lightest,#fff); }
rh-button\[variant=3D\"tertiary\"\].footer\[data-v-9af16c28\] {
\--rh-color-border= -strong: transparent; }
rh-button\[variant=3D\"tertiary\"\]\[data-v-9af16c28\]::part(button) {
padding: 1= 0px var(\--rh-space-lg,16px); }
rh-button\[variant=3D\"tertiary\"\].footer\[data-v-9af16c28\]::part(button)
{ pad= ding: 10px 0px; } .popover-container\[data-v-9af16c28\] {
background-color: light-dark(var(\--rh=
-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
bord= er-radius: 6px; box-shadow: var( \--rh-box-shadow-md,0 4px 6px 1px
light-dar= k(hsla(0,0%,8%,.25),rgba(0,0,0,.5)) ); position: absolute;
right: 0px; top:= 42px; width: 168px; z-index: 1; }
.footer-popover-container\[data-v-9af16c28\] { left: 0px; top: 54px; }
.theme-list-container\[data-v-9af16c28\] { align-items: flex-start;
display: = flex; flex-direction: column; list-style: none; margin: 0px;
padding: var(-= -rh-space-md,8px) 0; } .theme-list\[data-v-9af16c28\] {
margin: 0px; padding: 0px; width: 100%; } .theme-list
button.theme-btn\[data-v-9af16c28\] { align-items: center; backgr=
ound-color: transparent; border: none; color:
light-dark(var(\--rh-color-gra=
y-95,#151515),var(\--rh-color-white,#fff)); cursor: pointer; display:
flex; = justify-content: flex-start; padding: var(\--rh-space-md,8px)
var(\--rh-space= -xl,24px); width: 100%; } button.theme-btn
span.theme-btn-text\[data-v-9af16c28\] { font-family: \"Red H= at
Text\"; font-size: var(\--rh-font-size-body-text-sm,.875rem);
font-weight:= var(\--rh-font-weight-body-text-regular,400);
padding-left: var(\--rh-space-= md,8px); }
button.theme-btn\[data-v-9af16c28\]:hover { background-color:
light-dark(var(=
\--rh-color-gray-20,#e0e0e0),var(\--rh-color-gray-70,#383838)); }
section\[data-v-babbacad\] { padding: 0px; } h1\[data-v-babbacad\],
h2\[data-v-babbacad\] { margin: 0px; }
.main-error-container\[data-v-babbacad\] { background-color:
light-dark(var(-=
-rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
p= adding-bottom: var(\--rh-space-7xl,128px); padding-top:
var(\--rh-space-5xl,8= 0px); } .main-error\[data-v-babbacad\] {
background-color: light-dark(var(\--rh-color-=
surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); margin:
0px= auto; max-width: 44rem; padding: var(\--rh-space-3xl,48px); }
.cloud-IT-image\[data-v-babbacad\] { width: 9rem; }
.error-text-container p\[data-v-babbacad\] { color:
light-dark(#6a6e73,var(\--= rh-color-white,#fff)); font-size:
var(\--rh-font-size-body-text-lg,1.125rem)= ; }
.help-container\[data-v-babbacad\] { margin-top:
var(\--rh-space-4xl,64px); } .form-box-container\[data-v-babbacad\] {
justify-content: center; margin-top:= var(\--rh-space-xl,24px); }
.error-search-box\[data-v-babbacad\],
.form-box-container\[data-v-babbacad\] { = align-items: center; display:
flex; width: 100%; } .error-search-box\[data-v-babbacad\] {
justify-content: space-between; positi= on: relative; }
.search-icon-form\[data-v-babbacad\] { color:
light-dark(var(\--rh-color-gray-=
50,#707070),var(\--rh-color-status-neutral-on-dark,#c7c7c7)); left:
12px; po= sition: absolute; } .arrow-right-button\[data-v-babbacad\] {
color: light-dark(var(\--rh-color-gra=
y-95,#151515),var(\--rh-color-icon-secondary-on-dark,#fff)); }
.input-box\[data-v-babbacad\] { appearance: none; background-color:
light-dar=
k(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f=
1f)); border-top-color: ; border-top-style: ; border-top-width: ;
border-bo= ttom-color: ; border-bottom-style: ; border-bottom-width: ;
border-left-col= or: ; border-left-style: ; border-left-width: ;
border-image-source: ; bord= er-image-slice: ; border-image-width: ;
border-image-outset: ; border-image= -repeat: ; border-right: none;
font-family: var(\--rh-font-family-body-text,= \"Red Hat
Text\",\"RedHatText\",Arial,sans-serif); font-size: var(\--rh-font-siz=
e-body-text-md,1rem); height: 36px; padding: 0px 40px; text-overflow:
ellip= sis; white-space: nowrap; width: 100%; }
.input-box\[data-v-babbacad\]::placeholder { color:
light-dark(var(\--rh-color=
-text-secondary-on-light,#4d4d4d),var(\--rh-color-text-secondary-on-dark,#c7=
c7c7)); font-family: var(\--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatT= ext\",Arial,sans-serif); font-size:
var(\--rh-font-size-body-text-md,1rem); f= ont-weight:
var(\--rh-font-weight-code-regular,400); line-height: 24px; }
.form-box-container rh-button\[data-v-babbacad\]::part(button) {
align-items:= center; background-color:
light-dark(var(\--rh-color-gray-20,#e0e0e0),var(-=
-rh-color-status-neutral-on-light,#4d4d4d)); border-radius: 0px;
display: f= lex; height: 36px; justify-content: center;
\--\_default-border-color: light-=
dark(var(\--rh-color-gray-20,#e0e0e0),var(\--rh-color-status-neutral-on-light=
,#4d4d4d)); } .input-clear-btn\[data-v-babbacad\] { align-items: center;
background-color: = transparent; border: none; display: flex; height:
36px; justify-content: ce= nter; margin-right: -30px; outline: none;
transform: translate(-30px); } .input-clear-btn\[data-v-babbacad\]:focus
{ border: 1px solid var(\--rh-color-= accent-base-on-light,#06c); }
.input-clear-btn:focus .input-clear-icon\[data-v-babbacad\] { color:
var(\--rh= -color-gray-95,#151515); }
.input-clear-icon\[data-v-babbacad\] { color: rgb(107, 110, 114);
cursor: poi= nter; } .input-clear-icon\[data-v-babbacad\]:hover { color:
var(\--rh-color-gray-95,#1= 51515); } .help-links\[data-v-babbacad\] {
margin-top: var(\--rh-space-xl,24px); padding= : 0
var(\--rh-space-md,8px); } .help-links li\[data-v-babbacad\] { display:
inline-block; list-style: none; = margin-right:
var(\--rh-space-xl,24px); padding: var(\--rh-space-xs,4px) 0; }
.help-links li a\[data-v-babbacad\] { color:
light-dark(var(\--rh-context-ligh=
t-color-text-link,#06c),var(\--rh-color-blue-30,#92c5f9)); cursor:
pointer; = text-decoration: none; } \@media (max-width: 992px) {
.main-error\[data-v-babbacad\] { padding: var(\--rh-space-lg,16px); }
.cloud-IT-image\[data-v-babbacad\] { width: 6rem; } }
.feedback-container\[data-v-9de855e7\] { align-items: center;
background-colo= r:
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-=
darker,#1f1f1f)); display: flex; justify-content: flex-end; min-height:
48p= x; padding: var(\--rh-space-lg,16px) var(\--rh-space-2xl,32px); }
.toggle-theme-btn\[data-v-9de855e7\] { padding-left:
var(\--rh-space-xl,24px);= } \@media (max-width: 767px) {
.feedback-container\[data-v-9de855e7\] { padding:
var(\--rh-space-lg,16px); = } } \@media (max-width: 1024px) {
.toggle-theme-btn\[data-v-9de855e7\] { display: none; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location: https://docs.redhat.com/styles/rh-code-block-prism.css
\@charset \"utf-8\"; rh-code-block { \--\_styles-applied: true; &
pre\[class\*=3D\"language-\"\]::selection, &
pre\[class\*=3D\"language-\"\] ::sel= ection, &
code\[class\*=3D\"language-\"\]::selection, &
code\[class\*=3D\"language-= \"\] ::selection { text-shadow: none;
background: var(\--\_selected-text-backgr= ound); } \@media print { &
code\[class\*=3D\"language-\"\], & pre\[class\*=3D\"language-\"\] {
text-shadow: = none; } } & .token.atrule { color:
var(\--\_at-rule-color); } & .token.attr-name { color:
var(\--\_attr-name-color); } & .token.attr-value { color:
var(\--\_attr-value-color); } & .token.bold { font-weight:
var(\--\_important-color); } & .token.boolean { color:
var(\--\_boolean-color); } & .token.builtin { color:
var(\--\_built-in-color); } & .token.cdata { color:
var(\--\_cdata-color); } & .token.char { color:
var(\--\_character-color); } & .token.class-name { color:
var(\--\_class-name-color); } & .token.comment { color:
var(\--\_comment-color); } & .token.constant { color:
var(\--\_constant-color); } & .token.deleted { color:
var(\--\_deleted-color); } & .token.function { color:
var(\--\_function-name-color); } & .token.important { color:
var(\--\_important-color); } & .token.inserted { color:
var(\--\_inserted-color); } & .token.keyword { color:
var(\--\_keyword-color); } & .token.namespace { color:
var(\--\_namespace-color); } & .token.number { color:
var(\--\_number-color); } & .token.operator { color:
var(\--\_operator-color); } & .token.property { color:
var(\--\_property-color); } & .token.punctuation { color:
var(\--\_punctuation-color); } & .token.regex { color:
var(\--\_regex-color); } & .token.selector { color:
var(\--\_selector-color); } & .token.string { color:
var(\--\_string-color); } & .token.symbol { color:
var(\--\_symbol-color); } & .token.tag { color: var(\--\_tag-color); } &
.token.url { color: var(\--\_url-color); } & .token.variable { color:
var(\--\_variable-color); } & .token.italic { font-style: italic; } &
.token.entity { color: var(\--\_entity-color); cursor: help; } &
.token.prolog, & .token.doctype { color: var(\--\_doctype-color); } &
.language-css .token.string, & .style .token.string { color:
var(\--\_ope= rator-color); } & \> pre { opacity: 1; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
https://docs.redhat.com/styles/rh-table\--lightdom.min.css \@charset
\"utf-8\"; :root { \--rh-table\--wrappers\--width: auto; } rh-table {
display: block; max-width: 100%; margin: 2rem 0px; }
rh-table.full-screen\[class\]\[class\] { position: relative; z-index:
100; } rh-table\[class\]\[class\] table { margin: 0px; table-layout:
fixed; border: 0p= x; border-collapse: collapse; }
rh-table\[class\]\[class\] table caption { margin-top: 0.5rem;
margin-bottom: 0= .5rem; color:
var(\--pfe-table\_\_caption\--Color,currentColor); font-weight: 7= 00;
text-align: center; } rh-table\[class\]\[class\] table td,
rh-table\[class\]\[class\] table th { padding:= 0.5em 1rem;
border-right: 0px; border-bottom: 1px solid var(\--pfe-table\--B=
order,#d2d2d2); border-left: 0px; transition: background 0.25s ease-out;
} rh-table\[class\]\[class\] table td.content\--lg,
rh-table\[class\]\[class\] table t= h.content\--lg { min-width: 16em; }
rh-table\[class\]\[class\] table td.content\--md,
rh-table\[class\]\[class\] table t= h.content\--md { min-width: 10em; }
rh-table\[class\]\[class\] table td.halign-left,
rh-table\[class\]\[class\] table t= h.halign-left { text-align: left; }
rh-table\[class\]\[class\] table td.halign-center,
rh-table\[class\]\[class\] table= th.halign-center { text-align: center;
} rh-table\[class\]\[class\] table td.halign-right,
rh-table\[class\]\[class\] table = th.halign-right { text-align: right;
} rh-table\[class\]\[class\] table td.valign-top,
rh-table\[class\]\[class\] table th= .valign-top { vertical-align: top;
} rh-table\[class\]\[class\] table td.valign-middle,
rh-table\[class\]\[class\] table= th.valign-middle { vertical-align:
middle; } rh-table\[class\]\[class\] table td.valign-bottom,
rh-table\[class\]\[class\] table= th.valign-bottom { vertical-align:
bottom; } rh-table\[class\]\[class\] table thead td,
rh-table\[class\]\[class\] table thead t= h { padding-top: 1.5em;
border-top: 0px; font-weight: 600; background: var(=
\--pfe-table\_\_th\--Background,transparent); }
rh-table\[class\]\[class\] table .rh-table\_\_sort-button { position:
relative; d= isplay: inline-flex; margin: 0px; padding: 0px; border:
0px; font: inherit;= background: 0px 0px; cursor: pointer; appearance:
none; } rh-table\[class\]\[class\] table .rh-table\_\_sort-button svg {
align-self: cente= r; -webkit-box-ordinal-group: 2; order: 1; position:
relative; width: 22px;= height: 22px; margin-left: 0.5em; padding: 3px;
border-radius: 50%; } rh-table\[class\]\[class\] table
.rh-table\_\_sort-button .arrow\--down, rh-table\[= class\]\[class\]
table .rh-table\_\_sort-button .arrow\--up { fill: rgb(21, 21, 2= 1);
opacity: 0.3; } rh-table\[class\]\[class\] table
.rh-table\_\_sort-button:hover svg { background:= rgb(255, 255, 255); }
rh-table\[class\]\[class\] table .rh-table\_\_sort-button:hover
.arrow\--down, rh-= table\[class\]\[class\] table
.rh-table\_\_sort-button:hover .arrow\--up { fill: r= gb(0, 102, 204); }
rh-table\[class\]\[class\] table .rh-table\_\_header\--sorted-by\--za
.arrow\--down = { opacity: 1; } rh-table\[class\]\[class\] table
.rh-table\_\_header\--sorted-by\--az .arrow\--up { = opacity: 1; }
body.rh-table\--is-full-screen { overflow: hidden; }
rh-table.full-screen { z-index: 1000; }
rh-table\[class\]\[class\].full-screen table { margin: 0px auto; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;700&family=Red+Hat+Text:wght@400;500;700&display=swap
\@charset \"utf-8\"; \@font-face { font-family: \"Red Hat Display\";
font-style: normal; font-weigh= t: 400; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhatdis=
play/v20/8vIQ7wUr0m80wwYf0QCXZzYzUoTg8z6hVYs.woff2\") format(\"woff2\");
unico= de-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF,
U+304, U+3= 08, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
U+20A0-20AB, U+20= AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }
\@font-face { font-family: \"Red Hat Display\"; font-style: normal;
font-weigh= t: 400; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhatdis=
play/v20/8vIQ7wUr0m80wwYf0QCXZzYzUoTg_T6h.woff2\") format(\"woff2\");
unicode-= range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA,
U+2DC, U+304, U+3= 08, U+329, U+2000-206F, U+20AC, U+2122, U+2191,
U+2193, U+2212, U+2215, U+F= EFF, U+FFFD; } \@font-face { font-family:
\"Red Hat Display\"; font-style: normal; font-weigh= t: 500;
font-display: swap; src: url(\"https://fonts.gstatic.com/s/redhatdis=
play/v20/8vIQ7wUr0m80wwYf0QCXZzYzUoTg8z6hVYs.woff2\") format(\"woff2\");
unico= de-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF,
U+304, U+3= 08, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
U+20A0-20AB, U+20= AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }
\@font-face { font-family: \"Red Hat Display\"; font-style: normal;
font-weigh= t: 500; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhatdis=
play/v20/8vIQ7wUr0m80wwYf0QCXZzYzUoTg_T6h.woff2\") format(\"woff2\");
unicode-= range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA,
U+2DC, U+304, U+3= 08, U+329, U+2000-206F, U+20AC, U+2122, U+2191,
U+2193, U+2212, U+2215, U+F= EFF, U+FFFD; } \@font-face { font-family:
\"Red Hat Display\"; font-style: normal; font-weigh= t: 700;
font-display: swap; src: url(\"https://fonts.gstatic.com/s/redhatdis=
play/v20/8vIQ7wUr0m80wwYf0QCXZzYzUoTg8z6hVYs.woff2\") format(\"woff2\");
unico= de-range: U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF,
U+304, U+3= 08, U+329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
U+20A0-20AB, U+20= AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }
\@font-face { font-family: \"Red Hat Display\"; font-style: normal;
font-weigh= t: 700; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhatdis=
play/v20/8vIQ7wUr0m80wwYf0QCXZzYzUoTg_T6h.woff2\") format(\"woff2\");
unicode-= range: U+0-FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA,
U+2DC, U+304, U+3= 08, U+329, U+2000-206F, U+20AC, U+2122, U+2191,
U+2193, U+2212, U+2215, U+F= EFF, U+FFFD; } \@font-face { font-family:
\"Red Hat Text\"; font-style: normal; font-weight: = 400; font-display:
swap; src: url(\"https://fonts.gstatic.com/s/redhattext/v=
18/RrQXbohi_ic6B3yVSzGBrMxQZqctI8w.woff2\") format(\"woff2\");
unicode-range: = U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF,
U+304, U+308, U+329,= U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
U+20A0-20AB, U+20AD-20C0, U= +2113, U+2C60-2C7F, U+A720-A7FF; }
\@font-face { font-family: \"Red Hat Text\"; font-style: normal;
font-weight: = 400; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhattext/v=
18/RrQXbohi_ic6B3yVSzGBrMxQaKct.woff2\") format(\"woff2\");
unicode-range: U+0= -FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA,
U+2DC, U+304, U+308, U+329,= U+2000-206F, U+20AC, U+2122, U+2191,
U+2193, U+2212, U+2215, U+FEFF, U+FFF= D; } \@font-face { font-family:
\"Red Hat Text\"; font-style: normal; font-weight: = 500; font-display:
swap; src: url(\"https://fonts.gstatic.com/s/redhattext/v=
18/RrQXbohi_ic6B3yVSzGBrMxQZqctI8w.woff2\") format(\"woff2\");
unicode-range: = U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF,
U+304, U+308, U+329,= U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
U+20A0-20AB, U+20AD-20C0, U= +2113, U+2C60-2C7F, U+A720-A7FF; }
\@font-face { font-family: \"Red Hat Text\"; font-style: normal;
font-weight: = 500; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhattext/v=
18/RrQXbohi_ic6B3yVSzGBrMxQaKct.woff2\") format(\"woff2\");
unicode-range: U+0= -FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA,
U+2DC, U+304, U+308, U+329,= U+2000-206F, U+20AC, U+2122, U+2191,
U+2193, U+2212, U+2215, U+FEFF, U+FFF= D; } \@font-face { font-family:
\"Red Hat Text\"; font-style: normal; font-weight: = 700; font-display:
swap; src: url(\"https://fonts.gstatic.com/s/redhattext/v=
18/RrQXbohi_ic6B3yVSzGBrMxQZqctI8w.woff2\") format(\"woff2\");
unicode-range: = U+100-2BA, U+2BD-2C5, U+2C7-2CC, U+2CE-2D7, U+2DD-2FF,
U+304, U+308, U+329,= U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020,
U+20A0-20AB, U+20AD-20C0, U= +2113, U+2C60-2C7F, U+A720-A7FF; }
\@font-face { font-family: \"Red Hat Text\"; font-style: normal;
font-weight: = 700; font-display: swap; src:
url(\"https://fonts.gstatic.com/s/redhattext/v=
18/RrQXbohi_ic6B3yVSzGBrMxQaKct.woff2\") format(\"woff2\");
unicode-range: U+0= -FF, U+131, U+152-153, U+2BB-2BC, U+2C6, U+2DA,
U+2DC, U+304, U+308, U+329,= U+2000-206F, U+20AC, U+2122, U+2191,
U+2193, U+2212, U+2215, U+FEFF, U+FFF= D; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-1d6a8190-88b3-4561-a50a-9f98099c85b9@mhtml.blink \@charset
\"utf-8\"; =0A
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-acb2f814-d119-48f4-ac1a-693bb60538a3@mhtml.blink \@charset
\"utf-8\"; rh-footer \[data-analytics-text=3D\"Buy online (Japan)\"\] {
display: none !imp= ortant; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-538d43bd-128c-487b-b886-01d84a484ef2@mhtml.blink \@charset
\"utf-8\"; rh-cta\[variant=3D\"brick\"\]\[data-v-ca9eac59\]:hover {
text-decoration: underli= ne solid
light-dark(var(\--rh-color-interactive-primary-hover-on-light,#036)=
,var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc)); }
\[variant=3D\"brick\"\]\[data-v-ca9eac59\] { max-width: 150px; }
.pagination\[data-v-ca9eac59\] { display: flex; justify-content:
space-betwee= n; margin-bottom: var(\--rh-space-6xl,96px); margin-top:
var(\--rh-space-4xl,= 4rem); } .previous-btn\[data-v-ca9eac59\] {
margin-right: auto; } .next-btn\[data-v-ca9eac59\] { margin-left: auto;
} .next-btn\[data-v-ca9eac59\]:hover,
.previous-btn\[data-v-ca9eac59\]:hover { cu= rsor: pointer; }
.next-btn.disabled\[data-v-ca9eac59\],
.previous-btn.disabled\[data-v-ca9eac59= \] { background-color:
var(\--rh-color-bg-disabled,#f2f2f2); cursor: not-allo= wed;
pointer-events: none; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-c403079d-52be-4204-84a3-e7673fb8f2cc@mhtml.blink \@charset
\"utf-8\"; .html-container\[data-v-b8fb6e74\] { padding: 2rem 1.5rem
0px; } rh-alert\[data-v-b8fb6e74\] { color: rgb(21, 21, 21); } \@media
(max-width: 772px) { .html-container\[data-v-b8fb6e74\] { padding: 3rem
1rem 0px; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-105a5f0d-5fb3-4d1b-bd98-592ddfd42a54@mhtml.blink \@charset
\"utf-8\"; .item\[data-v-c61ac788\] { line-height: 22px; } #toc
.link\[data-v-c61ac788\], #toc-mobile .link\[data-v-c61ac788\] { color:
li=
ght-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
} #toc .link\[data-v-c61ac788\], #toc-mobile .link\[data-v-c61ac788\],
.heading\[d= ata-v-c61ac788\], .sub-nav .link\[data-v-c61ac788\],
.sub-nav .link .link\[data= -v-c61ac788\] { display: block; padding-top:
; padding-bottom: ; padding-lef= t: ; padding-right: 2.5em;
text-decoration: none; transition: background-co= lor 0.25s; }
.heading\[data-v-c61ac788\]:hover, .link\[data-v-c61ac788\]:hover,
.sub-nav .li= nk\[data-v-c61ac788\]:hover { background:
light-dark(var(\--rh-color-surface-l=
ighter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow:
rgb(210,= 210, 210) 3px 0px inset; color:
light-dark(var(\--rh-color-gray-95,#151515)=
,var(\--rh-color-white,#fff)); } ol\[data-v-c61ac788\] { margin: 0px;
padding: 0px; } li\[data-v-c61ac788\], ol\[data-v-c61ac788\],
ul\[data-v-c61ac788\] { list-style:= none; margin: 0px; }
.chapter-title\[data-v-c61ac788\] { font-size: 1em; }
.sub-nav\[data-v-c61ac788\] { font-size: 1em; line-height: 24px;
list-style: = none; margin: 0px; padding-left: 16px; } .sub-nav
.link\[data-v-c61ac788\]:hover { color: rgb(21, 21, 21); }
.active\[data-v-c61ac788\] { background:
light-dark(var(\--rh-color-surface-li=
ghter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow: inset
3px= 0 0 0 var(\--rh-color-icon-primary-on-light,#e00); }
.sub-chapter-title\[data-v-c61ac788\], .sub-chapter-title
a\[data-v-c61ac788\] = { font-size: 0.875rem; }
summary\[data-v-c61ac788\] { cursor: pointer; list-style: none;
position: rel= ative; }
summary\[data-v-c61ac788\]::-webkit-details-marker { display: none; }
html\[data-v-c61ac788\] { \--details-transition-time: .4s; }
.chapter-landing-page\[data-v-c61ac788\] { font-weight: 500; }
details\[open\]:first-of-type \> .heading\[data-v-c61ac788\]::after {
transform:= rotate(135deg); } details\[data-v-c61ac788\] { max-height:
var(\--details-height-closed,auto); t= ransition: all ease-out
var(\--details-transition-time,0); } details\[open\]\[data-v-c61ac788\]
{ max-height: var(\--details-height-open,auto= ); } details
.heading.sub-chapter-title\[data-v-c61ac788\]::after, details .headin=
g\[data-v-c61ac788\]::after { border-right: 3px solid
light-dark(var(\--rh-col=
or-gray-95,#151515),var(\--rh-color-white,#fff)); border-top: 3px solid
ligh=
t-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
color: = rgb(21, 21, 21); content: \"\"; display: flex; float: right;
height: 9px; mar= gin-left: 16px; position: absolute; right:
var(\--rh-space-xl,24px); top: 14= px; transform: rotate(45deg); width:
9px; } details .heading.sub-chapter-title\[data-v-c61ac788\]::after {
height: 8px; w= idth: 8px; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-20fc2390-e414-44e1-aa67-d3cf83efb5c9@mhtml.blink \@charset
\"utf-8\"; ol\[data-v-2b26994c\] { margin: 0px; padding: 0px; }
li\[data-v-2b26994c\], ol\[data-v-2b26994c\], ul\[data-v-2b26994c\] {
list-style:= none; margin: 0px; } .chapter-title\[data-v-2b26994c\] {
font-size: 1em; } .sub-chapter-title\[data-v-2b26994c\],
.sub-chapter-title a\[data-v-2b26994c\] = { font-size: 0.875rem; } #toc
.link\[data-v-2b26994c\], #toc-mobile .link\[data-v-2b26994c\],
.heading\[d= ata-v-2b26994c\], .sub-nav .link\[data-v-2b26994c\],
.sub-nav .link .link\[data= -v-2b26994c\] { display: block; padding-top:
; padding-bottom: ; padding-lef= t: ; padding-right: 2.5em;
text-decoration: none; transition: background-co= lor 0.25s; }
.heading\[data-v-2b26994c\]:hover, .link\[data-v-2b26994c\]:hover,
.sub-nav .li= nk\[data-v-2b26994c\]:hover { background:
light-dark(var(\--rh-color-surface-l=
ighter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow:
rgb(210,= 210, 210) 3px 0px inset; color:
light-dark(var(\--rh-color-gray-95,#151515)=
,var(\--rh-color-white,#fff)); } details\[open\]:first-of-type \>
.heading\[data-v-2b26994c\]::after { transform:= rotate(135deg); }
.item\[data-v-2b26994c\] { line-height: 22px; } #toc
.link\[data-v-2b26994c\], #toc-mobile .link\[data-v-2b26994c\] { color:
li=
ght-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
} .sub-nav\[data-v-2b26994c\], .toc-wrapper\[data-v-2b26994c\] {
list-style: none= ; margin: 0px; } .toc-wrapper\[data-v-2b26994c\] {
min-width: 100%; padding: 0px; } .sub-nav\[data-v-2b26994c\] {
font-size: 1em; line-height: 24px; padding-left= : 16px; } .sub-nav
.link\[data-v-2b26994c\]:hover { color: rgb(21, 21, 21); }
.active\[data-v-2b26994c\] { background:
light-dark(var(\--rh-color-surface-li=
ghter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); box-shadow: inset
3px= 0 0 0 var(\--rh-color-icon-primary-on-light,#e00); }
.chapter-landing-page\[data-v-2b26994c\] { font-weight: 500; }
summary\[data-v-2b26994c\] { cursor: pointer; list-style: none;
position: rel= ative; }
summary\[data-v-2b26994c\]::-webkit-details-marker { display: none; }
\@keyframes slideDown-2b26994c {=20 0% { height: 0px; opacity: 0; } 100%
{ height: var(\--details-height-open,\"100%\"); opacity: 1; } }
html\[data-v-2b26994c\] { \--details-transition-time: .4s; }
details\[data-v-2b26994c\] { max-height:
var(\--details-height-closed,auto); t= ransition: all ease-out
var(\--details-transition-time,0); } details\[open\]\[data-v-2b26994c\]
{ max-height: var(\--details-height-open,auto= ); } details
.heading.sub-chapter-title\[data-v-2b26994c\]::after, details .headin=
g\[data-v-2b26994c\]::after { border-right: 3px solid
light-dark(var(\--rh-col=
or-gray-95,#151515),var(\--rh-color-white,#fff)); border-top: 3px solid
ligh=
t-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
color: =
light-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-white,#fff));
con= tent: \"\"; display: flex; float: right; height: 9px; margin-left:
16px; posi= tion: absolute; right: var(\--rh-space-xl,24px); top: 14px;
transform: rotat= e(45deg); width: 9px; } details
.heading.sub-chapter-title\[data-v-2b26994c\]::after { height: 8px; w=
idth: 8px; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-91827dcd-6b33-4d5b-b6e0-9671d4072578@mhtml.blink \@charset
\"utf-8\"; .jump-links\[data-v-ebbf8b23\] { max-height: 50vh;
overflow-y: auto; } .jump-links ul\[data-v-ebbf8b23\] { align-items:
flex-start; border-left: 1px= solid
var(\--rh-color-border-subtle-on-light,#c7c7c7); display: flex; flex-=
direction: column; list-style: none; padding: 0px; }
.jump-link-item\[data-v-ebbf8b23\] { border-left: 3px solid transparent;
curs= or: pointer; } .jump-link-item\[data-v-ebbf8b23\]:hover {
border-left-color: light-dark(var(=
\--rh-color-interactive-secondary-hover-on-light,#4d4d4d),var(\--rh-color-int=
eractive-secondary-hover-on-dark,#c7c7c7)); } .jump-link-item
a\[data-v-ebbf8b23\] { color: light-dark(var(\--rh-color-gray-=
60,#4d4d4d),var(\--rh-color-white,#c7c7c7)); display: block;
font-family: \"R= ed Hat Text\"; font-weight: 400; line-height: 21px;
padding: var(\--rh-space-= md,8px) var(\--rh-space-lg,16px); }
.active_link\[data-v-ebbf8b23\] { border-left: 3px solid var(
\--rh-color-bran=
d-red,light-dark(var(\--rh-color-brand-red-on-light,#e00),var(\--rh-color-bra=
nd-red-on-dark,#e00)) ); } .active_link a\[data-v-ebbf8b23\],
.jump-link-item a\[data-v-ebbf8b23\]:focus-v= isible, .jump-link-item
a\[data-v-ebbf8b23\]:hover { color: light-dark(var(\--=
rh-color-gray-95,#151515),var(\--rh-color-white,#fff)); } \@media
(min-width: 992px) { .jump-links\[data-v-ebbf8b23\] { margin-top:
var(\--rh-space-lg,16px); max-h= eight: 80vh; } } \@media (min-width:
992px) and (max-width: 1439px) {
nav#contentPage-tablet-jumpLinks\[data-v-ebbf8b23\] { margin-top: 0px;
max-= height: 40vh; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-50639de0-b761-4352-adf0-d6eacd460bbe@mhtml.blink \@charset
\"utf-8\"; label\[for=3D\"page-format\"\]\[data-v-5cade871\] {
font-weight: 500; } .page-format-dropdown\[data-v-5cade871\] {
appearance: none; background-attac= hment: ; background-origin: ;
background-clip: ; background-color: ; backgr= ound-image:
var(\--select-dropdown-image); background-position: 97% center; =
background-repeat: no-repeat; background-size: auto; border: 1px solid
ligh=
t-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border=
-subtle-on-dark,#707070)); box-shadow: rgb(77, 77, 77) 0px -1px inset;
font= -family: \"Red Hat Text\"; font-size:
var(\--rh-font-size-body-text-md,1rem); = margin-top:
var(\--rh-space-xs,4px); max-width: 100%; min-height: 36px; over= flow:
hidden; padding: 0 var(\--rh-space-xl,24px) 0 var(\--rh-space-md,8px); =
text-overflow: ellipsis; white-space: nowrap; } \@media (max-width:
992px) { label\[for=3D\"page-format\"\]\[data-v-5cade871\] { display:
block; } } \@media (min-width: 1440px) {
.page-format-dropdown\[data-v-5cade871\] { background-position: 90%
center;= } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-f820d84b-4e24-4064-ad76-fa5b55672fd1@mhtml.blink \@charset
\"utf-8\"; rh-breadcrumb { \--\_breadcrumb-caret-image-default:
var(\--rh-breadcrumb-care=
t-image,url(\"data:image/svg+xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www.= w3.org/2000/svg\' width=3D\'10\' height=3D\'15\'
fill=3D\'none\' viewBox=3D\'0 0 10= 15\'%3E%3Cg
clip-path=3D\'url(%23a)\'%3E%3Cpath fill=3D\'red\' d=3D\'m2.5 14.5-2= -2
5-5-5-5 2-2 7 7z\'/%3E%3C/g%3E%3Cdefs%3E%3CclipPath id=3D\'a\'%3E%3Cpath
fi= ll=3D\'%23fff\' d=3D\'M10
.5H0v14h10z\'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E= \"));
\--\_breadcrumb-link-color:
var(\--rh-breadcrumb-link-color,var(\--rh-colo=
r-interactive-primary-default));
\--\_breadcrumb-link-color-current-page: var=
(\--rh-color-text-primary);
\--\_breadcrumb-link-color-current-page-subtle: va=
r(\--rh-color-text-secondary); \--\_breadcrumb-link-color-hover:
var(\--rh-colo= r-interactive-primary-hover);
\--\_breadcrumb-link-color-visited: var(\--rh-co=
lor-interactive-primary-visited-hover);
\--\_breadcrumb-link-color-visited-ho= ver:
var(\--rh-color-interactive-primary-visited-hover);
\--\_breadcrumb-link-= focus-outline-color:
var(\--rh-color-border-interactive); display: block; } rh-breadcrumb ol
{ container: breadcrumbs-list / inline-size; font-size: va=
r(\--rh-font-size-body-text-sm,.875rem); line-height:
var(\--rh-line-height-b= ody-text,1.5); margin-block: 0px;
padding-inline-start: 0px; } rh-breadcrumb \> ol \> li { align-items:
center; display: inline-flex; gap: v= ar(\--rh-space-lg,16px);
margin-block-end: var(\--rh-space-md,8px); padding-i= nline-end:
var(\--rh-breadcrumb-li-padding-inline-end,var(\--rh-space-lg,16px= ));
vertical-align: bottom; } rh-breadcrumb \> ol \>
li:not(:first-of-type)::before { background-color: var=
(\--rh-color-icon-secondary); content: \"\"; display: inline-block;
height: va= r(\--rh-font-size-body-text-sm,.875rem); mask-image:
var(\--\_breadcrumb-caret= -image-default); mask-position: center
center; mask-repeat: no-repeat; widt= h:
var(\--rh-font-size-body-text-sm,.875rem); }
rh-breadcrumb\[variant=3D\"subtle\"\] \> ol \>
li:not(:first-of-type)::before { b= ackground-color:
var(\--rh-color-icon-subtle,#707070); } rh-breadcrumb \> ol \>
li:first-child { padding-inline-start: 0px; } rh-breadcrumb \> ol \>
li:last-child { background-image: none; } rh-breadcrumb \> ol \> li,
rh-breadcrumb \> ol \> li \> a { color: var(\--\_breadc=
rumb-link-color); } rh-breadcrumb \> ol \> li \> a { text-decoration:
underline; } rh-breadcrumb \> ol \> li \> a:is(:hover, :focus, :active)
{ color: var(\--\_bre= adcrumb-link-color-hover); } rh-breadcrumb \> ol
\> li \> a:is(:focus, :focus-visible) { border-radius: var=
(\--rh-border-radius-default,3px); outline: 2px solid
var(\--\_breadcrumb-link= -focus-outline-color); } rh-breadcrumb \> ol
\> li:first-child \> a { margin-inline-start: 0px; } rh-breadcrumb \> ol
\> li:last-child, rh-breadcrumb \> ol \> li \> a\[aria-curren=
t=3D\"page\"\] { color: var(\--\_breadcrumb-link-color-current-page);
text-decor= ation: none; } rh-breadcrumb \> ol \> li \>
a\[aria-current=3D\"page\"\] { cursor: default; point= er-events: none;
} rh-breadcrumb\[variant=3D\"subtle\"\] \> ol \> li:last-child,
rh-breadcrumb\[varia= nt=3D\"subtle\"\] \> ol \> li \>
a\[aria-current=3D\"page\"\] { color: var(\--\_breadcr=
umb-link-color-current-page-subtle); }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-e1776a4d-2021-4648-8fec-29a5f4657f04@mhtml.blink \@charset
\"utf-8\"; rh-surface\[data-v-fa60319a\] { \--rh-color-surface:
transparent; } .breadcrumbs\[data-v-fa60319a\] { background-color:
light-dark(var(\--rh-color=
-surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,#383838));
padding: v= ar(\--rh-space-lg,16px) var(\--rh-space-2xl,32px); }
.main-breadcrumbs-container\[data-v-fa60319a\] { align-items: center;
display= : flex; gap: var(\--rh-space-xl,24px); }
rh-breadcrumb\[data-v-fa60319a\] { flex: 1 1 0%; } rh-breadcrumb \> ol
\> li\[data-v-fa60319a\] { margin-block-end: 0px; padding-b= ottom: 2px;
padding-top: 2px; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-3faea670-82a3-4775-b8b4-59813de98d2d@mhtml.blink \@charset
\"utf-8\"; .search-container\[data-v-7ec4cdc4\] { height: 100%; }
.form-box\[data-v-7ec4cdc4\], .search-container\[data-v-7ec4cdc4\] {
align-item= s: center; display: flex; justify-content: center; width:
100%; } .form-box\[data-v-7ec4cdc4\] { border: 1px solid
light-dark(var(\--rh-color-bo=
rder-subtle-on-light,#c7c7c7),var(\--rh-color-surface-dark,#383838)); }
.search-box\[data-v-7ec4cdc4\] { align-items: center; display: flex;
justify-= content: space-between; position: relative; width: 100%; }
ul\[data-v-7ec4cdc4\] { list-style-type: none; }
#search-list\[data-v-7ec4cdc4\] { background:
light-dark(var(\--rh-color-surfa=
ce-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f)); border: 1px
soli= d
light-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-=
surface-dark,#383838)); box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 4px;
color:=
light-dark(var(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-te=
xt-primary-on-dark,#fff)); cursor: pointer; display: block; left: 0px;
marg= in: 0px; padding: 0px; position: absolute; top: 37px; width: 100%;
z-index:= 200; } #search-list li\[data-v-7ec4cdc4\] { align-items:
center; border-bottom: 1px = solid
light-dark(#f0f0f0,var(\--rh-color-surface-dark,#383838)); display: fl=
ex; justify-content: space-between; padding: 0.75rem; } #search-list
.active\[data-v-7ec4cdc4\], #search-list li\[data-v-7ec4cdc4\]:hov= er {
background: light-dark(#f0f0f0,var(\--rh-color-surface-dark,#383838)); =
} .group-title\[data-v-7ec4cdc4\] { border-top: 1px solid rgb(77, 77,
77); colo= r: rgb(77, 77, 77); cursor: default; font-size: 12px;
font-weight: 400; poi= nter-events: none; }
.group-title\[data-v-7ec4cdc4\], .group-title\[data-v-7ec4cdc4\]:hover {
backgr= ound: rgb(255, 255, 255); }
.search-item-text-elipsis\[data-v-7ec4cdc4\] { display: inline-block;
max-wid= th: 48%; overflow: hidden; text-overflow: ellipsis;
white-space: nowrap; } .search-item-text\[data-v-7ec4cdc4\] {
padding-left: 1.75rem; } .search-item-chip\[data-v-7ec4cdc4\] { float:
right; font-size: 12px; \--rh-fo= nt-size-body-text-sm: 12px; }
.search-icon-form\[data-v-7ec4cdc4\] { color:
light-dark(var(\--rh-color-gray-=
50,#707070),var(\--rh-color-status-neutral-on-dark,#c7c7c7)); left:
12px; po= sition: absolute; } .input-search-box\[data-v-7ec4cdc4\] {
appearance: none; background-color: li=
ght-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darke=
r,#1f1f1f)); border: 0px; font-family:
var(\--rh-font-family-body-text,\"Red = Hat
Text\",\"RedHatText\",Arial,sans-serif); font-size:
var(\--rh-font-size-bod= y-text-md,1rem); height: 36px; padding: 0px
40px; width: 100%; } .input-search-box\[data-v-7ec4cdc4\]::placeholder {
color: light-dark(var(\--r=
h-color-text-secondary-on-light,#4d4d4d),var(\--rh-color-text-secondary-on-d=
ark,#c7c7c7)); } .input-clear-btn\[data-v-7ec4cdc4\] { align-items:
center; background-color: = transparent; border: none; display: flex;
height: 36px; justify-content: ce= nter; margin-right: -30px; outline:
none; transform: translate(-30px); }
.input-clear-btn\[data-v-7ec4cdc4\]:focus { border: 1px solid
var(\--rh-color-= accent-base-on-light,#06c); } .input-clear-btn:focus
.input-clear-icon\[data-v-7ec4cdc4\] { color: var(\--rh=
-color-canvas-black,#151515); } .input-clear-icon\[data-v-7ec4cdc4\] {
color: rgb(107, 110, 114); cursor: poi= nter; }
.input-clear-icon\[data-v-7ec4cdc4\]:hover { color:
var(\--rh-color-canvas-bla= ck,#151515); }
.form-submit-btn\[data-v-7ec4cdc4\]::part(button) { align-items: center;
back= ground-color:
light-dark(var(\--rh-color-surface-light,#e0e0e0),var(\--rh-col=
or-interactive-secondary-default-on-light,#4d4d4d)); border-radius: 0px;
di= splay: flex; height: 36px; justify-content: center;
\--\_default-border-color= : var(\--rh-color-gray-20,#e0e0e0); margin:
0px; } .form-submit-icon\[data-v-7ec4cdc4\] { color:
light-dark(#151515,var(\--rh-col= or-surface-light,#e0e0e0)); }
.input-close-btn\[data-v-7ec4cdc4\] { background: none; border: none;
cursor:= pointer; margin: 0 var(\--rh-space-lg,16px); }
.input-close-icon\[data-v-7ec4cdc4\] { color:
var(\--rh-color-white,#fff); } \@media (max-width: 992px) {
.form-box\[data-v-7ec4cdc4\] { gap: var(\--rh-space-md,8px); margin:
auto; w= idth: 100%; } .input-search-box\[data-v-7ec4cdc4\]::placeholder
{ font-family: var(\--rh-f= ont-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif); font-si= ze:
var(\--rh-font-size-body-text-md,1rem); font-weight:
var(\--rh-font-weigh= t-code-regular,400); line-height: 24px; }
.search-item-text-elipsis\[data-v-7ec4cdc4\] { max-width: 60%; } }
\@media (max-width: 767px) { .input-close-btn\[data-v-7ec4cdc4\] {
display: none; } .input-search-box\[data-v-7ec4cdc4\] { border-radius:
0px; } .input-clear-btn\[data-v-7ec4cdc4\] { margin-right: -42px;
transform: trans= late(-42px); } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-4554ea58-d77b-470a-acc6-121e7412bc29@mhtml.blink \@charset
\"utf-8\"; .status-legal .status-page-widget\[data-v-5f538988\] {
display: block; margin= : 0.5rem 0px; width: max-content; }
.status-page-widget\[data-v-5f538988\] { align-items: center; display:
flex; = flex-direction: row; } .status-legal .status-page-widget
.status-description\[data-v-5f538988\] { co= lor: rgb(204, 204, 204);
font-weight: 600; letter-spacing: 0.0125rem; line-= height: 1.5;
margin-right: 0.5rem; } .status-good\[data-v-5f538988\] {
background-color: rgb(62, 133, 54); }
.status-critical\[data-v-5f538988\] { background-color: rgb(163, 1, 0);
} .status-partial\[data-v-5f538988\] { background-color: rgb(245, 193,
45); } .status-maintentance\[data-v-5f538988\] { background-color:
rgb(49, 109, 193)= ; } .status-minor\[data-v-5f538988\] {
background-color: rgb(184, 92, 0); }
.status-description\[data-v-5f538988\] { color: rgb(204, 204, 204);
font-weig= ht: 500; letter-spacing: 0.2px; line-height: 1.5; }
.current-status-indicator\[data-v-5f538988\] { border-radius: 6px;
display: i= nline-block; height: 12px; margin: 0px 0px 0px 5px; width:
12px; } .current-status-indicator.small\[data-v-5f538988\] {
border-radius: 4px; disp= lay: inline-block; height: 8px; margin: 0px
0px 0px 5px; width: 8px; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-26823dad-2111-471f-bb56-9179b613589e@mhtml.blink \@charset
\"utf-8\"; :is(rh-footer, rh-footer-universal) a { color:
light-dark(var(\--rh-color-in=
teractive-primary-default-on-light,#06c),var(\--rh-color-interactive-primary=
-default-on-dark,#92c5f9)); text-decoration: none; } :is(rh-footer,
rh-footer-universal) a:hover { color: light-dark(var(\--rh-co=
lor-interactive-primary-hover-on-light,#036),var(\--rh-color-interactive-pri=
mary-hover-on-dark,#b9dafc)); text-decoration: underline; }
:is(rh-footer, rh-footer-universal) a:is(:focus, :focus-within) { color:
li=
ght-dark(var(\--rh-color-interactive-primary-hover-on-light,#036),var(\--rh-c=
olor-interactive-primary-hover-on-dark,#b9dafc)); text-decoration:
underlin= e; } :is(rh-footer, rh-footer-universal) a:visited { color:
light-dark(var(\--rh-=
color-interactive-primary-hover-on-light,#036),var(\--rh-color-interactive-p=
rimary-hover-on-dark,#b9dafc)); text-decoration: none; } :is(rh-footer,
rh-footer-universal) a\[slot\^=3D\"logo\"\] { display: block; }
:is(rh-footer) a\[slot\^=3D\"logo\"\] \> img { display: block; height:
var(\--rh-s= ize-icon-04,40px); width: auto; } :is(rh-footer,
rh-footer-universal) :is(h1, h2, h3, h4, h5, h6) { color: li=
ght-dark(var(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-text-=
primary-on-dark,#fff)); font-family:
var(\--rh-font-family-heading,RedHatDis= play,\"Red Hat
Display\",Helvetica,Arial,sans-serif); line-height: var(\--rh-l=
ine-height-heading,1.3); } rh-footer \[slot=3D\"links\"\]:is(h1, h2, h3,
h4, h5):nth-of-type(n+5) { \--\_lin= k-header-margin:
calc(var(\--rh-space-2xl, 32px) - var(\--rh-space-lg, 16px))= ; }
rh-footer \[slot\^=3D\"links\"\] a { gap:
var(\--rh-footer-links-gap,var(\--rh-spa= ce-md,8px)); } :is(rh-footer,
rh-footer-universal) \[slot\^=3D\"links\"\] li { display: content= s;
margin: 0px; padding: 0px; } :is(rh-footer, rh-footer-universal)
\[slot\^=3D\"links\"\] a { display: block; f= ont-size:
var(\--rh-footer-link-font-size,var(\--rh-font-size-body-text-sm,.8=
75rem)); width: fit-content; color:
light-dark(var(\--rh-color-text-primary-=
on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff))
!important; } rh-footer-universal \[slot\^=3D\"links\"\] a { font-size:
inherit; } :is(rh-footer, rh-footer-universal) {
\--rh-footer-section-side-gap: var(\--r= h-space-lg,16px); overflow-y:
auto; } :is(rh-footer, rh-footer-universal) \> :not(\[slot=3D\"logo\"\],
rh-footer-unive= rsal) { animation-delay: 0s; animation-duration: 5s;
animation-name: var(\--= \_fallback-animation,deopacitize-footer);
animation-timing-function: ease; o= pacity: var(\--\_fallback-opacity);
} \@media screen and (min-width: 768px) { :is(rh-footer,
rh-footer-universal) { \--rh-footer-section-side-gap: var(-=
-rh-space-2xl,32px); } } \@media screen and (min-width: 1440px) {
:is(rh-footer, rh-footer-universal) { \--rh-footer-section-side-gap:
var(-= -rh-space-4xl,64px); } } rh-footer:not(:defined) {
background-color: var(\--rh-color-surface-darker,#= 1f1f1f); display:
grid; grid-template-areas: \"footer\" \"global\"; grid-templa= te-rows:
1fr auto; min-height: var(\--rh-footer-nojs-min-height,750px); widt= h:
100%; } \@keyframes deopacitize-footer {=20 0% { \--\_fallback-opacity:
0; } 99% { \--\_fallback-opacity: 0; } 100% { \--\_fallback-opacity: 1;
} } rh-footer-universal:not(:defined) { background-color:
var(\--rh-color-surfac= e-darkest,#151515); display: block; min-height:
176px; width: 100%; } rh-footer-universal:not(:defined)::before {
grid-area: global; } rh-footer-universal rh-footer-copyright {
grid-column: -1 / 1; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-9b1ccd70-b89e-4848-8ac3-f13f01ca2dc2@mhtml.blink \@charset
\"utf-8\"; :is(rh-footer-block) a\[data-v-81a16915\] { text-decoration:
underline; } .reddit-span a img\[data-v-81a16915\] { transition: filter
0.3s; padding-bott= om: 3px !important; } .reddit-span a:hover
img\[data-v-81a16915\] { filter: brightness(0) saturate(= 100%)
invert(87%) sepia(0) saturate(0) hue-rotate(154deg) brightness(94%) c=
ontrast(84%); }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-4901e0e6-940f-4600-8807-6c753f6a5f44@mhtml.blink \@charset
\"utf-8\"; :host(\[size=3D\"sm\"\]) #container\[data-v-c6b48c1e\] {
\--\_size: var(\--pf-global= \--icon\--FontSize\--sm,12px); }
.content-wrapper\[data-v-c6b48c1e\] { background-color:
light-dark(var(\--rh-c=
olor-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
gap: 0= px; grid-template-columns: repeat(12, 1fr); height: auto;
margin: 0px auto;= min-height: 46vh; } .content\[data-v-c6b48c1e\] {
margin: 0 var(\--rh-space-lg,16px); } .line-below-chp\[data-v-c6b48c1e\]
{ border-right: 0px; border-bottom: 0px; b= order-left: 0px;
border-image: initial; border-top: .0625rem solid light-da=
rk(#d2d2d2,var(\--rh-color-border-subtle-on-dark,#707070)); margin:
var(\--rh= -space-xl,24px) 0 var(\--rh-space-3xl,48px); }
.docs-content-container\[data-v-c6b48c1e\] { font-size:
var(\--rh-font-size-bo= dy-text-lg,1.125rem); font-weight:
var(\--rh-font-weight-body-text-regular,4= 00); line-height: 1.6667;
padding-top: var(\--rh-space-xl,24px); }
.chapter-title\[data-v-c6b48c1e\] { font-family: \"Red Hat Display\"; }
h1.chapter-title\[data-v-c6b48c1e\] { margin: 0px; padding: 0px; }
.banner-wrapper\[data-v-c6b48c1e\] { padding: 0
var(\--rh-space-lg,16px); } .chapter .section
.simpara\[data-v-c6b48c1e\], .chapter .section p\[data-v-c6b= 48c1e\] {
font-family: \"Red Hat Text\"; font-size: var(\--rh-font-size-body-te=
xt-lg,1.125rem); font-weight:
var(\--rh-font-weight-body-text-regular,400); = line-height: 30px; }
.alert-section\[data-v-c6b48c1e\] { padding-bottom:
var(\--rh-space-2xl,32px);= } rh-alert\[data-v-c6b48c1e\] { width: auto;
} rh-back-to-top\[data-v-c6b48c1e\] { inset-block-end:
var(\--rh-space-lg,16px);= inset-inline-end: var(\--rh-space-lg,16px); }
.informaltable\[data-v-c6b48c1e\], .rhdocs
.informaltable\[data-v-c6b48c1e\], .= rhdocs
.table-contents\[data-v-c6b48c1e\], .rhdocs .table-wrapper\[data-v-c6b4=
8c1e\], .table-contents\[data-v-c6b48c1e\],
.table-wrapper\[data-v-c6b48c1e\] { = max-height:
var(\--rh-table\--maxHeight); overflow: auto; }
rh-table\[data-v-c6b48c1e\] { display: block; margin:
var(\--rh-space-2xl,32px= ) 0; max-width: 100%; }
.pvof-doc\_\_wrapper\[data-v-c6b48c1e\], .rhdocs\[data-v-c6b48c1e\] {
\--rh-table-= -maxHeight: calc(100vh - 12.5rem); }
.toc-filter\[data-v-c6b48c1e\] { display: none; }
.toc-filter-mobile\[data-v-c6b48c1e\] { padding:
var(\--rh-space-lg,16px); wid= th: 100%; } #text\[data-v-c6b48c1e\],
.toc-filter-mobile\[data-v-c6b48c1e\] { align-items: = center; display:
flex; } #text\[data-v-c6b48c1e\] { flex: 1 1 0%; flex-direction: row; }
#search-icon\[data-v-c6b48c1e\] { left: 2.5rem; position: absolute; top:
55%;= transform: translateY(-50%); z-index: 1; }
rh-icon\[data-v-c6b48c1e\] { \--rh-icon\--size: 16px; }
#text:focus-within #icon\[data-v-c6b48c1e\], #text:hover
#icon\[data-v-c6b48c1= e\] { color: rgb(21, 21, 21); }
#text\[data-v-c6b48c1e\]::after, #text\[data-v-c6b48c1e\]::before {
content: \"\"= ; inset: 0px; pointer-events: none; position: absolute; }
#text-input\[data-v-c6b48c1e\]:focus, #text-input:focus +
#utilities\[data-v-c= 6b48c1e\] { border-bottom: 2px solid rgb(0, 102,
204); outline: none; } #text-input\[data-v-c6b48c1e\] {
background-color: light-dark(var(\--rh-color-=
surface-lightest,#fff),var(\--rh-color-surface-darkest,#151515));
border-top= -color: ; border-top-style: ; border-top-width: ;
border-right-color: ; bor= der-right-style: ; border-right-width: ;
border-left-color: ; border-left-s= tyle: ; border-left-width: ;
border-image-source: ; border-image-slice: ; b= order-image-width: ;
border-image-outset: ; border-image-repeat: ; border-b= ottom: 1px solid
rgb(138, 141, 144); font-family: inherit; font-size: 100%;= grid-area:
text-input; line-height: 1.5; overflow: hidden; padding: 0.375r= em
0.25rem 0.375rem 0.5rem; position: relative; text-overflow: ellipsis;
wh= ite-space: nowrap; width: 100%; }
#text-input\[data-v-c6b48c1e\]::placeholder { color:
light-dark(#6a6e73,var(-= -rh-color-gray-30,#c7c7c7)); }
#utilities\[data-v-c6b48c1e\] { align-items: center; background-color:
light-=
dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darkest,#=
151515)); border-top-color: ; border-top-style: ; border-top-width: ;
borde= r-right-color: ; border-right-style: ; border-right-width: ;
border-image-s= ource: ; border-image-slice: ; border-image-width: ;
border-image-outset: ;= border-image-repeat: ; border-bottom: 1px solid
rgb(138, 141, 144); border= -left: 0px; display: flex; padding-bottom:
3px; padding-top: 3px; } #utilities rh-badge\[data-v-c6b48c1e\] {
border-radius: 80px; font-weight: va=
r(\--rh-font-weight-heading-medium,500); \--\_background-color: #e0e0e0;
} #clear-button\[data-v-c6b48c1e\], #utilities
rh-badge\[data-v-c6b48c1e\] { marg= in-right: var(\--rh-space-md,8px); }
#clear-button\[data-v-c6b48c1e\] { \--pf-c-button\--PaddingTop: .625rem;
\--pf-c= -button\--PaddingRight: .25rem; \--pf-c-button\--PaddingBottom:
.625rem; \--pf-= c-button\--PaddingLeft: .25rem; }
#text-input.no-right-border\[data-v-c6b48c1e\] { border-right: 0px; }
.focusable\[data-v-c6b48c1e\]:focus-visible { border: 2px solid
var(\--rh-colo= r-interactive-blue,#06c); }
.mobile-nav-wrapper\[data-v-c6b48c1e\] { align-items: center;
border-bottom: = 1px solid
light-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--r=
h-color-border-subtle-on-dark,#707070)); display: flex; height: auto;
justi= fy-content: space-between; padding: var(\--rh-space-sm,.5rem); }
.content-page-mobile-nav\[data-v-c6b48c1e\] { align-items: center;
background= -color:
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-sur=
face-darker,#1f1f1f)); min-height: 51px; position: sticky; top: 0px;
z-inde= x: 5; } .active-mobile-menu\[data-v-c6b48c1e\] { color:
light-dark(var(\--rh-color-gra=
y-95,#151515),var(\--rh-color-interactive-secondary-default-on-dark,#c7c7c7)=
); padding-left: 0.5rem; } .hidden\[data-v-c6b48c1e\] { display: none; }
.mobile-nav-btn\[data-v-c6b48c1e\] { background-color: transparent;
border: n= one; font-family: inherit; font-size: 0.875rem; font-weight:
500; margin: 0= px; min-height: 40px; min-width: 40px; }
.border-right\[data-v-c6b48c1e\] { border-right: 1px solid rgb(199, 199,
199)= ; } .product-container\[data-v-c6b48c1e\] { border-bottom: 1px
solid light-dark(v=
ar(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-=
on-dark,#707070)); padding: var(\--rh-space-2xl,32px)
var(\--rh-space-lg,16px= ); } .product-container
h1.product-title\[data-v-c6b48c1e\] { font-size: var(\--rh-=
font-size-code-xl,1.25rem); line-height: 30px; margin-bottom: 0px;
margin-t= op: 0px; } .product-container
.product-version\[data-v-c6b48c1e\] { align-items: center;= display:
flex; flex-wrap: wrap; margin-top: var(\--rh-space-lg,16px); }
.product-version .version-label\[data-v-c6b48c1e\] { font-family: \"Red
Hat Te= xt\"; font-size: var(\--rh-font-size-body-text-sm,.875rem);
font-weight: 500;= } .product-version
.version-select-dropdown\[data-v-c6b48c1e\] { margin: 0 var(=
\--rh-space-lg,16px); max-width: 9.75rem; min-height: 2rem; min-width:
3rem;= overflow: hidden; width: min-content; appearance: none;
background-size: ;= background-attachment: ; background-origin: ;
background-clip: ; backgroun= d-color: ; background-image:
var(\--select-dropdown-image); background-posit= ion: 85% 50%;
background-repeat: no-repeat; border-top-color: ; border-top-= style: ;
border-top-width: ; border-right-color: ; border-right-style: ; bo=
rder-right-width: ; border-left-color: ; border-left-style: ;
border-left-w= idth: ; border-image-source: ; border-image-slice: ;
border-image-width: ; = border-image-outset: ; border-image-repeat: ;
border-bottom: 0px; box-shado= w: 0 -1px 0 0
var(\--rh-color-gray-60,#4d4d4d) inset; cursor: pointer; font-= size:
var(\--rh-font-size-body-text-md,1rem); padding-top: ; padding-bottom:=
; padding-left: ; padding-right: var(\--rh-space-xl,24px);
text-overflow: e= llipsis; } pf-popover\[data-v-c6b48c1e\] { margin-top:
var(\--rh-space-md,8px); \--pf-c-po= pover\_\_arrow\--BackgroundColor:
var(\--rh-color-canvas-black,#151515); \--pf-c=
-popover\_\_content\--BackgroundColor: var(
\--rh-color-canvas-black,#151515 );= \--pf-c-popover\--BoxShadow: 0px
4px 8px 0px #15151540; \--pf-c-popover\_\_titl= e-text\--Color:
var(\--rh-color-white,#fff); \--pf-c-popover\--MaxWidth: 300px;=
\--pf-c-popover\--MinWidth: 300px; \--pf-c-popover\--c-button\--Top:
20px; \--pf= -c-popover\--c-button\--Right: 4px;
\--pf-c-button\--m-plain\--hover\--Color: var= (\--rh-color-white,#fff);
} pf-popover\[data-v-c6b48c1e\]::part(content) { padding:
var(\--rh-space-2xl,32= px); } pf-popover\[data-v-c6b48c1e\]::part(body)
{ margin-top: var(\--rh-space-lg,16p= x); }
pf-popover\[data-v-c6b48c1e\]::part(close-button) {
\--pf-c-button\--m-plain\--f= ocus\--Color:
var(\--rh-color-gray-30,#c7c7c7); \--pf-c-button\--m-plain\--Color= :
var(\--rh-color-gray-30,#c7c7c7); }
.popover-header-text\[data-v-c6b48c1e\] { color:
var(\--rh-color-white,#fff); = font-size:
var(\--rh-font-size-code-md,1rem); margin: 0px; max-width: 80%; p=
adding: 0px; } .popover-body-link\[data-v-c6b48c1e\] { color:
var(\--rh-color-blue-30,#92c5f9= ); text-decoration: none; }
.popover-trigger-btn\[data-v-c6b48c1e\] { align-items: center;
background: no= ne; border: none; cursor: pointer; display: flex;
justify-content: center; = } #first-button\[data-v-c6b48c1e\] { width:
80%; } #second-button\[data-v-c6b48c1e\] { text-align: right; width:
20%; } #toc-btn\[data-v-c6b48c1e\] { text-align: left; width: 100%; }
.toc-error\[data-v-c6b48c1e\] { margin: 0px; max-width: 100%; } #layout
label\[data-v-c6b48c1e\] { font-weight: 500; }
.page-layout-options\[data-v-c6b48c1e\] { display: flex; flex-direction:
colu= mn; max-width: 100%; padding-bottom: var(\--rh-space-lg,16px); }
.table-of-contents \> ol\[data-v-c6b48c1e\] { list-style: none; margin:
0px; p= adding: 0px; } nav.table-of-contents\[data-v-c6b48c1e\] {
z-index: 1; } nav.table-of-contents ol\[data-v-c6b48c1e\] { list-style:
none; margin: 0px; = padding: 0px; }
#mobile-browse-docs\[data-v-c6b48c1e\] { font-weight:
var(\--rh-font-weight-bo= dy-text-medium,500); padding-left:
var(\--rh-space-2xl,32px); }
#mobile-nav-content-wrapper\[data-v-c6b48c1e\] { border-bottom: 1px
solid lig=
ht-dark(var(\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-borde=
r-subtle-on-dark,#707070)); border-top: 1px solid
light-dark(var(\--rh-color=
-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-on-dark,#7070=
70)); } #page-content-options-mobile\[data-v-c6b48c1e\],
#toc-wrapper-mobile\[data-v-c= 6b48c1e\] { padding:
var(\--rh-space-md,8px); } nav#mobile-toc-menu\[data-v-c6b48c1e\] {
max-height: 50vh; overflow-y: scroll= ; }
rh-disclosure.jump-links-container\[data-v-c6b48c1e\] { margin:
var(\--rh-spac= e-xl,24px) var(\--rh-space-lg,16px) 0; }
.content-page-mobile-nav\[data-v-c6b48c1e\] { display: block;
transition: tra= nsform 0.3s ease-in-out; }
.hide-content-page-mobile-nav\[data-v-c6b48c1e\] { transform:
translateY(-100= %); transition: transform 0.3s ease-in-out; }
#breadcrumbs\[data-v-c6b48c1e\],
.content-format-selectors\[data-v-c6b48c1e\], =
.left-content\[data-v-c6b48c1e\], .tablet-jump-links\[data-v-c6b48c1e\],
.table= t-page-layout-options\[data-v-c6b48c1e\] { display: none; }
\@media (min-width: 768px) { .content\[data-v-c6b48c1e\] { margin: 0
var(\--rh-space-2xl,32px); }
rh-disclosure.jump-links-container\[data-v-c6b48c1e\] { margin:
var(\--rh-sp= ace-xl,24px) var(\--rh-space-2xl,32px) 0; } } \@media
(min-width: 992px) { #mobile-nav\[data-v-c6b48c1e\],
#toc-list-mobile\[data-v-c6b48c1e\] { display= : none; }
#breadcrumbs\[data-v-c6b48c1e\] { display: block; }
.content-wrapper\[data-v-c6b48c1e\] { grid-template-columns: repeat(2,
auto= ) repeat(10, 1fr); } .left-content\[data-v-c6b48c1e\] { display:
block; max-width: 320px; min-wi= dth: 320px; z-index: 6; }
.toc-container\[data-v-c6b48c1e\] { border-right: 1px solid
light-dark(var(=
\--rh-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-on-=
dark,#707070)); min-height: 100vh; position: sticky; top: 72px;
transition:= transform 0.3s ease-in-out; }
.toc-wrapper\[data-v-c6b48c1e\] { padding: 0px; }
.toc-focus-container\[data-v-c6b48c1e\] { position: sticky; top: 72px;
z-in= dex: 2; } .toc-focus-btn\[data-v-c6b48c1e\] { align-items: center;
background-color: =
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-dar=
ker,#1f1f1f)); border: 1px solid
light-dark(var(\--rh-color-border-interacti=
ve-on-light,#06c),var(\--rh-color-border-interactive-on-dark,#92c5f9));
bord= er-radius: 50%; cursor: pointer; display: flex; height: 40px;
justify-conte= nt: center; position: absolute; right: -20px; top: 15px;
width: 40px; } .toc-focus-btn\[data-v-c6b48c1e\]:focus-visible,
.toc-focus-btn\[data-v-c6b4= 8c1e\]:hover { background-color:
light-dark(var(\--rh-color-blue-10,#e0f0ff),=
var(\--rh-color-gray-70,#383838)); box-shadow: var(\--rh-box-shadow-sm,0
2px = 4px 0 hsla(0,0%,8%,.2)); }
.toc-focus-btn\[data-v-c6b48c1e\]:focus-visible { border: 2px solid
var(\--r= h-color-blue-50,#06c); }
.toc-focus-btn-icon\[data-v-c6b48c1e\] { color:
light-dark(var(\--rh-color-b=
lue-50,#06c),var(\--rh-color-blue-50,#92c5f9)); }
nav#toc\[data-v-c6b48c1e\] { height: auto; max-height:
var(\--toc-height,70v= h); overflow-y: auto; padding-bottom:
var(\--rh-space-2xl,32px); } .toc-filter\[data-v-c6b48c1e\] {
align-items: center; background-color: lig=
ht-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker=
,#1f1f1f)); display: flex; padding: var(\--rh-space-lg,16px)
var(\--rh-space-= 2xl,32px); position: sticky; top: 72px; width: 100%;
z-index: 1; } .product-container\[data-v-c6b48c1e\] { padding:
var(\--rh-space-xl,24px) va= r(\--rh-space-2xl,32px); }
.product-container.shrink-product-padding\[data-v-c6b48c1e\] { padding:
var= (\--rh-space-lg,16px); } .product-version
.version-select-dropdown\[data-v-c6b48c1e\] { margin: var(=
\--rh-space-md,8px) var(\--rh-space-sm,6px); }
.toc-filter\[data-v-c6b48c1e\] { display: block; }
#text-input\[data-v-c6b48c1e\] { padding: 0.375rem 0.25rem 0.375rem
2rem; } .page-layout-options\[data-v-c6b48c1e\] { max-width: 168px; }
.docs-content-container\[data-v-c6b48c1e\] { padding-top:
var(\--rh-space-3x= l,4rem); } .content\[data-v-c6b48c1e\] { margin: 0
var(\--rh-space-2xl,32px) 0 var(\--rh= -space-4xl,64px); max-width:
789px; } .expand-content\[data-v-c6b48c1e\] { max-width: 900px; }
.banner-wrapper\[data-v-c6b48c1e\] { padding: var(\--rh-space-3xl,48px)
var(= \--rh-space-6xl,96px) 0 var(\--rh-space-6xl,96px); }
.change-layout\[data-v-c6b48c1e\] { grid-template-columns: auto
repeat(11, = 1fr); } .collapse-left-content\[data-v-c6b48c1e\] {
max-width: 48px; min-width: 48p= x; }
.tablet-page-layout-options\[data-v-c6b48c1e\] { display: flex;
flex-direct= ion: column; max-width: 100%; padding-top:
var(\--rh-space-2xl,32px); } .tablet-jump-links\[data-v-c6b48c1e\] {
background-color: light-dark(var(\--=
rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
di= splay: flex; flex-direction: column; justify-content: flex-end;
position: s= ticky; top: 72px; z-index: 5; }
rh-disclosure.tablet-jump-links-container\[data-v-c6b48c1e\] {
margin-top: = var(\--rh-space-xl,24px); }
rh-back-to-top\[data-v-c6b48c1e\] { inset-inline-end:
var(\--rh-space-2xl,32= px); } \@keyframes slideaway-left-c6b48c1e {=20
0% { display: block; } 100% { opacity: 0; transform: translate(-40px); }
} \@keyframes slideaway-right-c6b48c1e {=20 0% { display: block; } 100%
{ opacity: 0; transform: translate(40px); } } \@keyframes
enter-left-c6b48c1e {=20 0% { display: none; transform:
translate(-40px); } 100% { opacity: 1; } } \@keyframes
enter-right-c6b48c1e {=20 0% { display: none; transform:
translate(40px); } 100% { opacity: 1; } } .hide-left\[data-v-c6b48c1e\]
{ animation: 0.2s ease 0s 1 normal none runni= ng
slideaway-left-c6b48c1e; display: none; } .enter-left\[data-v-c6b48c1e\]
{ animation: 0.3s ease 0s 1 normal none runn= ing enter-left-c6b48c1e;
border-right: none; display: block; } .enter-right\[data-v-c6b48c1e\] {
animation: 0.3s ease 0s 1 normal none run= ning enter-right-c6b48c1e;
display: block; } .hide-right\[data-v-c6b48c1e\] { animation: 0.2s ease
0s 1 normal none runn= ing slideaway-right-c6b48c1e; display: none; }
.toc-container.enter-toc-container-left\[data-v-c6b48c1e\] { transform:
tra= nslate(0px); } } \@media (min-width: 1100px) {
.expand-content\[data-v-c6b48c1e\] { margin: 0px auto; } } \@media
(min-width: 1200px) { .content\[data-v-c6b48c1e\] { margin: 0px auto; }
} \@media (min-width: 1440px) { .tablet-jump-links\[data-v-c6b48c1e\],
.tablet-page-layout-options\[data-v-c= 6b48c1e\] { display: none; }
.content-wrapper\[data-v-c6b48c1e\] { grid-template-columns: repeat(2,
auto= ) repeat(8, 1fr) repeat(2, auto); } .content\[data-v-c6b48c1e\] {
margin: 0 var(\--rh-space-4xl,64px); }
.expand-content\[data-v-c6b48c1e\] { margin: 0px auto; }
.change-layout\[data-v-c6b48c1e\] { grid-template-columns: auto
repeat(9, 1= fr) repeat(2, auto); }
.content-format-selectors\[data-v-c6b48c1e\] { color:
light-dark(var(\--rh-c=
olor-gray-95,#151515),var(\--rh-color-white,#fff)); display: block;
font-fam= ily: \"Red Hat Text\"; font-size:
var(\--rh-font-size-body-text-sm,.875rem); f= ont-weight:
var(\--rh-font-weight-body-text-medium,500); margin-right: var(-=
-rh-space-2xl,32px); max-width: 320px; min-width: 320px; padding-top:
var(-= -rh-space-2xl,32px); } summary\[data-v-c6b48c1e\] { cursor:
pointer; list-style: none; position: r= elative; }
summary\[data-v-c6b48c1e\]::-webkit-details-marker { display: none; }
details#jump-links-details .jump-links-heading\[data-v-c6b48c1e\] {
backgro= und-color:
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-=
surface-darker,#1f1f1f)); display: block; margin-top:
var(\--rh-space-lg,16p= x); padding: var(\--rh-space-lg,16px) 0 0
var(\--rh-space-xl,24px); position:= sticky; top: 72px; }
details#jump-links-details
.jump-links-heading\[data-v-c6b48c1e\]::before {= border-right: 3px
solid light-dark(var(\--rh-color-border-strong-on-light,#=
151515),var(\--rh-color-border-strong-on-dark,#fff)); border-top: 3px
solid =
light-dark(var(\--rh-color-border-strong-on-light,#151515),var(\--rh-color-bo=
rder-strong-on-dark,#fff)); color: var(\--rh-color-gray-95,#151515);
content= : \"\"; display: flex; height: 9px; left: 2px; position:
absolute; top: 26px;= transform: rotate(-135deg); width: 9px; }
details#jump-links-details\[open\]
.jump-links-heading\[data-v-c6b48c1e\]::be= fore { transform:
rotate(135deg); } .page-layout-sticky\[data-v-c6b48c1e\] { position:
sticky; top: 77px; } } \@media (min-width: 1600px) {
.content\[data-v-c6b48c1e\] { margin: 0px auto; } } \@media (min-width:
1920px) { .content-format-selectors\[data-v-c6b48c1e\] { margin-right:
var(\--rh-space= -4xl,64px); } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-512ac9a6-1fd9-4fd7-857d-f8fe1bfee729@mhtml.blink \@charset
\"utf-8\"; .element-invisible, .sr-only, .visually-hidden { height: 1px;
overflow: hid= den; padding: 0px; position: absolute; width: 1px; clip:
rect(0px, 0px, 0px= , 0px); border: 0px; white-space: nowrap; }
\@keyframes reveal-nav {=20 0% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); opacity: 0;=
visibility: hidden; } 99% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); } 100% { max-height:
9999em; opacity: 1; visibility: visible; } } \@keyframes
reveal-nav-parts {=20 0% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); opacity: 0;=
visibility: hidden; } 1% { visibility: visible; } 99% { max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); } 100% { max-height:
9999em; opacity: 1; visibility: visible; } } \@media print {
.pfe-navigation\_\_menu, pfe-navigation \[slot\] { display: none
!important; = } } pfe-navigation { \--pfe-broadcasted\--text:
var(\--pfe-theme\--color\--text,#151= 515);
\--pfe-broadcasted\--text\--muted:
var(\--pfe-theme\--color\--text\--muted,#= 6a6e73);
\--pfe-broadcasted\--link: var(\--pfe-theme\--color\--link,#06c);
\--pfe= -broadcasted\--link\--hover:
var(\--pfe-theme\--color\--link\--hover,#004080); \--=
pfe-broadcasted\--link\--focus:
var(\--pfe-theme\--color\--link\--focus,#004080);=
\--pfe-broadcasted\--link\--visited:
var(\--pfe-theme\--color\--link\--visited,#6= 753ac);
\--pfe-broadcasted\--link-decoration: var(\--pfe-theme\--link-decoratio=
n,none); \--pfe-broadcasted\--link-decoration\--hover:
var(\--pfe-theme\--link-d= ecoration\--hover,underline);
\--pfe-broadcasted\--link-decoration\--focus: var=
(\--pfe-theme\--link-decoration\--focus,underline);
\--pfe-broadcasted\--link-de= coration\--visited:
var(\--pfe-theme\--link-decoration\--visited,none); } \@supports
(display:grid) { pfe-navigation { animation: 0.1618s ease 4s 1 normal
forwards running rev= eal-nav; max-height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); } pfe-navigation \> \*
{ animation: 0.1618s ease 4s 1 normal forwards running=
reveal-nav-parts; opacity: 0; transition: opacity
var(\--pfe-reveal-duratio= n,.1618s) ease-in-out; visibility: hidden; }
} pfe-navigation.pfe-navigation\--processed,
pfe-navigation.pfe-navigation\--pr= ocessed \> \* { animation: auto ease
0s 1 normal none running none; opacity: = 1; visibility: visible; }
pfe-navigation pfe-primary-detail { display: none; }
pfe-navigation\[pfelement\] { display: block; } pfe-navigation-dropdown
{ color: var(\--pfe-navigation\_\_dropdown\--Color,#151= 515); }
#pfe-navigation\[breakpoint=3D\"desktop\"\]
.hidden-at-desktop\[class\]\[class\]\[cl= ass\],
#pfe-navigation\[breakpoint=3D\"mobile\"\]
.hidden-at-mobile\[class\]\[class= \]\[class\],
#pfe-navigation\[breakpoint=3D\"tablet\"\]
.hidden-at-tablet\[class\]\[c= lass\]\[class\],
pfe-navigation\[breakpoint=3D\"desktop\"\] .hidden-at-desktop\[cla=
ss\]\[class\]\[class\], pfe-navigation\[breakpoint=3D\"mobile\"\]
.hidden-at-mobile\[= class\]\[class\]\[class\],
pfe-navigation\[breakpoint=3D\"tablet\"\] .hidden-at-tabl=
et\[class\]\[class\]\[class\] { display: none; } #pfe-navigation,
#pfe-navigation \*, pfe-navigation, pfe-navigation \* { box-= sizing:
border-box; } #pfe-navigation \[pfelement\]
.pfe-navigation\_\_log-in-link, pfe-navigation \[p= felement\]
.pfe-navigation\_\_log-in-link { display: none; } #pfe-navigation,
pfe-navigation { align-items: stretch; background: var(\--p=
fe-navigation\_\_nav-bar\--Background,#151515); color:
var(\--pfe-navigation\_\_n=
av-bar\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
displa= y: flex; font-family: var(\--pfe-navigation\--FontFamily,Red Hat
Text,RedHatT= ext,Arial,Helvetica,sans-serif); font-size:
var(\--pf-global\--FontSize\--md,1= rem); height: auto; line-height:
1.5; margin: 0px; max-width: 9999em; min-h= eight:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); padding: 0px 16px;
posi= tion: relative; z-index:
var(\--pfe-navigation\--ZIndex,var(\--pfe-theme\--zind=
ex\--navigation,95)); } \@media (min-width: 768px) { #pfe-navigation,
pfe-navigation { flex-wrap: wrap; margin: 0px; max-width= : 9999em;
padding: 0px 16px; } } \@media (min-width: 1200px) { #pfe-navigation,
pfe-navigation { margin: 0px auto; padding: 0px 32px; } }
#pfe-navigation .pfe-navigation\_\_dropdown, #pfe-navigation
pfe-navigation-d= ropdown, pfe-navigation .pfe-navigation\_\_dropdown,
pfe-navigation pfe-navig= ation-dropdown { display: none; }
#pfe-navigation \> \[slot=3D\"account\"\], #pfe-navigation \>
\[slot=3D\"search\"\], = #pfe-navigation \>
\[slot=3D\"secondary-links\"\], pfe-navigation \> \[slot=3D\"acc=
ount\"\], pfe-navigation \> \[slot=3D\"search\"\], pfe-navigation \>
\[slot=3D\"secon= dary-links\"\] { height: 0px; overflow: hidden;
visibility: hidden; width: 0p= x; } \@media (min-width: 768px) {
#pfe-navigation nav.pfe-navigation, pfe-navigation nav.pfe-navigation {
a= lign-items: stretch; display: flex; flex-wrap: wrap; } } \@media
(min-width: 992px) { #pfe-navigation nav.pfe-navigation, pfe-navigation
nav.pfe-navigation { f= lex-wrap: nowrap; } } #pfe-navigation
.pfe-navigation\_\_logo-wrapper, pfe-navigation .pfe-navigati=
on\_\_logo-wrapper { align-items: center; display: flex;
justify-content: fle= x-start; margin: 0px; min-width: 150px; padding:
10px 16px 10px 0px; } \@media (min-width: 768px) {
.pfe-navigation\--no-main-menu #pfe-navigation
.pfe-navigation\_\_logo-wrapp= er, .pfe-navigation\--no-main-menu
pfe-navigation .pfe-navigation\_\_logo-wrap= per { margin-right: auto; }
} .pfe-navigation\--collapse-secondary-links
.pfe-navigation\--no-main-menu #pf= e-navigation
.pfe-navigation\_\_logo-wrapper, .pfe-navigation\--collapse-secon=
dary-links .pfe-navigation\--no-main-menu pfe-navigation
.pfe-navigation\_\_lo= go-wrapper { margin-right: 0px; } #pfe-navigation
.pfe-navigation\_\_logo-link, pfe-navigation .pfe-navigation\_=
\_logo-link { border-radius: 3px; display: block; margin-left: -8px;
outline= : 0px; padding: 6px 8px; position: relative; } #pfe-navigation
.pfe-navigation\_\_logo-link:focus, pfe-navigation .pfe-navig=
ation\_\_logo-link:focus { outline: 0px; } #pfe-navigation
.pfe-navigation\_\_logo-link:focus::after, pfe-navigation .pf=
e-navigation\_\_logo-link:focus::after { border: 1px dashed rgb(255,
255, 255= ); inset: 0px; content: \"\"; display: block; position:
absolute; } #pfe-navigation .pfe-navigation\_\_logo-image,
pfe-navigation .pfe-navigation= \_\_logo-image { display: block; height:
auto; width: 100%; } \@media (min-width: 576px) { #pfe-navigation
.pfe-navigation\_\_logo-image, pfe-navigation .pfe-navigati=
on\_\_logo-image { height: var(\--pfe-navigation\_\_logo\--height,40px);
width: a= uto; } } \@media print { #pfe-navigation
.pfe-navigation\_\_logo-image, pfe-navigation .pfe-navigati=
on\_\_logo-image { display: none; } } #pfe-navigation
.pfe-navigation\_\_logo-image:only-child, pfe-navigation .pfe=
-navigation\_\_logo-image:only-child { display: block; } \@media
(min-width: 576px) { #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--s= mall,
pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image= \--small {
height: var(\--pfe-navigation\_\_logo\--height,32px); } } \@media print
{ #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--s= creen,
pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-imag= e\--screen {
display: none !important; } } \@media screen { #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--p= rint,
pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image= \--print {
display: none !important; } } #pfe-navigation
.pfe-navigation\_\_logo-image.pfe-navigation\_\_logo-image\--scr=
een.pfe-navigation\_\_logo-image\--print, pfe-navigation
.pfe-navigation\_\_logo=
-image.pfe-navigation\_\_logo-image\--screen.pfe-navigation\_\_logo-image\--print=
{ display: inline-block !important; } #pfe-navigation
.pfe-navigation\_\_fallback-links a, #pfe-navigation .pfe-nav=
igation\_\_log-in-link, #pfe-navigation .pfe-navigation\_\_menu-link,
#pfe-navi= gation .pfe-navigation\_\_secondary-link, pfe-navigation
.pfe-navigation\_\_fal= lback-links a, pfe-navigation
.pfe-navigation\_\_log-in-link, pfe-navigation =
.pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-link = { \--pfe-icon\--color:
var(\--pfe-navigation\_\_dropdown\--link\--Color,var(\--pfe-=
theme\--color\--link,#06c)); align-items: center; appearance: none;
backgroun= d: 0px 0px; border: 0px; color:
var(\--pfe-navigation\_\_nav-bar\--Color\--defau=
lt,var(\--pfe-theme\--color\--ui-base\--text,#fff)); cursor: pointer;
display: = flex; font-family: inherit; font-size:
var(\--pf-global\--FontSize\--md,1rem);= justify-content: center;
margin: 0px; outline: 0px; padding: 8px 24px; pos= ition: relative;
text-align: center; text-decoration: none; white-space: no= wrap; width:
100%; } \@media print { #pfe-navigation
.pfe-navigation\_\_fallback-links a, #pfe-navigation .pfe-n=
avigation\_\_log-in-link, #pfe-navigation .pfe-navigation\_\_menu-link,
#pfe-na= vigation .pfe-navigation\_\_secondary-link, pfe-navigation
.pfe-navigation\_\_f= allback-links a, pfe-navigation
.pfe-navigation\_\_log-in-link, pfe-navigatio= n
.pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-lin= k { display: none !important; } }
\@media (min-width: 768px) { #pfe-navigation
.pfe-navigation\_\_fallback-links a, #pfe-navigation .pfe-n=
avigation\_\_log-in-link, #pfe-navigation .pfe-navigation\_\_menu-link,
#pfe-na= vigation .pfe-navigation\_\_secondary-link, pfe-navigation
.pfe-navigation\_\_f= allback-links a, pfe-navigation
.pfe-navigation\_\_log-in-link, pfe-navigatio= n
.pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-lin= k { \--pfe-icon\--color:
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var(\--=
pfe-theme\--color\--ui-base\--text,#fff)); color:
var(\--pfe-navigation\_\_nav-ba=
r\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
display: fl= ex; flex-direction: column; font-size:
var(\--pfe-navigation\--FontSize\--xs,1= 2px); height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); justify-content:=
flex-end; padding: 14px 8px; width: auto; } \@supports (display:grid) {
#pfe-navigation .pfe-navigation\_\_fallback-links a, #pfe-navigation
.pfe-n= avigation\_\_log-in-link, #pfe-navigation
.pfe-navigation\_\_menu-link, #pfe-na= vigation
.pfe-navigation\_\_secondary-link, pfe-navigation .pfe-navigation\_\_f=
allback-links a, pfe-navigation .pfe-navigation\_\_log-in-link,
pfe-navigatio= n .pfe-navigation\_\_menu-link, pfe-navigation
.pfe-navigation\_\_secondary-lin= k { place-items: center; display:
grid; grid-template-rows: 26px 18px; } } #pfe-navigation
.pfe-navigation\_\_fallback-links a\[class\]:focus, #pfe-navi= gation
.pfe-navigation\_\_fallback-links a\[class\]:hover, #pfe-navigation
.pfe= -navigation\_\_log-in-link\[class\]:focus, #pfe-navigation
.pfe-navigation\_\_log= -in-link\[class\]:hover, #pfe-navigation
.pfe-navigation\_\_menu-link\[class\]:fo= cus, #pfe-navigation
.pfe-navigation\_\_menu-link\[class\]:hover, #pfe-navigati= on
.pfe-navigation\_\_secondary-link\[class\]:focus, #pfe-navigation
.pfe-navig= ation\_\_secondary-link\[class\]:hover, pfe-navigation
.pfe-navigation\_\_fallbac= k-links a\[class\]:focus, pfe-navigation
.pfe-navigation\_\_fallback-links a\[cl= ass\]:hover, pfe-navigation
.pfe-navigation\_\_log-in-link\[class\]:focus, pfe-n= avigation
.pfe-navigation\_\_log-in-link\[class\]:hover, pfe-navigation .pfe-na=
vigation\_\_menu-link\[class\]:focus, pfe-navigation
.pfe-navigation\_\_menu-link= \[class\]:hover, pfe-navigation
.pfe-navigation\_\_secondary-link\[class\]:focus,= pfe-navigation
.pfe-navigation\_\_secondary-link\[class\]:hover { box-shadow: = inset 0
4px 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-th=
eme\--color\--ui-accent,#06c)); } } #pfe-navigation
.pfe-navigation\_\_fallback-links a:focus, #pfe-navigation .p=
fe-navigation\_\_fallback-links a:hover, #pfe-navigation
.pfe-navigation\_\_log= -in-link:focus, #pfe-navigation
.pfe-navigation\_\_log-in-link:hover, #pfe-na= vigation
.pfe-navigation\_\_menu-link:focus, #pfe-navigation .pfe-navigation\_=
\_menu-link:hover, #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, #p= fe-navigation
.pfe-navigation\_\_secondary-link:hover, pfe-navigation .pfe-na=
vigation\_\_fallback-links a:focus, pfe-navigation
.pfe-navigation\_\_fallback-= links a:hover, pfe-navigation
.pfe-navigation\_\_log-in-link:focus, pfe-navig= ation
.pfe-navigation\_\_log-in-link:hover, pfe-navigation
.pfe-navigation\_\_m= enu-link:focus, pfe-navigation
.pfe-navigation\_\_menu-link:hover, pfe-naviga= tion
.pfe-navigation\_\_secondary-link:focus, pfe-navigation
.pfe-navigation\_= \_secondary-link:hover { box-shadow: inset 4px 0 0 0
var(\--pfe-navigation\_\_n=
av-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c)); }
\@media (min-width: 768px) { #pfe-navigation
.pfe-navigation\_\_fallback-links a:focus, #pfe-navigation =
.pfe-navigation\_\_fallback-links a:hover, #pfe-navigation
.pfe-navigation\_\_l= og-in-link:focus, #pfe-navigation
.pfe-navigation\_\_log-in-link:hover, #pfe-= navigation
.pfe-navigation\_\_menu-link:focus, #pfe-navigation .pfe-navigatio=
n\_\_menu-link:hover, #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, = #pfe-navigation
.pfe-navigation\_\_secondary-link:hover, pfe-navigation .pfe-=
navigation\_\_fallback-links a:focus, pfe-navigation
.pfe-navigation\_\_fallbac= k-links a:hover, pfe-navigation
.pfe-navigation\_\_log-in-link:focus, pfe-nav= igation
.pfe-navigation\_\_log-in-link:hover, pfe-navigation .pfe-navigation\_=
\_menu-link:focus, pfe-navigation .pfe-navigation\_\_menu-link:hover,
pfe-navi= gation .pfe-navigation\_\_secondary-link:focus, pfe-navigation
.pfe-navigatio= n\_\_secondary-link:hover { box-shadow: inset 0 4px 0 0
var(\--pfe-navigation\_=
\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c));
} } .pfe-navigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_= fallback-links a:focus,
.pfe-navigation\--collapse-secondary-links #pfe-navi= gation
.pfe-navigation\_\_fallback-links a:hover, .pfe-navigation\--collapse-s=
econdary-links #pfe-navigation .pfe-navigation\_\_log-in-link:focus,
.pfe-nav= igation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_log-in-l= ink:hover,
.pfe-navigation\--collapse-secondary-links #pfe-navigation .pfe-n=
avigation\_\_menu-link:focus, .pfe-navigation\--collapse-secondary-links
#pfe-= navigation .pfe-navigation\_\_menu-link:hover,
.pfe-navigation\--collapse-seco= ndary-links #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, .pfe-nav=
igation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_secondar= y-link:hover,
.pfe-navigation\--collapse-secondary-links pfe-navigation .pfe=
-navigation\_\_fallback-links a:focus,
.pfe-navigation\--collapse-secondary-li= nks pfe-navigation
.pfe-navigation\_\_fallback-links a:hover, .pfe-navigation=
\--collapse-secondary-links pfe-navigation
.pfe-navigation\_\_log-in-link:focu= s,
.pfe-navigation\--collapse-secondary-links pfe-navigation
.pfe-navigation= \_\_log-in-link:hover,
.pfe-navigation\--collapse-secondary-links pfe-navigati= on
.pfe-navigation\_\_menu-link:focus,
.pfe-navigation\--collapse-secondary-li= nks pfe-navigation
.pfe-navigation\_\_menu-link:hover, .pfe-navigation\--colla=
pse-secondary-links pfe-navigation
.pfe-navigation\_\_secondary-link:focus, .=
pfe-navigation\--collapse-secondary-links pfe-navigation
.pfe-navigation\_\_se= condary-link:hover { box-shadow: inset 4px 0 0 0
var(\--pfe-navigation\_\_nav-=
bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c)); }
#pfe-navigation .pfe-navigation\_\_fallback-links a:focus,
#pfe-navigation .p= fe-navigation\_\_log-in-link:focus, #pfe-navigation
.pfe-navigation\_\_menu-lin= k:focus, #pfe-navigation
.pfe-navigation\_\_secondary-link:focus, pfe-navigat= ion
.pfe-navigation\_\_fallback-links a:focus, pfe-navigation
.pfe-navigation= \_\_log-in-link:focus, pfe-navigation
.pfe-navigation\_\_menu-link:focus, pfe-n= avigation
.pfe-navigation\_\_secondary-link:focus { outline: 0px; }
#pfe-navigation .pfe-navigation\_\_fallback-links a:focus::after,
#pfe-naviga= tion .pfe-navigation\_\_log-in-link:focus::after,
#pfe-navigation .pfe-naviga= tion\_\_menu-link:focus::after,
#pfe-navigation .pfe-navigation\_\_secondary-li= nk:focus::after,
pfe-navigation .pfe-navigation\_\_fallback-links a:focus::af= ter,
pfe-navigation .pfe-navigation\_\_log-in-link:focus::after,
pfe-navigati= on .pfe-navigation\_\_menu-link:focus::after,
pfe-navigation .pfe-navigation\_= \_secondary-link:focus::after {
border: 1px dashed; inset: 0px; content: \"\";= display: block;
position: absolute; } #pfe-navigation .pfe-navigation\_\_fallback-links
a pfe-icon, #pfe-navigation= .pfe-navigation\_\_log-in-link pfe-icon,
#pfe-navigation .pfe-navigation\_\_me= nu-link pfe-icon, #pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon,= pfe-navigation
.pfe-navigation\_\_fallback-links a pfe-icon, pfe-navigation =
.pfe-navigation\_\_log-in-link pfe-icon, pfe-navigation
.pfe-navigation\_\_menu= -link pfe-icon, pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon { p= ointer-events: none; }
#pfe-navigation .pfe-navigation\_\_fallback-links a
.secondary-link\_\_icon-wra= pper, #pfe-navigation
.pfe-navigation\_\_fallback-links a \> pfe-icon, #pfe-na= vigation
.pfe-navigation\_\_log-in-link .secondary-link\_\_icon-wrapper, #pfe-n=
avigation .pfe-navigation\_\_log-in-link \> pfe-icon, #pfe-navigation
.pfe-nav= igation\_\_menu-link .secondary-link\_\_icon-wrapper,
#pfe-navigation .pfe-navi= gation\_\_menu-link \> pfe-icon,
#pfe-navigation .pfe-navigation\_\_secondary-li= nk
.secondary-link\_\_icon-wrapper, #pfe-navigation
.pfe-navigation\_\_secondar= y-link \> pfe-icon, pfe-navigation
.pfe-navigation\_\_fallback-links a .second= ary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigation\_\_fallback-links a \> = pfe-icon,
pfe-navigation .pfe-navigation\_\_log-in-link .secondary-link\_\_icon=
-wrapper, pfe-navigation .pfe-navigation\_\_log-in-link \> pfe-icon,
pfe-navig= ation .pfe-navigation\_\_menu-link
.secondary-link\_\_icon-wrapper, pfe-navigat= ion
.pfe-navigation\_\_menu-link \> pfe-icon, pfe-navigation
.pfe-navigation\_\_= secondary-link .secondary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigatio= n\_\_secondary-link \> pfe-icon {
\--pfe-icon\--size: 18px; padding-right: 5px; = } \@media (min-width:
768px) { #pfe-navigation .pfe-navigation\_\_fallback-links a
.secondary-link\_\_icon-w= rapper, #pfe-navigation
.pfe-navigation\_\_fallback-links a \> pfe-icon, #pfe-= navigation
.pfe-navigation\_\_log-in-link .secondary-link\_\_icon-wrapper, #pfe=
-navigation .pfe-navigation\_\_log-in-link \> pfe-icon, #pfe-navigation
.pfe-n= avigation\_\_menu-link .secondary-link\_\_icon-wrapper,
#pfe-navigation .pfe-na= vigation\_\_menu-link \> pfe-icon,
#pfe-navigation .pfe-navigation\_\_secondary-= link
.secondary-link\_\_icon-wrapper, #pfe-navigation
.pfe-navigation\_\_second= ary-link \> pfe-icon, pfe-navigation
.pfe-navigation\_\_fallback-links a .seco= ndary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigation\_\_fallback-links a = \> pfe-icon,
pfe-navigation .pfe-navigation\_\_log-in-link .secondary-link\_\_ic=
on-wrapper, pfe-navigation .pfe-navigation\_\_log-in-link \> pfe-icon,
pfe-nav= igation .pfe-navigation\_\_menu-link
.secondary-link\_\_icon-wrapper, pfe-navig= ation
.pfe-navigation\_\_menu-link \> pfe-icon, pfe-navigation
.pfe-navigation= \_\_secondary-link .secondary-link\_\_icon-wrapper,
pfe-navigation .pfe-navigat= ion\_\_secondary-link \> pfe-icon {
padding: 2px 0px 4px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation .pfe-navigation\_\_= fallback-links a
.secondary-link\_\_icon-wrapper, .pfe-navigation\--collapse-s=
econdary-links #pfe-navigation .pfe-navigation\_\_fallback-links a \>
pfe-icon= , .pfe-navigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation= \_\_log-in-link .secondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-seco= ndary-links #pfe-navigation
.pfe-navigation\_\_log-in-link \> pfe-icon, .pfe-n=
avigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_menu-l= ink .secondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-link= s #pfe-navigation
.pfe-navigation\_\_menu-link \> pfe-icon, .pfe-navigation\--c=
ollapse-secondary-links #pfe-navigation
.pfe-navigation\_\_secondary-link .se= condary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links #pfe-= navigation
.pfe-navigation\_\_secondary-link \> pfe-icon, .pfe-navigation\--col=
lapse-secondary-links pfe-navigation .pfe-navigation\_\_fallback-links a
.sec= ondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-na= vigation
.pfe-navigation\_\_fallback-links a \> pfe-icon, .pfe-navigation\--col=
lapse-secondary-links pfe-navigation .pfe-navigation\_\_log-in-link
.secondar= y-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-navigat= ion
.pfe-navigation\_\_log-in-link \> pfe-icon,
.pfe-navigation\--collapse-seco= ndary-links pfe-navigation
.pfe-navigation\_\_menu-link .secondary-link\_\_icon= -wrapper,
.pfe-navigation\--collapse-secondary-links pfe-navigation .pfe-nav=
igation\_\_menu-link \> pfe-icon,
.pfe-navigation\--collapse-secondary-links pf= e-navigation
.pfe-navigation\_\_secondary-link .secondary-link\_\_icon-wrapper,=
.pfe-navigation\--collapse-secondary-links pfe-navigation
.pfe-navigation\_\_= secondary-link \> pfe-icon { padding: 0px 16px 0px
0px; } #pfe-navigation .pfe-navigation\_\_fallback-links a pfe-icon,
#pfe-navigation= .pfe-navigation\_\_log-in-link pfe-icon,
#pfe-navigation .pfe-navigation\_\_me= nu-link pfe-icon, #pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon,= pfe-navigation
.pfe-navigation\_\_fallback-links a pfe-icon, pfe-navigation =
.pfe-navigation\_\_log-in-link pfe-icon, pfe-navigation
.pfe-navigation\_\_menu= -link pfe-icon, pfe-navigation
.pfe-navigation\_\_secondary-link pfe-icon { d= isplay: block; height:
18px; } #pfe-navigation .pfe-navigation\_\_fallback-links a\[class\],
#pfe-navigation .= pfe-navigation\_\_fallback-links a\[href\],
#pfe-navigation .pfe-navigation\_\_lo= g-in-link\[class\],
#pfe-navigation .pfe-navigation\_\_log-in-link\[href\], #pfe-=
navigation .pfe-navigation\_\_menu-link\[class\], #pfe-navigation
.pfe-navigati= on\_\_menu-link\[href\], #pfe-navigation
.pfe-navigation\_\_secondary-link\[class\]= , #pfe-navigation
.pfe-navigation\_\_secondary-link\[href\], pfe-navigation .pf=
e-navigation\_\_fallback-links a\[class\], pfe-navigation
.pfe-navigation\_\_fall= back-links a\[href\], pfe-navigation
.pfe-navigation\_\_log-in-link\[class\], pfe= -navigation
.pfe-navigation\_\_log-in-link\[href\], pfe-navigation .pfe-navigat=
ion\_\_menu-link\[class\], pfe-navigation
.pfe-navigation\_\_menu-link\[href\], pfe= -navigation
.pfe-navigation\_\_secondary-link\[class\], pfe-navigation .pfe-nav=
igation\_\_secondary-link\[href\] { align-items: center;
justify-content: cente= r; } #pfe-navigation
.pfe-navigation\_\_account-toggle, #pfe-navigation \[slot=3D\"a=
ccount\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-nav= igation
\[slot=3D\"account\"\] \> a\[href\] { align-items: center; appearance:
non= e; background: 0px 0px; border: 0px; cursor: pointer; font-family:
inherit;= margin: 0px; outline: 0px; position: relative; text-align:
center; text-de= coration: none; white-space: nowrap;
\--pfe-icon\--color: var(\--pfe-navigatio=
n\_\_nav-bar\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
co= lor:
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var(\--pfe-theme\--color\--=
ui-base\--text,#fff)); display: flex; flex-direction: column; font-size:
var= (\--pfe-navigation\--FontSize\--xs,12px); height:
var(\--pfe-navigation\_\_nav-ba= r\--Height,72px); justify-content:
flex-end; padding: 14px 8px; width: auto;= } \@media print {
#pfe-navigation .pfe-navigation\_\_account-toggle, #pfe-navigation
\[slot=3D= \"account\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-n= avigation
\[slot=3D\"account\"\] \> a\[href\] { display: none !important; } }
#pfe-navigation .pfe-navigation\_\_account-toggle:focus, #pfe-navigation
.pfe= -navigation\_\_account-toggle:hover, #pfe-navigation
\[slot=3D\"account\"\] \> a\[h= ref\]:focus, #pfe-navigation
\[slot=3D\"account\"\] \> a\[href\]:hover, pfe-navigat= ion
.pfe-navigation\_\_account-toggle:focus, pfe-navigation
.pfe-navigation\_\_= account-toggle:hover, pfe-navigation
\[slot=3D\"account\"\] \> a\[href\]:focus, pf= e-navigation
\[slot=3D\"account\"\] \> a\[href\]:hover { box-shadow: inset 4px 0 0= 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--u=
i-accent,#06c)); } #pfe-navigation
.pfe-navigation\_\_account-toggle:focus, #pfe-navigation \[slo=
t=3D\"account\"\] \> a\[href\]:focus, pfe-navigation
.pfe-navigation\_\_account-tog= gle:focus, pfe-navigation
\[slot=3D\"account\"\] \> a\[href\]:focus { outline: 0px= ; }
#pfe-navigation .pfe-navigation\_\_account-toggle:focus::after,
#pfe-navigati= on \[slot=3D\"account\"\] \> a\[href\]:focus::after,
pfe-navigation .pfe-navigatio= n\_\_account-toggle:focus::after,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\]= :focus::after {
border: 1px dashed; inset: 0px; content: \"\"; display: block= ;
position: absolute; } #pfe-navigation .pfe-navigation\_\_account-toggle
pfe-icon, #pfe-navigation \[= slot=3D\"account\"\] \> a\[href\]
pfe-icon, pfe-navigation .pfe-navigation\_\_accou= nt-toggle pfe-icon,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\] pfe-icon { =
pointer-events: none; } \@supports (display:grid) { #pfe-navigation
.pfe-navigation\_\_account-toggle, #pfe-navigation \[slot=3D=
\"account\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-n= avigation
\[slot=3D\"account\"\] \> a\[href\] { place-items: center; display:
grid= ; grid-template-rows: 26px 18px; } } #pfe-navigation
.pfe-navigation\_\_account-toggle\[class\]:focus, #pfe-navigati= on
.pfe-navigation\_\_account-toggle\[class\]:hover, #pfe-navigation
\[slot=3D\"a= ccount\"\] \> a\[href\]\[class\]:focus, #pfe-navigation
\[slot=3D\"account\"\] \> a\[hre= f\]\[class\]:hover, pfe-navigation
.pfe-navigation\_\_account-toggle\[class\]:focu= s, pfe-navigation
.pfe-navigation\_\_account-toggle\[class\]:hover, pfe-navigat= ion
\[slot=3D\"account\"\] \> a\[href\]\[class\]:focus, pfe-navigation
\[slot=3D\"acco= unt\"\] \> a\[href\]\[class\]:hover { box-shadow: inset
0 4px 0 0 var(\--pfe-naviga=
tion\_\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c));
} \@media print { #pfe-navigation .pfe-navigation\_\_account-toggle,
#pfe-navigation \[slot=3D= \"account\"\] \> a\[href\], pfe-navigation
.pfe-navigation\_\_account-toggle, pfe-n= avigation
\[slot=3D\"account\"\] \> a\[href\] { display: none; } } #pfe-navigation
.pfe-navigation\_\_account-toggle pfe-icon, #pfe-navigation \[=
slot=3D\"account\"\] \> a\[href\] pfe-icon, pfe-navigation
.pfe-navigation\_\_accou= nt-toggle pfe-icon, pfe-navigation
\[slot=3D\"account\"\] \> a\[href\] pfe-icon { = \--pfe-icon\--size:
18px; padding: 2px 0px 4px; } \@media (min-width: 768px) {
#pfe-navigation .pfe-navigation\_\_account-toggle pfe-icon,
#pfe-navigation= \[slot=3D\"account\"\] \> a\[href\] pfe-icon,
pfe-navigation .pfe-navigation\_\_acc= ount-toggle pfe-icon,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\] pfe-icon = {
padding-right: 0px; } } #pfe-navigation
.pfe-navigation\_\_account-toggle:focus, #pfe-navigation .pfe=
-navigation\_\_account-toggle:hover, #pfe-navigation
.pfe-navigation\_\_account= -toggle\[aria-expanded=3D\"true\"\],
#pfe-navigation \[slot=3D\"account\"\] \> a\[hre= f\]\[href\]:focus,
#pfe-navigation \[slot=3D\"account\"\] \> a\[href\]\[href\]:hover, p=
fe-navigation .pfe-navigation\_\_account-toggle:focus, pfe-navigation
.pfe-na= vigation\_\_account-toggle:hover, pfe-navigation
.pfe-navigation\_\_account-tog= gle\[aria-expanded=3D\"true\"\],
pfe-navigation \[slot=3D\"account\"\] \> a\[href\]\[hr= ef\]:focus,
pfe-navigation \[slot=3D\"account\"\] \> a\[href\]\[href\]:hover {
box-sh= adow: inset 0 4px 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--=
pfe-theme\--color\--ui-accent,#06c)); } #pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\], pf=
e-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\] { \--pf=
e-icon\--color:
var(\--pfe-navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme=
\--color\--text,#151515)); background:
var(\--pfe-navigation\_\_nav-bar\--toggle-=
-BackgroundColor\--active,var(\--pfe-theme\--color\--surface\--lightest,#fff));
= color:
var(\--pfe-navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme\--color-=
-text,#151515)); } #pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\]:foc= us,
pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\]:= focus {
outline: 0px; } #pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"true\"\]:foc=
us::after, pfe-navigation
.pfe-navigation\_\_account-toggle\[aria-expanded=3D\"=
true\"\]:focus::after { border: 1px dashed
var(\--pfe-navigation\_\_nav-bar\--Col=
or\--active,var(\--pfe-theme\--color\--text,#151515)); inset: 0px;
content: \"\";= display: block; position: absolute; } #pfe-navigation
.pfe-navigation\_\_fallback-links, #pfe-navigation .pfe-navig=
ation\_\_menu, pfe-navigation .pfe-navigation\_\_fallback-links,
pfe-navigation= .pfe-navigation\_\_menu { font-size: inherit;
list-style: none; margin: 0px;= padding: 0px; } \@media (min-width:
768px) { #pfe-navigation .pfe-navigation\_\_fallback-links,
#pfe-navigation .pfe-nav= igation\_\_menu, pfe-navigation
.pfe-navigation\_\_fallback-links, pfe-navigati= on
.pfe-navigation\_\_menu { align-items: stretch; display: flex; } }
#pfe-navigation .pfe-navigation\_\_fallback-links li, #pfe-navigation
.pfe-na= vigation\_\_menu li, pfe-navigation
.pfe-navigation\_\_fallback-links li, pfe-n= avigation
.pfe-navigation\_\_menu li { font-size: inherit; margin: 0px; paddi= ng:
0px; } #pfe-navigation .pfe-navigation\_\_fallback-links li::before,
#pfe-navigation= .pfe-navigation\_\_menu li::before, pfe-navigation
.pfe-navigation\_\_fallback= -links li::before, pfe-navigation
.pfe-navigation\_\_menu li::before { conten= t: none; } #pfe-navigation
.pfe-navigation\_\_fallback-links, pfe-navigation .pfe-naviga=
tion\_\_fallback-links { margin-left: auto; } #pfe-navigation
.pfe-navigation\_\_menu-link, pfe-navigation .pfe-navigation\_=
\_menu-link { display: flex; font-size:
var(\--pf-global\--FontSize\--md,1rem);= white-space: nowrap; }
#pfe-navigation.pfe-navigation\--processed,
pfe-navigation.pfe-navigation\--p= rocessed { display: block; padding:
0px; } #pfe-navigation.pfe-navigation\--processed::before,
pfe-navigation.pfe-navig= ation\--processed::before { content: none; }
#pfe-navigation.pfe-navigation\--processed \> \[slot=3D\"account\"\],
#pfe-naviga= tion.pfe-navigation\--processed \> \[slot=3D\"search\"\],
#pfe-navigation.pfe-nav= igation\--processed \>
\[slot=3D\"secondary-links\"\], pfe-navigation.pfe-navigat=
ion\--processed \> \[slot=3D\"account\"\],
pfe-navigation.pfe-navigation\--process= ed \> \[slot=3D\"search\"\],
pfe-navigation.pfe-navigation\--processed \> \[slot=3D=
\"secondary-links\"\] { height: auto; overflow: visible; visibility:
visible; = width: auto; } #pfe-navigation.pfe-navigation\--processed
pfe-navigation-dropdown, pfe-navi= gation.pfe-navigation\--processed
pfe-navigation-dropdown { display: block; = }
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown,
#pfe-n= avigation.pfe-navigation\--processed pfe-navigation-dropdown,
#pfe-navigatio= n.pfe-navigation\--processed \> \[slot\],
pfe-navigation.pfe-navigation\--proces= sed .pfe-navigation\_\_dropdown,
pfe-navigation.pfe-navigation\--processed pfe= -navigation-dropdown,
pfe-navigation.pfe-navigation\--processed \> \[slot\] { a= nimation:
auto ease 0s 1 normal none running none; opacity: 1; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\], pfe-n=
avigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] {
display: b= lock; height: auto; list-style: none; margin: 0px 0px 8px;
padding: 0px; wi= dth: auto; } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\], pfe=
-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] {
margin: = 0px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\], .pfe-navigation\--collapse-secondary-li=
nks pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] { m= argin: 0px 0px 8px; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a, #=
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> butto= n, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> butt= on { \--pfe-icon\--color:
var(\--pfe-navigation\_\_dropdown\--link\--Color,var(\--p=
fe-theme\--color\--link,#06c)); align-items: center; appearance: none;
backgr= ound: 0px 0px; border: 0px; color:
var(\--pfe-navigation\_\_dropdown\--link\--Co=
lor,var(\--pfe-theme\--color\--link,#06c)); cursor: pointer; display:
flex; fo= nt-family: inherit; font-size:
var(\--pf-global\--FontSize\--md,1rem); justify= -content: flex-start;
margin: 0px; outline: 0px; padding: 8px 24px; positio= n: relative;
text-align: center; text-decoration: none; white-space: nowrap= ; width:
100%; } \@media print { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> but= ton,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> = a, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> bu= tton { display: none !important; }
} \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> but= ton,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> = a, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> bu= tton { \--pfe-icon\--color:
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var=
(\--pfe-theme\--color\--ui-base\--text,#fff)); color:
var(\--pfe-navigation\_\_nav=
-bar\--Color\--default,var(\--pfe-theme\--color\--ui-base\--text,#fff));
display:= flex; flex-direction: column; font-size:
var(\--pfe-navigation\--FontSize\--x= s,12px); height:
var(\--pfe-navigation\_\_nav-bar\--Height,72px); justify-conte= nt:
flex-end; padding: 14px 8px; width: auto; } \@supports (display:grid) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a,=
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> but= ton,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> = a, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> bu= tton { place-items: center;
display: grid; grid-template-rows: 26px 18px; } }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a\[= class\]:focus,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a\[class\]:hover,
#pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> button\[class\]:focus,
#pfe-navigation.pfe-navigation= \--processed
\[slot=3D\"secondary-links\"\] \> button\[class\]:hover, pfe-navigatio=
n.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] \>
a\[class\]:focus, pf= e-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a\[class= \]:hover,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"=
\] \> button\[class\]:focus, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"= secondary-links\"\] \> button\[class\]:hover { box-shadow:
inset 0 4px 0 0 var(-=
-pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme\--color\--ui-accent=
,#06c)); } } #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:fo= cus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \>= a:hover,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-link=
s\"\] \> button:focus, #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> button:hover,
pfe-navigation.pfe-navigation\--processed \[slo=
t=3D\"secondary-links\"\] \> a:focus,
pfe-navigation.pfe-navigation\--processed =
\[slot=3D\"secondary-links\"\] \> a:hover,
pfe-navigation.pfe-navigation\--proces= sed
\[slot=3D\"secondary-links\"\] \> button:focus,
pfe-navigation.pfe-navigatio= n\--processed
\[slot=3D\"secondary-links\"\] \> button:hover { box-shadow: inset = 4px
0 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme\--c=
olor\--ui-accent,#06c)); } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:= focus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> a:hover,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-li=
nks\"\] \> button:focus, #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"se= condary-links\"\] \> button:hover,
pfe-navigation.pfe-navigation\--processed \[s=
lot=3D\"secondary-links\"\] \> a:focus,
pfe-navigation.pfe-navigation\--processe= d
\[slot=3D\"secondary-links\"\] \> a:hover,
pfe-navigation.pfe-navigation\--proc= essed
\[slot=3D\"secondary-links\"\] \> button:focus,
pfe-navigation.pfe-navigat= ion\--processed
\[slot=3D\"secondary-links\"\] \> button:hover { box-shadow: inse= t 0
4px 0 0
var(\--pfe-navigation\_\_nav-bar\--highlight-color,var(\--pfe-theme-=
-color\--ui-accent,#06c)); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a:focus,
.pfe-navigation\--collapse-se= condary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a:hover, .pfe-navigation\--collapse-secondary-links
#pfe-navigatio= n.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> button:focus, .pfe=
-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--proce= ssed
\[slot=3D\"secondary-links\"\] \> button:hover,
.pfe-navigation\--collapse-s= econdary-links
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a:focus, .pfe-navigation\--collapse-secondary-links
pfe-navigation= .pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:hover, .pfe-navig=
ation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed \[s=
lot=3D\"secondary-links\"\] \> button:focus,
.pfe-navigation\--collapse-secondar= y-links
pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> button:hover { box-shadow: inset 4px
0 0 0 var(\--pfe-navigation\_\_nav-bar=
\--highlight-color,var(\--pfe-theme\--color\--ui-accent,#06c)); }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:fo= cus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \>= button:focus,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a:focus, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"second= ary-links\"\] \> button:focus { outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:fo= cus::after,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-li=
nks\"\] \> button:focus::after,
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> a:focus::after,
pfe-navigation.pfe-navigation\--proc= essed
\[slot=3D\"secondary-links\"\] \> button:focus::after { border: 1px
dashed= ; inset: 0px; content: \"\"; display: block; position: absolute;
} #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a pf= e-icon,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"=
\] \> button pfe-icon, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> a pfe-icon,
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> button pfe-icon { pointer-events: none; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a .s= econdary-link\_\_icon-wrapper,
#pfe-navigation.pfe-navigation\--processed \[slo=
t=3D\"secondary-links\"\] \> a \> pfe-icon,
#pfe-navigation.pfe-navigation\--proc= essed
\[slot=3D\"secondary-links\"\] \> button
.secondary-link\_\_icon-wrapper, #p=
fe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> button= \> pfe-icon, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-li= nks\"\] \> a .secondary-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation\--pro= cessed
\[slot=3D\"secondary-links\"\] \> a \> pfe-icon,
pfe-navigation.pfe-naviga= tion\--processed
\[slot=3D\"secondary-links\"\] \> button .secondary-link\_\_icon-w=
rapper, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> button \> pfe-icon {
\--pfe-icon\--size: 18px; padding-right: 5px; } \@media (min-width:
768px) { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a = .secondary-link\_\_icon-wrapper,
#pfe-navigation.pfe-navigation\--processed \[s=
lot=3D\"secondary-links\"\] \> a \> pfe-icon,
#pfe-navigation.pfe-navigation\--pr= ocessed
\[slot=3D\"secondary-links\"\] \> button
.secondary-link\_\_icon-wrapper, =
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> butt= on \> pfe-icon,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> a .secondary-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a \> pfe-icon,
pfe-navigation.pfe-navi= gation\--processed
\[slot=3D\"secondary-links\"\] \> button .secondary-link\_\_icon=
-wrapper, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links= \"\] \> button \> pfe-icon { padding: 2px
0px 4px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a .secondary-link\_\_icon-wrapper,
.pfe= -navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--proce= ssed
\[slot=3D\"secondary-links\"\] \> a \> pfe-icon,
.pfe-navigation\--collapse-s= econdary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary=
-links\"\] \> button .secondary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-= secondary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondar=
y-links\"\] \> button \> pfe-icon,
.pfe-navigation\--collapse-secondary-links pf=
e-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> a .seco= ndary-link\_\_icon-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-nav=
igation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\] \> a
\> pfe-icon= , .pfe-navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--= processed
\[slot=3D\"secondary-links\"\] \> button
.secondary-link\_\_icon-wrapper= ,
.pfe-navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--= processed
\[slot=3D\"secondary-links\"\] \> button \> pfe-icon { padding: 0px 16p=
x 0px 0px; } #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a pf= e-icon,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"=
\] \> button pfe-icon, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> a pfe-icon,
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> button pfe-icon { display: block; height:
18px; } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:= focus,
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\]= \> button:focus,
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondar=
y-links\"\] \> a:focus, pfe-navigation.pfe-navigation\--processed
\[slot=3D\"seco= ndary-links\"\] \> button:focus { outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:= focus::after,
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> button:focus::after,
pfe-navigation.pfe-navigation\--processed \[sl=
ot=3D\"secondary-links\"\] \> a:focus::after,
pfe-navigation.pfe-navigation\--pr= ocessed
\[slot=3D\"secondary-links\"\] \> button:focus::after { border: 1px
dash= ed
var(\--pfe-navigation\_\_nav-bar\--Color\--default,var(\--pfe-theme\--color\--ui=
-base\--text,#fff)); inset: 0px; content: \"\"; display: block;
position: abso= lute; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a:focus,
.pfe-navigation\--collapse-se= condary-links
#pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-=
links\"\] \> button:focus, .pfe-navigation\--collapse-secondary-links
pfe-navig= ation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a:focus, .pfe-=
navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--process= ed
\[slot=3D\"secondary-links\"\] \> button:focus { box-shadow: none; }
\@media (min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] \> a\[= aria-expanded=3D\"true\"\],
#pfe-navigation.pfe-navigation\--processed \[slot=3D=
\"secondary-links\"\] \> button\[aria-expanded=3D\"true\"\],
pfe-navigation.pfe-nav= igation\--processed
\[slot=3D\"secondary-links\"\] \> a\[aria-expanded=3D\"true\"\], =
pfe-navigation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
\> butto= n\[aria-expanded=3D\"true\"\] { \--pfe-icon\--color:
var(\--pfe-navigation\_\_nav-ba=
r\--Color\--active,var(\--pfe-theme\--color\--text,#151515));
background: var(\--=
pfe-navigation\_\_nav-bar\--toggle\--BackgroundColor\--active,var(\--pfe-theme\--c=
olor\--surface\--lightest,#fff)); color:
var(\--pfe-navigation\_\_nav-bar\--Color=
\--active,var(\--pfe-theme\--color\--text,#151515)); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\] \> a\[aria-expanded=3D\"true\"\],
.pfe-navig= ation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--processed \[=
slot=3D\"secondary-links\"\] \> button\[aria-expanded=3D\"true\"\],
.pfe-navigation= \--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed \[slot=
=3D\"secondary-links\"\] \> a\[aria-expanded=3D\"true\"\],
.pfe-navigation\--collaps= e-secondary-links
pfe-navigation.pfe-navigation\--processed \[slot=3D\"seconda=
ry-links\"\] \> button\[aria-expanded=3D\"true\"\] { background: 0px
0px; box-shad= ow: none; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown\_= \_wrapper\--single-column,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_custom-dropdown\_\_wrapper\--single-column { position:
relative; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown\_= \_wrapper,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_custom-=
dropdown\_\_wrapper { display: block; }
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe-n=
avigation\_\_dropdown-wrapper\[class\],
pfe-navigation.pfe-navigation\--processe= d
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class\] { hei= ght: 0px;
transition: var(\--pfe-navigation\--accordion-transition,height .25= s
ease-in-out); } \@media (prefers-reduced-motion) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe=
-navigation\_\_dropdown-wrapper\[class\],
pfe-navigation.pfe-navigation\--proces= sed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class\] { t= ransition: none; } }
\@media (min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe=
-navigation\_\_dropdown-wrapper\[class\],
pfe-navigation.pfe-navigation\--proces= sed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class\] { p= osition: absolute;
right: 0px; top: var(\--pfe-navigation\_\_nav-bar\--Height,7= 2px); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class= \],
.pfe-navigation\--collapse-secondary-links
pfe-navigation.pfe-navigation-= -processed
\[slot=3D\"secondary-links\"\] .pfe-navigation\_\_dropdown-wrapper\[cla=
ss\] { position: static; } \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe=
-navigation\_\_dropdown-wrapper\[class\]\[aria-hidden=3D\"false\"\],
pfe-navigation= .pfe-navigation\--processed
\[slot=3D\"secondary-links\"\] .pfe-navigation\_\_drop=
down-wrapper\[class\]\[aria-hidden=3D\"false\"\] { height: auto; } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
\[slot=3D\"secondary-links\"\]
.pfe-navigation\_\_dropdown-wrapper\[class=
\]\[aria-hidden=3D\"false\"\],
.pfe-navigation\--collapse-secondary-links pfe-nav=
igation.pfe-navigation\--processed \[slot=3D\"secondary-links\"\]
.pfe-navigatio=
n\_\_dropdown-wrapper\[class\]\[aria-hidden=3D\"false\"\] { height: 0px;
} #pfe-navigation.pfe-navigation\--processed\[breakpoint=3D\"mobile\"\]
\[slot=3D\"s= econdary-links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wrapper, pfe-navi=
gation.pfe-navigation\--processed\[breakpoint=3D\"mobile\"\]
\[slot=3D\"secondary-= links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wrapper { left: calc(100vw= -
var(\--pfe-navigation\_\_mobile-dropdown\--PaddingHorizontal,32px));
positio= n: absolute; top: 0px; width: 100vw; }
#pfe-navigation.pfe-navigation\--processed\[breakpoint=3D\"mobile\"\]
\[slot=3D\"s= econdary-links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wrapper\[aria-hidd= en=3D\"false\"\],
pfe-navigation.pfe-navigation\--processed\[breakpoint=3D\"mobil= e\"\]
\[slot=3D\"secondary-links\"\]\[mobile-slider\]
.pfe-navigation\_\_dropdown-wra= pper\[aria-hidden=3D\"false\"\] {
height: calc(100vh - var(\--pfe-navigation\_\_na= v-bar\--Height,72px));
overflow-y: scroll; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-w= rapper\--default-styles,
#pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_site-switcher .pfe-navigation\_\_dropdown-wrapper,
pfe-navigation.pfe= -navigation\--processed
.pfe-navigation-item\_\_tray\--container, pfe-navigatio=
n.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styl= es,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher= .pfe-navigation\_\_dropdown-wrapper {
background: var(\--pfe-navigation\_\_drop=
down\--Background,var(\--pfe-theme\--color\--surface\--lightest,#fff));
padding:= 0
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--mobile,24px);
} \@media (min-width: 768px) {
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--con= tainer,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown=
-wrapper\--default-styles, #pfe-navigation.pfe-navigation\--processed
.pfe-na= vigation\_\_site-switcher .pfe-navigation\_\_dropdown-wrapper,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation-item\_\_tray\--container, pfe-navigat=
ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switch= er .pfe-navigation\_\_dropdown-wrapper {
padding: 0 var(\--pfe-navigation\_\_dro=
pdown\--full-width\--spacing\--desktop,64px)
var(\--pfe-navigation\_\_dropdown\--f=
ull-width\--spacing\--mobile,24px); } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation-item\_\_tray\--container, .pfe-navigation\--collapse-s=
econdary-links #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_d= ropdown-wrapper\--default-styles,
.pfe-navigation\--collapse-secondary-links =
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown-wrapper,
.pfe-navigation\--collapse-secondary-links =
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner,
.pfe-navigation\--collapse-secondary-links pfe-navigation.pfe-navigatio=
n\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles,
.pfe-naviga= tion\--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_site-switcher .pfe-navigation\_\_dropdown-wrapper {
padding: 0 =
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--mobile,24px);
} #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown=
-wrapper\--default-styles a, pfe-navigation.pfe-navigation\--processed
.pfe-n= avigation-item\_\_tray\--container a,
pfe-navigation.pfe-navigation\--processed=
.pfe-navigation\_\_dropdown-wrapper\--default-styles a { border: 1px
solid tr= ansparent; color:
var(\--pfe-navigation\_\_dropdown\--link\--Color,var(\--pfe-the=
me\--color\--link,#06c)); display: inline-block; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-ite=
m\_\_tray\--container a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-=
navigation\_\_dropdown-wrapper\--default-styles a:focus,
#pfe-navigation.pfe-n= avigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a:ho= ver,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--c= ontainer a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-=
item\_\_tray\--container a:hover,
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_dropdown-wrapper\--default-styles a:focus,
pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a:h= over { color:
var(\--pfe-navigation\_\_dropdown\--link\--Color\--hover,#036); tex=
t-decoration: underline; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dr=
opdown-wrapper\--default-styles a:focus,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container a:focus,
pfe-navigation.pfe-nav= igation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a:focu= s { border:
1px dashed; outline: 0px; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header,
#pfe-navigation.pfe-navigation\--processed .pfe=
-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading-level\], #=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner h2,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tra=
y\--container h3, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-= item\_\_tray\--container h4,
#pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation-item\_\_tray\--container h5,
#pfe-navigation.pfe-navigation\--processe= d
.pfe-navigation-item\_\_tray\--container h6,
#pfe-navigation.pfe-navigation-= -processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles .pfe-link-list=
\--header, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdo= wn-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-level\], #pfe-nav=
igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles h2,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dro=
pdown-wrapper\--default-styles h3,
#pfe-navigation.pfe-navigation\--processed=
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4,
#pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5,=
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h6,
pfe-navigation.pfe-navigation\--processed .pfe-navigat=
ion-item\_\_tray\--container .pfe-link-list\--header,
pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation-item\_\_tray\--container \[role=3D\"heading\"\]\[ar=
ia-heading-level\], pfe-navigation.pfe-navigation\--processed
.pfe-navigation= -item\_\_tray\--container h2,
pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation-item\_\_tray\--container h3,
pfe-navigation.pfe-navigation\--processed=
.pfe-navigation-item\_\_tray\--container h4,
pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation-item\_\_tray\--container h5, pfe-navigation.pfe-navig=
ation\--processed .pfe-navigation-item\_\_tray\--container h6,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles =
.pfe-link-list\--header, pfe-navigation.pfe-navigation\--processed
.pfe-navig= ation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-lev= el\],
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wra= pper\--default-styles h2,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_dropdown-wrapper\--default-styles h3,
pfe-navigation.pfe-navigation-= -processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4, pfe-naviga=
tion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-s= tyles h5,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles h6 { margin:
var(\--pfe-navigation\--gutter,32px) 0= .75em; padding: 0px;
break-inside: avoid; color: var(\--pfe-navigation\_\_dro=
pdown\--headings\--Color,#464646); font-family:
var(\--pfe-navigation\--FontFam= ilyHeadline,Red Hat
Display,RedHatDisplay,Arial,Helvetica,sans-serif); font= -size:
var(\--pf-global\--FontSize\--lg,1.125rem); font-weight: 500; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner
.pfe-link-list\--header:first-child,
#pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-headi= ng-level\]:first-child,
#pfe-navigation.pfe-navigation\--processed .pfe-navig=
ation-item\_\_tray\--container h2:first-child,
#pfe-navigation.pfe-navigation-= -processed
.pfe-navigation-item\_\_tray\--container h3:first-child, #pfe-navig=
ation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h4:fi= rst-child,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_=
tray\--container h5:first-child,
#pfe-navigation.pfe-navigation\--processed .=
pfe-navigation-item\_\_tray\--container h6:first-child,
#pfe-navigation.pfe-na= vigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles .pfe-=
link-list\--header:first-child,
#pfe-navigation.pfe-navigation\--processed .p=
fe-navigation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-hea= ding-level\]:first-child,
#pfe-navigation.pfe-navigation\--processed .pfe-nav=
igation\_\_dropdown-wrapper\--default-styles h2:first-child,
#pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles = h3:first-child,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_=
dropdown-wrapper\--default-styles h4:first-child,
#pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5:first-= child,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown-=
wrapper\--default-styles h6:first-child,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container
.pfe-link-list\--header:first-ch= ild,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--c= ontainer
\[role=3D\"heading\"\]\[aria-heading-level\]:first-child,
pfe-navigation= .pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h2:first-c= hild,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--= container h3:first-child,
pfe-navigation.pfe-navigation\--processed .pfe-nav=
igation-item\_\_tray\--container h4:first-child,
pfe-navigation.pfe-navigation= \--processed
.pfe-navigation-item\_\_tray\--container h5:first-child, pfe-navig=
ation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h6:fi= rst-child,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdo=
wn-wrapper\--default-styles .pfe-link-list\--header:first-child,
pfe-navigati= on.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-sty= les
\[role=3D\"heading\"\]\[aria-heading-level\]:first-child,
pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2:= first-child,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_drop=
down-wrapper\--default-styles h3:first-child,
pfe-navigation.pfe-navigation-= -processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4:first-child= ,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h5:first-child,
pfe-navigation.pfe-navigation\--processed =
.pfe-navigation\_\_dropdown-wrapper\--default-styles h6:first-child {
margin-t= op: 0px; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header a,
#pfe-navigation.pfe-navigation\--processed .p=
fe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading-level\] = a,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--co= ntainer h2 a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-ite=
m\_\_tray\--container h3 a, #pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation-item\_\_tray\--container h4 a,
#pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation-item\_\_tray\--container h5 a,
#pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation-item\_\_tray\--container h6 a, #pfe-navigation.p=
fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles =
.pfe-link-list\--header a, #pfe-navigation.pfe-navigation\--processed
.pfe-na= vigation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-= level\] a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdo=
wn-wrapper\--default-styles h2 a,
#pfe-navigation.pfe-navigation\--processed =
.pfe-navigation\_\_dropdown-wrapper\--default-styles h3 a,
#pfe-navigation.pfe= -navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4= a,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wra= pper\--default-styles h5 a,
#pfe-navigation.pfe-navigation\--processed .pfe-n=
avigation\_\_dropdown-wrapper\--default-styles h6 a,
pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation-item\_\_tray\--container .pfe-link-list\--heade= r a,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--c= ontainer
\[role=3D\"heading\"\]\[aria-heading-level\] a,
pfe-navigation.pfe-navig= ation\--processed
.pfe-navigation-item\_\_tray\--container h2 a, pfe-navigation=
.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container h3
a, pfe-= navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container = h4 a,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--= container h5 a,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-it=
em\_\_tray\--container h6 a, pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation\_\_dropdown-wrapper\--default-styles
.pfe-link-list\--header a, pfe-nav= igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a,
pfe-navigation.pfe-navig= ation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2 a, pf=
e-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--d= efault-styles h3 a,
pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--default-styles h4 a,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5 a, pfe-navigat=
ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles h6 a { border:
1px solid transparent; color: var(\--pfe-navigation\_\_dro=
pdown\--headings\--Color,#464646); text-decoration: underline; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header
a:focus, #pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation-item\_\_tray\--container .pfe-link-list\--header
a:hover, #= pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner
\[role=3D\"heading\"\]\[aria-heading-level\] a:focus,
#pfe-navigation.pfe-nav= igation\--processed
.pfe-navigation-item\_\_tray\--container \[role=3D\"heading\"\]=
\[aria-heading-level\] a:hover,
#pfe-navigation.pfe-navigation\--processed .pf=
e-navigation-item\_\_tray\--container h2 a:focus,
#pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation-item\_\_tray\--container h2 a:hover, #pfe-naviga=
tion.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
h3 a:f= ocus, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray-= -container h3 a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-navig=
ation-item\_\_tray\--container h4 a:focus,
#pfe-navigation.pfe-navigation\--pro= cessed
.pfe-navigation-item\_\_tray\--container h4 a:hover, #pfe-navigation.pf=
e-navigation\--processed .pfe-navigation-item\_\_tray\--container h5
a:focus, #= pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contai= ner h5 a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-i=
tem\_\_tray\--container h6 a:focus,
#pfe-navigation.pfe-navigation\--processed =
.pfe-navigation-item\_\_tray\--container h6 a:hover,
#pfe-navigation.pfe-navig= ation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles .pfe-lin=
k-list\--header a:focus, #pfe-navigation.pfe-navigation\--processed
.pfe-navi= gation\_\_dropdown-wrapper\--default-styles
.pfe-link-list\--header a:hover, #p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--= default-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a:focus, #pfe-navigat=
ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles
\[role=3D\"heading\"\]\[aria-heading-level\] a:hover,
#pfe-navigation.pfe-na= vigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2 a:= focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdown-=
wrapper\--default-styles h2 a:hover,
#pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h3 a:focus,
#pfe-navig= ation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-= styles h3 a:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--default-styles h4 a:focus,
#pfe-navigation.pfe-navigat= ion\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4 a:hover= ,
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapp= er\--default-styles h5 a:focus,
#pfe-navigation.pfe-navigation\--processed .p=
fe-navigation\_\_dropdown-wrapper\--default-styles h5 a:hover,
#pfe-navigation= .pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-style= s h6 a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dr=
opdown-wrapper\--default-styles h6 a:hover,
pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation-item\_\_tray\--container .pfe-link-list\--header a:foc=
us, pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--co= ntainer .pfe-link-list\--header
a:hover, pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading= -level\] a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-i=
tem\_\_tray\--container \[role=3D\"heading\"\]\[aria-heading-level\]
a:hover, pfe-na= vigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h2= a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tr=
ay\--container h2 a:hover, pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation-item\_\_tray\--container h3 a:focus,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation-item\_\_tray\--container h3 a:hover, pfe-navigation.pf=
e-navigation\--processed .pfe-navigation-item\_\_tray\--container h4
a:focus, p= fe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--contain= er h4 a:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-ite=
m\_\_tray\--container h5 a:focus,
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation-item\_\_tray\--container h5 a:hover,
pfe-navigation.pfe-navigatio= n\--processed
.pfe-navigation-item\_\_tray\--container h6 a:focus, pfe-navigati=
on.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
h6 a:hov= er, pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrap= per\--default-styles
.pfe-link-list\--header a:focus, pfe-navigation.pfe-navi=
gation\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
.pfe-li= nk-list\--header a:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_dropdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-le= vel\] a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dro=
pdown-wrapper\--default-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a:hove= r,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapp= er\--default-styles h2 a:focus,
pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_dropdown-wrapper\--default-styles h2 a:hover,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles = h3 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropd=
own-wrapper\--default-styles h3 a:hover,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4 a:focus,
pfe-nav= igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles h4 a:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navigati=
on\_\_dropdown-wrapper\--default-styles h5 a:focus,
pfe-navigation.pfe-navigat= ion\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5 a:hover= ,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h6 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe=
-navigation\_\_dropdown-wrapper\--default-styles h6 a:hover { color:
var(\--pfe= -navigation\_\_dropdown\--link\--Color\--hover,#036);
text-decoration: none; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner .pfe-link-list\--header
a:focus, #pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation-item\_\_tray\--container
\[role=3D\"heading\"\]\[aria-heading-l= evel\] a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-it=
em\_\_tray\--container h2 a:focus,
#pfe-navigation.pfe-navigation\--processed .=
pfe-navigation-item\_\_tray\--container h3 a:focus,
#pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation-item\_\_tray\--container h4 a:focus, #pfe-navi=
gation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container h5 a= :focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tra=
y\--container h6 a:focus, #pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation\_\_dropdown-wrapper\--default-styles
.pfe-link-list\--header a:focus, #=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper-= -default-styles
\[role=3D\"heading\"\]\[aria-heading-level\] a:focus, #pfe-naviga=
tion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-s= tyles h2 a:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation=
\_\_dropdown-wrapper\--default-styles h3 a:focus,
#pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h4 a:focus,=
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles h5 a:focus,
#pfe-navigation.pfe-navigation\--processed .pf=
e-navigation\_\_dropdown-wrapper\--default-styles h6 a:focus,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation-item\_\_tray\--container .pfe-link-li= st\--header
a:focus, pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n-item\_\_tray\--container \[role=3D\"heading\"\]\[aria-heading-level\]
a:focus, pfe= -navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container= h2 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_=
\_tray\--container h3 a:focus, pfe-navigation.pfe-navigation\--processed
.pfe-= navigation-item\_\_tray\--container h4 a:focus,
pfe-navigation.pfe-navigation-= -processed
.pfe-navigation-item\_\_tray\--container h5 a:focus, pfe-navigation=
.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container h6
a:focus= , pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles
.pfe-link-list\--header a:focus, pfe-navigation.pfe-naviga=
tion\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
\[role=3D\"= heading\"\]\[aria-heading-level\] a:focus,
pfe-navigation.pfe-navigation\--proce= ssed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h2 a:focus,
pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default= -styles h3 a:focus,
pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--default-styles h4 a:focus,
pfe-navigation.pfe-navigati= on\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles h5 a:focus,=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--default-styles h6 a:focus {
border: 1px dashed; outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner li,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles li, pfe-navigation.pfe-navigation\--processed
.pfe= -navigation-item\_\_tray\--container li,
pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation\_\_dropdown-wrapper\--default-styles li { margin: 0px
0px = 16px; break-inside: avoid; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner a,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tra=
y\--container pfe-card, #pfe-navigation.pfe-navigation\--processed
.pfe-navig= ation-item\_\_tray\--container pfe-cta,
#pfe-navigation.pfe-navigation\--proces= sed
.pfe-navigation\_\_dropdown-wrapper\--default-styles a,
#pfe-navigation.pf= e-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles p= fe-card,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles pfe-cta,
pfe-navigation.pfe-navigation\--processed=
.pfe-navigation-item\_\_tray\--container a,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation-item\_\_tray\--container pfe-card, pfe-navigation.pfe-=
navigation\--processed .pfe-navigation-item\_\_tray\--container pfe-cta,
pfe-na= vigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defau= lt-styles a,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_drop=
down-wrapper\--default-styles pfe-card,
pfe-navigation.pfe-navigation\--proce= ssed
.pfe-navigation\_\_dropdown-wrapper\--default-styles pfe-cta {
break-insi= de: avoid; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner
pfe-cta\[pfe-priority=3D\"primary\"\],
#pfe-navigation.pfe-navigation\--pro= cessed
.pfe-navigation-item\_\_tray\--container
pfe-cta\[priority=3D\"primary\"\],=
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrappe= r\--default-styles
pfe-cta\[pfe-priority=3D\"primary\"\], #pfe-navigation.pfe-na=
vigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-styles pfe-c=
ta\[priority=3D\"primary\"\], pfe-navigation.pfe-navigation\--processed
.pfe-nav= igation-item\_\_tray\--container
pfe-cta\[pfe-priority=3D\"primary\"\], pfe-naviga=
tion.pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
pfe-ct= a\[priority=3D\"primary\"\],
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-priority=3D\"primary\"\],=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--default-styles
pfe-cta\[priority=3D\"primary\"\] { \--pfe-cta\--BackgroundColor= :
var(\--pfe-navigation\_\_dropdown\--pfe-cta\--BackgroundColor,#e00);
\--pfe-cta= \--BackgroundColor\--hover:
var(\--pfe-navigation\_\_dropdown\--pfe-cta\--hover\--B=
ackgroundColor,#c00); \--pfe-theme\--ui\--border-width: 0; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner
pfe-cta\[pfe-priority=3D\"primary\"\]:focus,
#pfe-navigation.pfe-navigatio= n\--processed
.pfe-navigation-item\_\_tray\--container pfe-cta\[pfe-priority=3D\"=
primary\"\]:hover, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-= item\_\_tray\--container
pfe-cta\[priority=3D\"primary\"\]:focus, #pfe-navigation.=
pfe-navigation\--processed .pfe-navigation-item\_\_tray\--container
pfe-cta\[pri= ority=3D\"primary\"\]:hover,
#pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-priority=3D\"primary\"= \]:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdow=
n-wrapper\--default-styles pfe-cta\[pfe-priority=3D\"primary\"\]:hover,
#pfe-nav= igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--defaul= t-styles
pfe-cta\[priority=3D\"primary\"\]:focus, #pfe-navigation.pfe-navigatio=
n\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[prio= rity=3D\"primary\"\]:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation-item\_\_tray\--container
pfe-cta\[pfe-priority=3D\"primary\"\]:focus, pfe-n=
avigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container p=
fe-cta\[pfe-priority=3D\"primary\"\]:hover,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation-item\_\_tray\--container
pfe-cta\[priority=3D\"primary\"\]:f= ocus,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--= container
pfe-cta\[priority=3D\"primary\"\]:hover, pfe-navigation.pfe-navigatio=
n\--processed .pfe-navigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-= priority=3D\"primary\"\]:focus,
pfe-navigation.pfe-navigation\--processed .pfe-=
navigation\_\_dropdown-wrapper\--default-styles
pfe-cta\[pfe-priority=3D\"primar= y\"\]:hover,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dropdo=
wn-wrapper\--default-styles pfe-cta\[priority=3D\"primary\"\]:focus,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper\--default-st= yles
pfe-cta\[priority=3D\"primary\"\]:hover { \--pfe-cta\--BackgroundColor:
var(=
\--pfe-navigation\_\_dropdown\--pfe-cta\--hover\--BackgroundColor,#c00);
} pfe-card #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tr= ay\--container pfe-cta, pfe-card
#pfe-navigation.pfe-navigation\--processed .=
pfe-navigation\_\_dropdown-wrapper\--default-styles pfe-cta, pfe-card
pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container pfe-= cta, pfe-card
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_dro=
pdown-wrapper\--default-styles pfe-cta { margin-top: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--conta= iner li,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-item\_\_tr=
ay\--container ul, #pfe-navigation.pfe-navigation\--processed
.pfe-navigation= \_\_dropdown-wrapper\--default-styles li,
#pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_dropdown-wrapper\--default-styles ul,
pfe-navigation.= pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container li, pfe-nav=
igation.pfe-navigation\--processed
.pfe-navigation-item\_\_tray\--container ul,=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--default-styles li,
pfe-navigation.pfe-navigation\--processed .pfe-navigati=
on\_\_dropdown-wrapper\--default-styles ul { list-style: none; margin:
0px; pa= dding: 0px; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-grid, #pfe-naviga= tion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles, p=
fe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigatio= n.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { col= or:
var(\--pfe-navigation\_\_dropdown\--Color,#151515); column-count: auto;
dis= play: block; font-size: var(\--pf-global\--FontSize\--md,1rem);
gap: 0px; marg= in-left: auto; margin-right: auto; max-width:
var(\--pfe-navigation\--content= -max-width,1136px); padding-bottom:
12px; padding-top: 12px; width: calc(10= 0% + 32px); } \@media
(min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
.pfe-navigation-grid, #pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles,=
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { c= olumn-count: 3;
display: block; gap: var(\--pfe-navigation\--gutter,32px); pa=
dding-bottom: 12px; padding-top: 12px; } } \@media (min-width: 1200px) {
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
#pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles,=
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { c= olumn-count: auto;
display: flex; flex-wrap: wrap; padding-bottom: 32px; pa= dding-top:
32px; } \@supports (display:grid) {
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
#pfe-navi= gation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles,=
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles { d= isplay: grid; gap:
var(\--pfe-navigation\--gutter,32px); grid-auto-flow: row;=
grid-template-columns: repeat(4, minmax(0px, 1fr)); } } }
.pfe-navigation\--collapse-main-menu
#pfe-navigation.pfe-navigation\--process= ed .pfe-navigation-grid,
.pfe-navigation\--collapse-main-menu #pfe-navigatio=
n.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles, .pfe=
-navigation\--collapse-main-menu
pfe-navigation.pfe-navigation\--processed .p= fe-navigation-grid,
.pfe-navigation\--collapse-main-menu pfe-navigation.pfe-=
navigation\--processed .pfe-navigation\_\_dropdown\--default-styles {
column-co= unt: 3; display: block; gap:
var(\--pfe-navigation\--gutter,32px); padding-bo= ttom: 12px;
padding-top: 12px; } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed .pfe-navigation-grid,
.pfe-navigation\--collapse-secondary-links #p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-= styles,
.pfe-navigation\--collapse-secondary-links pfe-navigation.pfe-naviga=
tion\--processed .pfe-navigation-grid,
.pfe-navigation\--collapse-secondary-l= inks
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--de= fault-styles { column-count: auto;
display: block; gap: 0px; margin-left: -= 16px; margin-right: -16px;
max-width: var(\--pfe-navigation\--content-max-wid= th,1136px);
padding-bottom: 12px; padding-top: 12px; width: calc(100% + 32p= x); }
.pfe-navigation\_\_menu-item\--open
#pfe-navigation.pfe-navigation\--processed = .pfe-navigation-grid,
.pfe-navigation\_\_menu-item\--open #pfe-navigation.pfe-=
navigation\--processed .pfe-navigation\_\_dropdown\--default-styles,
.pfe-navig= ation\_\_menu-item\--open
pfe-navigation.pfe-navigation\--processed .pfe-naviga= tion-grid,
.pfe-navigation\_\_menu-item\--open pfe-navigation.pfe-navigation\--=
processed .pfe-navigation\_\_dropdown\--default-styles {
transition-delay: 0s;= visibility: visible; }
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*,
#pfe-na= vigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-style= s \> \*,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*, p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-= styles \> \* { margin: 0px 0px
18px; break-inside: avoid; } \@media (min-width: 1200px) {
#pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*,
#pfe-= navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-sty= les \> \*,
pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid \> \*,=
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--defaul= t-styles \> \* { margin: 0px; } }
.pfe-navigation\--collapse-main-menu
#pfe-navigation.pfe-navigation\--process= ed .pfe-navigation-grid \> \*,
.pfe-navigation\--collapse-main-menu #pfe-navig=
ation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles \>= \*,
.pfe-navigation\--collapse-main-menu
pfe-navigation.pfe-navigation\--proc= essed .pfe-navigation-grid \> \*,
.pfe-navigation\--collapse-main-menu pfe-nav=
igation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--default-styles= \> \* { margin: 0px 0px
18px; } #pfe-navigation.pfe-navigation\--processed .pfe-navigation-grid,
pfe-navigat= ion.pfe-navigation\--processed .pfe-navigation-grid {
max-width: 100%; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--1-x, p=
fe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown\--1-x { di= splay: block; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown,
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_site-switcher .pfe-navigation\_\_dropdown { background:
rgb(255, 255,= 255); } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown
site-switcher, pfe-navigation.pfe-navigation\--proce= ssed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switcher= { margin-left: auto; margin-right: auto; max-width:
var(\--pfe-navigation\--= content-max-width,1136px); padding: 12px
var(\--pfe-navigation\_\_dropdown\--fu=
ll-width\--spacing\--mobile,24px); } \@media (min-width: 1200px) {
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher = .pfe-navigation\_\_dropdown
site-switcher, pfe-navigation.pfe-navigation\--pro= cessed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switch= er { padding: 32px
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--des=
ktop,64px); } } .pfe-navigation\--collapse-main-menu
#pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switcher, = .pfe-navigation\--collapse-main-menu
pfe-navigation.pfe-navigation\--processe= d
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown
site-switcher { = padding: 12px
var(\--pfe-navigation\_\_dropdown\--full-width\--spacing\--mobile,2=
4px); } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_site-switcher .p= fe-navigation\_\_dropdown
site-switcher .container, pfe-navigation.pfe-naviga= tion\--processed
.pfe-navigation\_\_site-switcher .pfe-navigation\_\_dropdown si=
te-switcher .container { margin: 0px; padding: 0px; width: auto; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--invisible\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navigatio=
n\_\_dropdown-wrapper\--invisible\[class\] { padding: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_dropdown-wrapper= \--invisible
pfe-navigation-dropdown, pfe-navigation.pfe-navigation\--process= ed
.pfe-navigation\_\_dropdown-wrapper\--invisible pfe-navigation-dropdown
{ v= isibility: hidden; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown-= -single-column\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-naviga=
tion\_\_custom-dropdown\--single-column\[class\] { padding: 0px; }
\@media (min-width: 768px) { #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdow= n\--single-column\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_custom-dropdown\--single-column\[class\] { box-shadow:
var(\--pfe-navig= ation\_\_dropdown\--BoxShadow,0 1px 2px
rgba(0,0,0,.12)); max-width: 100%; min= -width: 13em; padding: 0px 32px;
position: absolute; top: 100%; } }
.pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation\_\_custom-dropdown\--single-column\[class\], .pfe-navig=
ation\--collapse-secondary-links
pfe-navigation.pfe-navigation\--processed .p=
fe-navigation\_\_custom-dropdown\--single-column\[class\] { box-shadow:
none; ma= x-width: 100%; position: static; } \@media (min-width: 768px)
{ #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdow= n\--single-column\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navi=
gation\_\_custom-dropdown\--single-column\[class\] { right: 0px; } }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown-= -full\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_cus=
tom-dropdown\--full\[class\] { width: 100%; } \@media (min-width: 768px)
{ #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdow= n\--full\[class\],
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_c=
ustom-dropdown\--full\[class\] { left: 0px; position: absolute; right:
0px; } } .pfe-navigation\--collapse-secondary-links
#pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation\_\_custom-dropdown\--full\[class\],
.pfe-navigation\--co= llapse-secondary-links
pfe-navigation.pfe-navigation\--processed .pfe-naviga=
tion\_\_custom-dropdown\--full\[class\] { position: static; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_custom-dropdown-= -full\[class\]
.pfe-navigation\_\_dropdown, pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_custom-dropdown\--full\[class\]
.pfe-navigation\_\_dropdo= wn { width: 100%; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_search\--d=
efault-styles { padding-left: 16px; padding-right: 16px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles form,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_sear=
ch\--default-styles form { align-items: center; display: flex; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button,
#pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_s=
earch\--default-styles input, pfe-navigation.pfe-navigation\--processed
.pfe-= navigation\_\_search\--default-styles button,
pfe-navigation.pfe-navigation\--p= rocessed
.pfe-navigation\_\_search\--default-styles input { padding: 10px; tra=
nsition: box-shadow 0.2s; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_sea=
rch\--default-styles input { border-width: 1px; border-style: solid;
border-= color: rgb(240, 240, 240) rgb(240, 240, 240) rgb(139, 142,
145); border-ima= ge: initial; color: rgb(113, 117, 121); flex: 1 1 0%;
font-size: var(\--pf-g= lobal\--FontSize\--md,1rem); margin-right: 8px;
} #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input::placeholder,
pfe-navigation.pfe-navigation\--processed .pfe-na=
vigation\_\_search\--default-styles input::placeholder { color: rgb(113,
117, = 121); } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_se=
arch\--default-styles button { background-color: rgb(238, 0, 0); border:
1px= solid rgb(238, 0, 0); border-radius: 2px; color: rgb(255, 255,
255); flex:= 0 1 auto; font-size:
var(\--pf-global\--FontSize\--md,1rem); }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigati=
on\_\_search\--default-styles input:hover,
pfe-navigation.pfe-navigation\--proc= essed
.pfe-navigation\_\_search\--default-styles input:focus,
pfe-navigation.p= fe-navigation\--processed
.pfe-navigation\_\_search\--default-styles input:hove= r { outline: 0px;
} #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles input:focus::after,
#pfe-navigation.pfe-navigation\--processed .pfe-n=
avigation\_\_search\--default-styles input:hover::after,
pfe-navigation.pfe-na= vigation\--processed
.pfe-navigation\_\_search\--default-styles input:focus::af= ter,
pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--defa= ult-styles input:hover::after {
border: 1px dashed rgb(0, 0, 0); inset: 0px= ; content: \"\"; display:
block; position: absolute; } #pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button:focus,
#pfe-navigation.pfe-navigation\--processed .pfe-navigat=
ion\_\_search\--default-styles button:hover,
pfe-navigation.pfe-navigation\--pr= ocessed
.pfe-navigation\_\_search\--default-styles button:focus, pfe-navigatio=
n.pfe-navigation\--processed .pfe-navigation\_\_search\--default-styles
button:= hover { outline: 0px; }
#pfe-navigation.pfe-navigation\--processed
.pfe-navigation\_\_search\--default-= styles button:focus::after,
#pfe-navigation.pfe-navigation\--processed .pfe-=
navigation\_\_search\--default-styles button:hover::after,
pfe-navigation.pfe-= navigation\--processed
.pfe-navigation\_\_search\--default-styles button:focus:= :after,
pfe-navigation.pfe-navigation\--processed .pfe-navigation\_\_search\--d=
efault-styles button:hover::after { border: 1px dashed rgb(255, 255,
255); = inset: 0px; content: \"\"; display: block; position: absolute; }
#pfe-navigation .pfe-navigation\_\_site-switcher\_\_back-wrapper,
pfe-navigatio= n .pfe-navigation\_\_site-switcher\_\_back-wrapper {
border-bottom: var(\--pfe-n=
avigation\_\_dropdown\--separator\--Border,1px solid
var(\--pfe-theme\--color\--ui= \--border\--lighter,#d2d2d2)); display:
block; } \@media (min-width: 768px) { #pfe-navigation
.pfe-navigation\_\_site-switcher\_\_back-wrapper, pfe-navigat= ion
.pfe-navigation\_\_site-switcher\_\_back-wrapper { display: none; } }
.pfe-navigation\--collapse-secondary-links #pfe-navigation
.pfe-navigation\_\_= site-switcher\_\_back-wrapper,
.pfe-navigation\--collapse-secondary-links pfe-= navigation
.pfe-navigation\_\_site-switcher\_\_back-wrapper { display: block; }
#pfe-navigation .pfe-navigation\_\_site-switcher\_\_back-button,
pfe-navigation= .pfe-navigation\_\_site-switcher\_\_back-button {
background-color: transparen= t; border: 1px solid transparent; color:
var(\--pfe-navigation\_\_dropdown\--li=
nk\--Color,var(\--pfe-theme\--color\--link,#06c)); cursor: pointer;
font-size: = var(\--pf-global\--FontSize\--md,1rem); padding: 21px 21px
21px 45px; position= : relative; text-align: left; width: 100%; }
#pfe-navigation .pfe-navigation\_\_site-switcher\_\_back-button::before,
pfe-na= vigation .pfe-navigation\_\_site-switcher\_\_back-button::before
{ border-botto= m-color: ; border-bottom-style: ; border-bottom-width: ;
border-left-color:= ; border-left-style: ; border-left-width: ;
border-image-source: ; border-= image-slice: ; border-image-width: ;
border-image-outset: ; border-image-re= peat: ; border-right: 0px;
border-top: 0px; content: \"\"; display: block; he= ight: 8px; left:
35px; position: absolute; right: auto; top: 27px; transfor= m:
rotate(45deg); transform-origin: left top; width: 8px; } #pfe-navigation
.pfe-navigation\_\_site-switcher\_\_back-button:focus, #pfe-nav= igation
.pfe-navigation\_\_site-switcher\_\_back-button:hover, pfe-navigation .=
pfe-navigation\_\_site-switcher\_\_back-button:focus, pfe-navigation
.pfe-navig= ation\_\_site-switcher\_\_back-button:hover { border: 1px
dashed var(\--pfe-navi= gation\_\_dropdown\--Color,#151515); color:
var(\--pfe-navigation\_\_dropdown\--li= nk\--Color\--hover,#036);
outline: 0px; } #pfe-navigation.pfe-navigation\--processed
site-switcher, pfe-navigation.pfe= -navigation\--processed site-switcher
{ columns: auto; display: block; }
#pfe-navigation.pfe-navigation\--stuck,
pfe-navigation.pfe-navigation\--stuck= { left: 0px; position: fixed;
top: 0px; width: 100%; z-index: var(\--pfe-th=
eme\--zindex\--navigation,95); }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_outer-me= nu-wrapper\_\_inner,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-na=
vigation\_\_outer-menu-wrapper\_\_inner { opacity: 1 !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
pfe-navigation-account, #=
pfe-navigation.pfe-navigation\--in-crusty-browser rh-account-dropdown,
pfe-n= avigation.pfe-navigation\--in-crusty-browser
pfe-navigation-account, pfe-nav=
igation.pfe-navigation\--in-crusty-browser rh-account-dropdown {
display: no= ne !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser\[open-toggle=3D\"pfe-naviga=
tion\_\_account-toggle\"\] pfe-navigation-account,
#pfe-navigation.pfe-navigati=
on\--in-crusty-browser\[open-toggle=3D\"pfe-navigation\_\_account-toggle\"\]
rh-ac= count-dropdown,
pfe-navigation.pfe-navigation\--in-crusty-browser\[open-toggl=
e=3D\"pfe-navigation\_\_account-toggle\"\] pfe-navigation-account,
pfe-navigatio=
n.pfe-navigation\--in-crusty-browser\[open-toggle=3D\"pfe-navigation\_\_account-=
toggle\"\] rh-account-dropdown { display: block !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-ite= m,
pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-i= tem { display: block; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-lin= k\[aria-expanded=3D\"true\"\],
pfe-navigation.pfe-navigation\--in-crusty-browser=
.pfe-navigation\_\_menu-link\[aria-expanded=3D\"true\"\] {
\--pfe-icon\--color: va=
r(\--pfe-navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme\--color\--text,#15=
1515)); background:
var(\--pfe-navigation\_\_nav-bar\--toggle\--BackgroundColor-=
-active,var(\--pfe-theme\--color\--surface\--lightest,#fff)); color:
var(\--pfe-=
navigation\_\_nav-bar\--Color\--active,var(\--pfe-theme\--color\--text,#151515));
= } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-lin= k\[aria-expanded=3D\"true\"\]:focus,
pfe-navigation.pfe-navigation\--in-crusty-b= rowser
.pfe-navigation\_\_menu-link\[aria-expanded=3D\"true\"\]:focus {
outline: = 0px; } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_menu-lin= k\[aria-expanded=3D\"true\"\]:focus::after,
pfe-navigation.pfe-navigation\--in-c= rusty-browser
.pfe-navigation\_\_menu-link\[aria-expanded=3D\"true\"\]:focus::aft= er
{ border: 1px dashed; inset: 0px; content: \"\"; display: block;
position:= absolute; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= ,
pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdow= n { display: flex; flex-wrap: wrap; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= \> .style-scope,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navi=
gation\_\_dropdown \> .style-scope { flex-basis: 25%; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= .pfe-navigation\_\_footer.style-scope,
pfe-navigation.pfe-navigation\--in-cru= sty-browser
.pfe-navigation\_\_dropdown .pfe-navigation\_\_footer.style-scope {=
flex-basis: 100%; } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= .pfe-navigation\_\_footer.style-scope \>
.style-scope, pfe-navigation.pfe-nav= igation\--in-crusty-browser
.pfe-navigation\_\_dropdown .pfe-navigation\_\_foote= r.style-scope \>
.style-scope { margin-right: 16px; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= \--single-column,
#pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-nav=
igation\_\_dropdown\--single-column ul,
#pfe-navigation.pfe-navigation\--in-cru= sty-browser
.pfe-navigation\_\_dropdown\--single-column \> .style-scope, pfe-na=
vigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown\--singl= e-column,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigation\_=
\_dropdown\--single-column ul,
pfe-navigation.pfe-navigation\--in-crusty-brows= er
.pfe-navigation\_\_dropdown\--single-column \> .style-scope { display:
flex;= flex-flow: column; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_dropdown= \--single-column \> .style-scope,
pfe-navigation.pfe-navigation\--in-crusty-br= owser
.pfe-navigation\_\_dropdown\--single-column \> .style-scope {
flex-basis:= auto; } #pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_search-t= oggle,
#pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigation\_\_s=
econdary-link, #pfe-navigation.pfe-navigation\--in-crusty-browser
\[slot=3D\"s= econdary-links\"\] \> a,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe=
-navigation\_\_search-toggle,
pfe-navigation.pfe-navigation\--in-crusty-browse= r
.pfe-navigation\_\_secondary-link,
pfe-navigation.pfe-navigation\--in-crusty= -browser
\[slot=3D\"secondary-links\"\] \> a { color: rgb(255, 255, 255) !import=
ant; justify-content: center !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_search-t= oggle\[aria-expanded=3D\"true\"\],
#pfe-navigation.pfe-navigation\--in-crusty-br= owser
.pfe-navigation\_\_secondary-link\[aria-expanded=3D\"true\"\],
#pfe-navigat= ion.pfe-navigation\--in-crusty-browser
\[slot=3D\"secondary-links\"\] \> a\[aria-e= xpanded=3D\"true\"\],
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-na=
vigation\_\_search-toggle\[aria-expanded=3D\"true\"\],
pfe-navigation.pfe-navigat= ion\--in-crusty-browser
.pfe-navigation\_\_secondary-link\[aria-expanded=3D\"tru= e\"\],
pfe-navigation.pfe-navigation\--in-crusty-browser
\[slot=3D\"secondary-li= nks\"\] \> a\[aria-expanded=3D\"true\"\] {
color: rgb(21, 21, 21) !important; }
#pfe-navigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_account-= wrapper\--logged-in
.pfe-navigation\_\_log-in-link, #pfe-navigation.pfe-naviga=
tion\--in-crusty-browser .pfe-navigation\_\_search-toggle
.secondary-link\_\_ico= n-wrapper,
#pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigatio=
n\_\_search-toggle pfe-icon,
#pfe-navigation.pfe-navigation\--in-crusty-browse= r
.pfe-navigation\_\_secondary-link .secondary-link\_\_icon-wrapper,
#pfe-navig= ation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_secondary-link pfe= -icon,
#pfe-navigation.pfe-navigation\--in-crusty-browser \[slot=3D\"secondary=
-links\"\] \> a .secondary-link\_\_icon-wrapper,
#pfe-navigation.pfe-navigation-= -in-crusty-browser
\[slot=3D\"secondary-links\"\] \> a pfe-icon, pfe-navigation.=
pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_account-wrapper\--logged-= in
.pfe-navigation\_\_log-in-link,
pfe-navigation.pfe-navigation\--in-crusty-b= rowser
.pfe-navigation\_\_search-toggle .secondary-link\_\_icon-wrapper,
pfe-na= vigation.pfe-navigation\--in-crusty-browser
.pfe-navigation\_\_search-toggle p= fe-icon,
pfe-navigation.pfe-navigation\--in-crusty-browser .pfe-navigation\_\_=
secondary-link .secondary-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation= \--in-crusty-browser
.pfe-navigation\_\_secondary-link pfe-icon, pfe-navigatio=
n.pfe-navigation\--in-crusty-browser \[slot=3D\"secondary-links\"\] \> a
.seconda= ry-link\_\_icon-wrapper,
pfe-navigation.pfe-navigation\--in-crusty-browser \[sl=
ot=3D\"secondary-links\"\] \> a pfe-icon { display: none !important; }
\[id=3D\"pfe-navigation\_\_account-dropdown\"\]\[class\]\[class\] {
display: block; h= eight: auto; left: 0px; padding: 0px; position:
absolute; top: var(\--pfe-na= vigation\_\_nav-bar\--Height,72px); width:
100%; }
\[id=3D\"pfe-navigation\_\_account-dropdown\"\].pfe-navigation\_\_dropdown-wrapper-=
-invisible\[class\] { display: none; }
.pfe-navigation\_\_dropdown-wrapper { overflow: hidden; } \@media
(min-width: 768px) { .pfe-navigation\_\_custom-dropdown\--single-column
{ min-width: 25em; } } .pfe-navigation\--collapse-secondary-links
.pfe-navigation\_\_custom-dropdown-= -single-column { min-width: 0px; }
.secondary-link\_\_icon-wrapper { align-items: center; display: flex;
justify= -content: center; } .secondary-link\_\_alert-count {
background: var(\--pfe-navigation\_\_nav-bar\--a=
lert-color,var(\--pfe-theme\--color\--link,#06c)); border-radius: 20px;
color:=
var(\--pfe-navigation\_\_nav-bar\--Color\--on-highlight,var(\--pfe-theme\--color-=
-text\--on-saturated,#fff)); display: block; font-size:
var(\--pfe-navigation= \--FontSize\--xs,12px); line-height: 20px;
margin: 0px 4px 0px 2px; min-width= : 23px; overflow: hidden; padding:
0px 8px; } .secondary-link\_\_alert-count:empty { display: none; }
#pfe-navigation\_\_1x-skip-links { left: 0px; position: absolute; top:
0px; } #pfe-navigation\_\_1x-skip-links,
#pfe-navigation\_\_1x-skip-links li { height:= 0px; list-style: none;
margin: 0px; padding: 0px; width: 0px; } .skip-link\[class\]\[class\] {
font-size: var(\--pf-global\--FontSize\--sm,.875rem= ); line-height:
18px; } .skip-link\[class\]\[class\]:focus { border-radius: 0.21429em;
height: auto; le= ft: 50%; padding: 0.42857em 0.57143em; position:
fixed; top: 8px; transform= : translate(-50%); width: auto; z-index:
99999; clip: auto; background: var=
(\--pfe-navigation\_\_skip-link\--BackgroundColor,var(\--pfe-theme\--color\--surfa=
ce\--lightest,#fff)); color:
var(\--pfe-navigation\_\_skip-link\--Color,var(\--pf=
e-theme\--color\--link,#06c)); text-decoration: none; } pfe-navigation
pfe-navigation-account\[slot=3D\"account\"\] { background: var(-=
-pfe-navigation\_\_dropdown\--Background,var(\--pfe-theme\--color\--surface\--ligh=
test,#fff)); width: 100%; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-ccbcedbe-eba7-45c6-8d5e-49008519b3e0@mhtml.blink \@charset
\"utf-8\"; .pfe-navigation-default-container\[data-v-b258bd1d\] {
position: sticky; top:= 0px; z-index: 100; }
pfe-navigation\[data-v-b258bd1d\]::part(pfe-navigation\_\_search-wrapper\--md),
=
pfe-navigation\[data-v-b258bd1d\]::part(secondary-links\_\_button\--search)
{ di= splay: none; } .search-btn\[data-v-b258bd1d\] { align-items:
center; background-color: var(-= -rh-color-canvas-black,#151515);
border: 3px solid var(\--rh-color-canvas-bl= ack,#151515); cursor:
pointer; display: flex; flex-direction: column; heigh= t: 100%;
justify-content: center; outline: none; padding: 14px var(\--rh-spa=
ce-md,8px); } .search-btn\[data-v-b258bd1d\]:focus { border-top: 3px
solid var(\--rh-color-a= ccent-brand-on-light,#e00); outline: 2px dotted
var(\--rh-color-white,#fff);= } .search-btn
.search-icon\[data-v-b258bd1d\] { height: 26px; padding: 2px 0 va=
r(\--rh-space-xs,4px); width: 20px; } .search-btn
.search-icon\[data-v-b258bd1d\], .search-icon-helper-text\[data-v-=
b258bd1d\] { color: var(\--rh-color-white,#fff); }
.search-mobile\[data-v-b258bd1d\] { margin-bottom:
var(\--rh-space-2xl,32px); = } .search-mobile form\[data-v-b258bd1d\] {
display: flex; gap: var(\--rh-space-m= d,8px); margin: auto; }
.search-box\[data-v-b258bd1d\] { width: 35rem; } nav\[data-v-b258bd1d\]
{ background-color: rgb(21, 21, 21); justify-content: = space-between;
width: 100%; } a\[data-v-b258bd1d\], a\[data-v-b258bd1d\]:visited {
color: rgb(255, 255, 255);= display: inline-block; font-size:
var(\--rh-font-size-body-text-md,1rem); }
.skip-link\[class\]\[class\]\[data-v-b258bd1d\] { font-size:
var(\--pf-global\--Fon= tSize\--sm,.875rem); line-height: 18px; }
.skip-link\[class\]\[class\]\[data-v-b258bd1d\]:focus { border-radius:
0.21429em;= height: auto; left: 50%; padding: 0.42857em 0.57143em;
position: fixed; to= p: 8px; transform: translate(-50%); width: auto;
z-index: 99999; clip: auto= ; background: var(
\--pfe-navigation\_\_skip-link\--BackgroundColor,var(\--pfe-t=
heme\--color\--surface\--lightest,#fff) ); color: var(
\--pfe-navigation\_\_skip-=
link\--Color,var(\--pfe-theme\--color\--link,#06c) ); text-decoration:
none; } .visually-hidden\[data-v-b258bd1d\] { border: 1px solid rgb(0,
102, 204); hei= ght: 1px; overflow: hidden; padding: 0px; position:
absolute; width: 1px; c= lip: rect(0px, 0px, 0px, 0px); white-space:
nowrap; } h3\[data-v-b258bd1d\] { color:
light-dark(var(\--rh-color-text-primary-on-ligh=
t,#151515),var(\--rh-color-text-primary-on-dark,#fff)); font-family:
var( \--= rh-font-family-heading,\"Red Hat
Display\",Helvetica,Arial,sans-serif ); font= -size:
var(\--rh-font-size-body-text-lg,1.125rem); }
.language-picker\[data-v-b258bd1d\] { align-items: center;
background-color: =
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-dar=
ker,#1f1f1f)); display: flex; flex-direction: column; padding:
var(\--rh-spa= ce-xl,24px); width: 100%; } .language-picker
h3\[data-v-b258bd1d\] { margin: 0px; padding: 0px 1rem 1rem;= }
.language-picker ul\[data-v-b258bd1d\] { margin: 0px; padding: 0px; }
.language-picker a\[data-v-b258bd1d\] { color:
light-dark(var(\--rh-color-inte=
ractive-primary-default-on-light,#06c),var(\--rh-color-interactive-primary-d=
efault-on-dark,#92c5f9)); } .language-picker a\[data-v-b258bd1d\]:hover
{ color: light-dark(var(\--rh-colo=
r-interactive-primary-hover-on-light,#036),var(\--rh-color-interactive-prima=
ry-hover-on-dark,#b9dafc)); } .language-picker li\[data-v-b258bd1d\] {
list-style: none; } .language-dropdown\[data-v-b258bd1d\] { background:
rgb(255, 255, 255); box-s= hadow: rgba(0, 0, 0, 0.098) 0px 3px 6px;
position: absolute; right: 0px; wi= dth: 100%; z-index: 104; display:
block !important; } .pfe-navigation.pfe-navigation\--processed \>
\[slot=3D\"secondary-links\"\]\[data= -v-b258bd1d\] { height: auto;
overflow: visible; visibility: visible; width:= auto; }
\[slot=3D\"secondary-links\"\]\[data-v-b258bd1d\] { background-color:
light-dark(=
var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f=
)); } .upper-navigation\[data-v-b258bd1d\] { padding: 0
var(\--rh-space-2xl,32px); } .upper-nav-container\[data-v-b258bd1d\] {
border-bottom: 1px solid rgb(64, 64= , 64); margin: 0px; }
.upper-nav-hidden\[data-v-b258bd1d\]:not(:focus):not(:active) { clip:
rect(0p= x, 0px, 0px, 0px); clip-path: inset(50%); height: 1px;
overflow: hidden; po= sition: absolute; white-space: nowrap; width: 1px;
} .upper-nav-menu\[data-v-b258bd1d\] { align-items: center; display:
flex; just= ify-content: flex-end; line-height: 1.444; list-style: none;
margin-bottom:= 0px; margin-top: 0px; padding-left: 0px; }
.upper-nav-menu\[data-v-b258bd1d\], .upper-nav-menu \>
li\[data-v-b258bd1d\] { p= osition: relative; } .upper-nav-menu \>
li:not(:first-child) \> a\[data-v-b258bd1d\]::before, .upper= -nav-menu
\> li:not(:first-child) \> button\[data-v-b258bd1d\]::before { backgr=
ound-color: rgb(64, 64, 64); content: \"\"; height: 40%; left: 0px;
position:= absolute; top: 30%; width: 1px; } li\[data-v-b258bd1d\] {
display: list-item; margin: 0px; padding: 0px; text-a= lign:
-webkit-match-parent; } .upper-nav-menu
button.upper-nav-links\[data-v-b258bd1d\] { border-width: 3px= 0px 0px;
border-right-style: initial; border-bottom-style: initial; border=
-left-style: initial; border-right-color: initial; border-bottom-color:
ini= tial; border-left-color: initial; border-image: initial;
border-top-style: = solid; border-top-color: transparent; cursor:
pointer; line-height: 1.444; = } .upper-nav-menu
button.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258b= d1d\]
{ outline-color: rgb(21, 21, 21); } .upper-nav-menu
button.upper-nav-links\[aria-expanded=3D\"true\"\] .upper-nav-a=
rrow\[data-v-b258bd1d\] { filter: invert(0) sepia(2%) saturate(21%)
hue-rotat= e(257deg) brightness(108%) contrast(100%); transform:
rotate(270deg); } .upper-nav-menu
button.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258b=
d1d\]::before { display: none; } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\] { background-color: var( =
\--pfe-navigation\--BackgroundColor,var(\--pfe-theme\--color\--surface\--darkest,=
#151515) ); border-top: 3px solid transparent; color: rgb(255, 255,
255); d= isplay: block; font-family: var(
\--rh-font-family-body-text,\"Red Hat Text\",=
\"RedHatText\",Arial,sans-serif ); font-size:
var(\--rh-font-size-body-text-sm= ,.875rem); outline: none; padding:
12px 12px 14px; text-decoration: none; } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\]:hover { border-top-color:= rgb(184,
187, 190); } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\]:focus-within { outline: 1= px dashed
var(\--rh-color-white,#fff); outline-offset: -1px; } .upper-nav-menu
.upper-nav-links\[data-v-b258bd1d\]:focus-within::before { di= splay:
none; } .upper-nav-dropdown-container\[data-v-b258bd1d\] { background:
light-dark(var=
(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));=
box-shadow: rgba(0, 0, 0, 0.098) 0px 3px 6px; display: none; padding:
5px = 30px 24px; position: absolute; right: 0px; top: 100%; width:
500px; z-index= : 105; } .upper-nav-dropdown-container \>
ul\[data-v-b258bd1d\] { column-count: 2; list= -style-type: none;
padding: 0px; width: auto; } .upper-nav-dropdown-container \> ul
li\[data-v-b258bd1d\] { color: rgb(21, 21,= 21); font-family: var(
\--rh-font-family-heading,\"Red Hat Display\",Helvetic=
a,Arial,sans-serif ); font-size:
var(\--rh-font-size-body-text-sm,.875rem); = list-style-type: none;
margin-bottom: 0px; } .upper-nav-dropdown-container \> ul li
span\[data-v-b258bd1d\] { color: light-=
dark(var(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-text-prim=
ary-on-dark,#fff)); font-weight:
var(\--rh-font-weight-body-text-medium,500)= ; }
.upper-nav-dropdown-container \> ul ul\[data-v-b258bd1d\] {
padding-left: 0px;= padding-top: 9px; } .upper-nav-dropdown-container \>
ul \> li\[data-v-b258bd1d\] { padding-top: 19p= x; break-inside: avoid;
} .upper-nav-dropdown-container \> ul \> li \> ul \>
li\[data-v-b258bd1d\] { line-h= eight: 1.45; padding: 4px 0px; }
.upper-nav-menu .upper-nav-arrow\[data-v-b258bd1d\] { display:
inline-block; = filter: invert(100%) sepia(8%) saturate(7%)
hue-rotate(1turn) brightness(10= 0%) contrast(93%); height: 18px;
margin-left: 5px; transform: rotate(90deg)= ; vertical-align: middle;
width: 8px; } #pfe-navigation\_\_secondary-links
.show\[data-v-b258bd1d\], .upper-navigation = .show\[data-v-b258bd1d\] {
display: block; } .upper-nav-menu
.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258bd1d\]:a=
ctive, .upper-nav-menu
.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258= bd1d\]:focus,
.upper-nav-menu .upper-nav-links\[aria-expanded=3D\"true\"\]\[data-=
v-b258bd1d\]:hover { background-color: rgb(255, 255, 255); color:
rgb(21, 21= , 21); } .upper-nav-menu
.upper-nav-links\[aria-expanded=3D\"true\"\]\[data-v-b258bd1d\] {=
background-color: rgb(255, 255, 255); border-top-color: rgb(184, 187,
190)= ; color: rgb(0, 0, 0); position: relative; z-index: 1; }
.upper-nav-dropdown-container \> ul a\[data-v-b258bd1d\] { color:
light-dark(v=
ar(\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh-color-int=
eractive-primary-default-on-dark,#92c5f9)); font-family: var(
\--rh-font-fam= ily-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif ); font-size: 14= px;
text-decoration: none; } select\[data-v-b258bd1d\] { background-image:
url(\"data:image/svg+xml;charset= =3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'10\' height=3D= \'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%23151515\'
d=3D\'M.= 678 0h8.644c.596 0 .895.797.497 1.195l-4.372
4.58c-.298.3-.695.3-.993 0L.18= 1.196C-.216.797.081 0 .678
0\'/%3E%3C/svg%3E\"); } .pfe-navigation\_\_search\[data-v-b258bd1d\] {
background-color: var(\--rh-color= -white,#fff); }
.pfe-navigation\_\_search form\[data-v-b258bd1d\] { display: flex; gap:
var(\--r= h-space-md,8px); margin: auto; max-width: 992px; }
pfe-navigation \[slot=3D\"secondary-links\"\]
.buttons\[data-v-b258bd1d\] { displ= ay: flex; flex-wrap: wrap; gap:
var(\--rh-space-md,8px); margin-top: 4px; } pfe-navigation
\[slot=3D\"secondary-links\"\] .buttons\[data-v-b258bd1d\] :first-=
child { flex: 1 0 100%; } pfe-navigation \[slot=3D\"secondary-links\"\]
.buttons a\[data-v-b258bd1d\] { bor= der: 1px solid
light-dark(#d2d2d2,var(\--rh-color-border-subtle-on-dark,#707= 070));
border-radius: 3px; color: light-dark(var(\--rh-color-interactive-pri=
mary-default-on-light,#06c),var(\--rh-color-interactive-primary-default-on-d=
ark,#92c5f9)); cursor: pointer; flex-basis: calc(50% - 5px);
font-family: v= ar( \--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif= ); font-weight:
var(\--rh-font-weight-code-regular,400); padding: 1em; text= -align:
center; text-decoration: none; } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select\[data-v-b258bd= 1d\]
{ border-top-color: ; border-top-style: ; border-top-width: ; border-ri=
ght-color: ; border-right-style: ; border-right-width: ;
border-bottom-styl= e: ; border-bottom-width: ; border-left-color: ;
border-left-style: ; borde= r-left-width: ; border-image-source: ;
border-image-slice: ; border-image-w= idth: ; border-image-outset: ;
border-image-repeat: ; border-bottom-color: =
light-dark(#3c3f42,var(\--rh-color-gray-50,#707070)); cursor: pointer;
displ= ay: flex; margin: 3rem 0px; position: relative; } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select label\[data-v-=
b258bd1d\] { bottom: 100%; font-size: 14px; font-weight: 500;
margin-bottom:= 5px; position: absolute; } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select label\[data-v-=
b258bd1d\], pfe-navigation \[slot=3D\"secondary-links\"\]
.mobile-lang-select se= lect\[data-v-b258bd1d\] { color:
light-dark(var(\--rh-color-text-primary-on-li=
ght,#151515),var(\--rh-color-text-primary-on-dark,#fff)); font-family:
var( = \--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,sans-serif ); = } pfe-navigation
\[slot=3D\"secondary-links\"\] .mobile-lang-select select\[data-v=
-b258bd1d\] { appearance: none; background-color:
light-dark(#fff,var(\--rh-c= olor-gray-80,#292929)); border-style: none;
flex-basis: 100%; font-size: 16= px; line-height: 24px; padding: 6px
24px 6px 8px; } select\[data-v-b258bd1d\] { background-image:
var(\--header-select); backgroun= d-position: 98% 50%;
background-repeat: no-repeat; } #inputLabel\[data-v-b258bd1d\] {
align-items: center; display: flex; position= : relative; } #inputLabel
form\[data-v-b258bd1d\] { width: 100%; } .input-box\[data-v-b258bd1d\] {
font-family: var( \--rh-font-family-body-text,= \"Red Hat
Text\",\"RedHatText\",Arial,sans-serif ); font-size: var(\--rh-font-si=
ze-body-text-md,1rem); height: 36px; padding: 0px 8px; width: 100%; }
.input-box\[data-v-b258bd1d\]::placeholder { color: rgb(106, 110, 115);
font-= family: var( \--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatText\",Arial,s= ans-serif ); font-size:
var(\--rh-font-size-body-text-md,1rem); font-weight:=
var(\--rh-font-weight-code-regular,400); line-height: 24px; }
.pfe-navigation\_\_custom-nav-container\[data-v-b258bd1d\] { padding: 0
0 var(-= -rh-space-lg,16px) 0; } .spacing-32\[data-v-b258bd1d\] { gap:
var(\--rh-space-2xl,32px); } h2.pfe-menu-item-heading\[data-v-b258bd1d\]
{ color: light-dark(var(\--rh-colo=
r-text-primary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff))=
; font-size: var(\--rh-font-size-body-text-lg,1.125rem); line-height:
27px; = margin: 0px; padding: 0px; }
ul.menu\_\_products-container\[data-v-b258bd1d\] { grid-auto-flow:
column; grid= -template-rows: repeat(3, auto); }
ul.menu\_\_products-container\[data-v-b258bd1d\],
ul.menu\_\_products-container-l= earn\[data-v-b258bd1d\] { display:
grid; gap: var(\--rh-space-2xl,32px); list-= style: none; margin:
var(\--rh-space-2xl,32px) 0 0; padding: 0px; }
ul.menu\_\_products-container-learn\[data-v-b258bd1d\] { grid-auto-flow:
row; g= rid-template-columns: repeat(3, auto); }
a.pfe-navigation\_\_custom-nav-link\[data-v-b258bd1d\] { border: 1px
solid tran= sparent; color:
light-dark(var(\--rh-color-interactive-primary-default-on-li=
ght,#06c),var(\--rh-color-interactive-primary-default-on-dark,#92c5f9));
dis= play: inline-block; }
a.pfe-navigation\_\_custom-nav-link\[data-v-b258bd1d\]:hover {
background: ligh=
t-dark(var(\--rh-color-surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,=
#383838)); outline: 8px solid
light-dark(var(\--rh-color-surface-lighter,#f2=
f2f2),var(\--rh-color-surface-dark,#383838)); }
a.pfe-navigation\_\_custom-nav-link\[data-v-b258bd1d\]:focus { border:
1px dash= ed
light-dark(var(\--rh-color-interactive-primary-default-on-light,#06c),var=
(\--rh-color-interactive-primary-default-on-dark,#92c5f9)); outline:
0px; } .pfe-navigation\_\_custom-nav-title\[data-v-b258bd1d\] { display:
inline-block;= } a.pfe-navigation\_\_custom-nav-link:hover
.pfe-navigation\_\_custom-nav-title\[d= ata-v-b258bd1d\] { color:
light-dark(var(\--rh-color-interactive-primary-hove=
r-on-light,#036),var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc))=
; text-decoration: underline; }
.pfe-navigation\_\_custom-nav-body\[data-v-b258bd1d\] { color:
light-dark(var(-=
-rh-color-text-primary-on-light,#151515),var(\--rh-color-text-primary-on-dar=
k,#fff)); display: inline-block; font-size:
var(\--rh-font-size-body-text-sm= ,.875rem); margin-top:
var(\--rh-space-md,8px); }
ul.menu\_\_use-cases-container\[data-v-b258bd1d\] { list-style: none;
margin: v= ar(\--rh-space-lg,16px) 0 0; padding: 0px; }
a.pfe-list-link\[data-v-b258bd1d\] { border: 1px solid transparent;
color: li=
ght-dark(var(\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh=
-color-interactive-primary-default-on-dark,#92c5f9)); display:
inline-block= ; margin-top: var(\--rh-space-lg,16px); }
a.pfe-list-link\[data-v-b258bd1d\]:hover { color:
light-dark(var(\--rh-color-i=
nteractive-primary-hover-on-light,#036),var(\--rh-color-interactive-primary-=
hover-on-dark,#b9dafc)); text-decoration: underline; }
a.pfe-list-link\[data-v-b258bd1d\]:focus { border: 1px dashed
light-dark(var(=
\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh-color-intera=
ctive-primary-default-on-dark,#92c5f9)); outline: 0px; }
.pfe-navigation\--footer\[data-v-b258bd1d\] { border-top: 1px solid
var(\--rh-c= olor-gray-60,#4d4d4d); margin-top:
var(\--rh-space-3xl,48px); padding-top: v= ar(\--rh-space-3xl,48px); }
pfe-navigation\[data-v-b258bd1d\]::part(mobile\_\_dropdown),
pfe-navigation\[dat=
a-v-b258bd1d\]::part(pfe-navigation\_\_dropdown-wrapper) {
background-color: l=
ight-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-dark=
er,#1f1f1f)); } rh-account-dropdown\[data-v-b258bd1d\] {
\--pfe-navigation\_\_dropdown\--link\--Co= lor:
light-dark(var(\--rh-color-interactive-primary-default-on-light,#06c),v=
ar(\--rh-color-interactive-primary-default-on-dark,#92c5f9));
\--pfe-navigati= on\_\_dropdown\--Color\--secondary:
light-dark(var(\--rh-color-text-primary-on-l=
ight,#151515),var(\--rh-color-text-primary-on-dark,#fff));
\--pfe-navigation\_= \_dropdown\--headings\--Color:
light-dark(var(\--rh-color-text-primary-on-light=
,#151515),var(\--rh-color-text-primary-on-dark,#fff));
\--pfe-navigation\_\_dro= pdown\--link\--Color\--hover:
light-dark(var(\--rh-color-interactive-primary-ho=
ver-on-light,#036),var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc=
)); \--pfe-navigation\_\_dropdown\--highlight-color:
light-dark(#c9190b,#fe5142= ); } \@media (min-width: 767px) {
.pfe-navigation\_\_search form\[data-v-b258bd1d\] { padding:
var(\--rh-space-2= xl,32px) 0; }
\[slot=3D\"secondary-links\"\]\[data-v-b258bd1d\] { background-color:
var(\--rh-= color-surface-darkest,#151515); } } \@media (max-width:
767px) { .right-navigation\[data-v-b258bd1d\],
.upper-navigation\[data-v-b258bd1d\] { = display: none; }
ul.menu\_\_products-container\[data-v-b258bd1d\],
ul.menu\_\_products-container= -learn\[data-v-b258bd1d\] { gap:
var(\--rh-space-2xl,32px); grid-auto-flow: ro= w; grid-template-columns:
1fr; } } \@media (max-width: 960px) { .search-box\[data-v-b258bd1d\] {
width: 28rem; } } \@media (min-width: 768px) and (max-width: 810px) {
.search-box\[data-v-b258bd1d\] { width: 24rem; } } \@media (max-width:
1199px) { .pfe-navigation\_\_custom-nav-container\[data-v-b258bd1d\] {
padding: 0px; } } \@media (min-width: 992px) {
.pfe-navigation-content-page-container\[data-v-b258bd1d\] { position:
stick= y; top: 0px; z-index: 100; } } \@media (min-width: 1200px) {
pfe-navigation\[data-v-b258bd1d\]::part(mobile\_\_dropdown) {
background-colo= r: var(\--rh-color-surface-darkest,#151515); } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-120ee431-c0f4-427d-929f-6adb91d139c8@mhtml.blink \@charset
\"utf-8\"; rh-alert\[data-v-84359384\] { width: 100%; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-7b8aef40-7566-4bf9-a120-d1b4d7dbb4c9@mhtml.blink \@charset
\"utf-8\"; \@keyframes fade-in {=20 0% { opacity: 0; visibility: hidden;
} 1% { visibility: visible; } 100% { opacity: 1; visibility: visible; }
} \@media (min-height: 48em) { .rhdocs { \--rh-table\--maxHeight:
calc(100vh - 12.5rem); } } \*, .rhdocs \*, .rhdocs ::after, .rhdocs
::before, ::after, ::before { box-si= zing: border-box; } .rhdocs img,
.rhdocs object, .rhdocs svg, img, object, svg { display: inlin= e-block;
max-width: 100%; vertical-align: middle; } .rhdocs hr { border-right:
0px; border-bottom: 0px; border-left: 0px; borde= r-image: initial;
border-top: .0625rem solid light-dark(#d2d2d2,var(\--rh-co=
lor-border-subtle-on-dark,#707070)); clear: both; margin: 1rem 0px; }
.rhdocs a { color:
light-dark(var(\--rh-color-interactive-primary-default-on=
-light,#06c),var(\--rh-color-interactive-primary-default-on-dark,#92c5f9));
= text-decoration: underline; } .rhdocs a:focus, .rhdocs a:hover {
color: light-dark(var(\--rh-color-interac=
tive-primary-hover-on-light,#036),var(\--rh-color-interactive-primary-hover-=
on-dark,#b9dafc)); } .rhdocs a.anchor-heading { color:
light-dark(var(\--rh-color-gray-95,#151515=
),var(\--rh-color-white,#fff)); cursor: pointer; text-decoration: none;
word= -break: break-word; } .rhdocs p { margin: 1.49963rem 0px; }
.rhdocs li \> p { margin: 0px; } .rhdocs h1 { font-weight:
var(\--rh-font-weight-heading-regular,400); } .rhdocs h1, .rhdocs h2,
.rhdocs h3, .rhdocs h4, .rhdocs h5, .rhdocs h6 { fo= nt-family:
RedHatDisplay, \"Red Hat Display\", \"Helvetica Neue\", Arial, sans-=
serif; margin: 0px 0px 0.625rem; } .rhdocs h2, .rhdocs h3, .rhdocs h4,
.rhdocs h5, .rhdocs h6 { font-weight: v=
ar(\--rh-font-weight-heading-medium,500); } .rhdocs h1 { font-size:
var(\--rh-font-size-heading-xl,2.5rem); margin: 2rem= 0px; } .rhdocs h2
{ font-size: var(\--rh-font-size-heading-md,1.75rem); margin: 2re= m
0px; } .rhdocs h3 { font-size: var(\--rh-font-size-heading-sm,1.5rem); }
.rhdocs h4 { font-size: var(\--rh-font-size-heading-xs,1.25rem); }
.rhdocs h5 { font-size: 18px; } .rhdocs ol ::marker, .rhdocs ul ::marker
{ font: inherit; } .rhdocs li { margin: 0px 0px 0.5em; padding: 0px; }
.rhdocs li \> p { margin: 0.5rem 0px; } .rhdocs li \> ol, .rhdocs li \>
ul { margin: 0px; } .rhdocs dl dd { margin: 0.5rem 0px 0.5rem 1rem; }
.rhdocs dl dd \> p { margin: 0.5rem 0px; } .rhdocs .informaltable,
.rhdocs .table-contents, .rhdocs .table-wrapper { m= ax-height:
var(\--rh-table\--maxHeight); overflow: auto; } .rhdocs table { border:
0px; font-size: 1rem; line-height: 1.6667; table-la= yout: fixed;
\--rh-table\--hoveredCol\--Background: light-dark(rgba(from var(-=
-rh-color-blue-50,#0066cc) r g b/.1),rgba(from
var(\--rh-color-blue-70,#0033= 66) r g b/.3));
\--rh-table\--hoveredRow\--Background: light-dark(rgba(from va=
r(\--rh-color-gray-40,#a3a3a3) r g b/.1),rgba(from
var(\--rh-color-white,#fff= fff) r g b/.1));
\--rh-table\--hoveredIntersection\--Background: light-dark(#e=
0edf4,#2f3d54); background-color:
light-dark(var(\--rh-color-surface-lightes=
t,#fff),var(\--rh-color-surface-darker,#1f1f1f)); } .rhdocs table
caption { color: rgb(88, 88, 88); margin-bottom: 0.5rem; marg= in-top:
0.5rem; text-align: left; } .rhdocs table td, .rhdocs table th {
border-top: 0px; border-right: 0px; bo= rder-left: 0px; border-image:
initial; border-bottom: .0625rem solid var(\--=
pfe-table\--Border,#d2d2d2); padding: 0.5em 1rem; } .rhdocs table
td.halign-left, .rhdocs table th.halign-left { text-align: le= ft; }
.rhdocs table td.halign-center, .rhdocs table th.halign-center, table
td.ha= lign-center, table th.halign-center { text-align: center; }
.rhdocs table td.halign-right, .rhdocs table th.halign-right {
text-align: = right; } .rhdocs table td.valign-top, .rhdocs table
th.valign-top { vertical-align: = top; } .rhdocs table td.valign-middle,
.rhdocs table th.valign-middle { vertical-a= lign: middle; } .rhdocs
table td.valign-bottom, .rhdocs table th.valign-bottom { vertical-a=
lign: bottom; } .rhdocs table thead td, .rhdocs table thead th {
background: rgb(245, 245, = 245); font-weight: 600; } .rhdocs rh-table
table, .rhdocs rh-table.rh-table\--expanded-vertically { ma= x-height:
max-content; } .rhdocs pre.nowrap { overflow: auto; overflow-wrap:
normal; white-space: pr= e; word-break: normal; } .rhdocs
.codeblock\_\_wrapper pre { background: transparent; }
.rh-table\--full-screen code, .rhdocs .content\--md code, .rhdocs
.content\--s= m code, .rhdocs .rh-table\--full-screen code {
overflow-wrap: normal; word-b= reak: normal; } .rhdocs\[class\] pre
code, \[class\] pre code { background: inherit; color: inh= erit;
font-family: inherit; font-size: inherit; font-weight: inherit; line-=
height: inherit; padding: 0px; } .rhdocs .keycap, .rhdocs kbd {
background-color: rgb(238, 238, 238); backgr= ound-image:
linear-gradient(rgb(221, 221, 221), rgb(238, 238, 238), rgb(255= , 255,
255)); border-radius: 0.1875rem; box-shadow: rgb(255, 255, 255) 0px =
-0.0625rem, rgb(170, 170, 170) 0px 0.0625rem 0px 0.1875rem; color:
rgb(21, = 21, 21); font-family: RedHatMono, \"Red Hat Mono\", Consolas,
monospace; font= -size: 90%; font-weight: 400; margin: 0px 0.25rem;
padding: 0.125rem 0.375r= em; } .keycap strong, .rhdocs .keycap strong {
font-weight: inherit; } .rhdocs kbd.keyseq, kbd.keyseq { background:
transparent; border: 0px; box-= shadow: none; padding: 0px; } .rhdocs
kbd.keyseq kbd, kbd.keyseq kbd { display: inline-block; margin: 0px=
0.375rem; } .rhdocs kbd.keyseq kbd:first-child, kbd.keyseq
kbd:first-child { margin-lef= t: 0px; } .rhdocs b.button { font-size:
90%; font-weight: 700; padding: 0.1875rem; } .rhdocs b.button::before {
content: \"\[\"; } .rhdocs b.button::after { content: \"\]\"; } html {
font-family: sans-serif; text-size-adjust: 100%; } body { margin: 0px; }
.rhdocs audio, .rhdocs canvas, .rhdocs progress, .rhdocs video {
display: i= nline-block; vertical-align: baseline; } .rhdocs
audio:not(\[controls\]) { display: none; height: 0px; } \[hidden\],
template { display: none; } .rhdocs a { background: transparent; }
.rhdocs a:active, .rhdocs a:hover { outline: 0px; } .rhdocs
a.anchor-heading:focus-visible { color: light-dark(var(\--rh-color-g=
ray-95,#151515),var(\--rh-color-white,#fff)); } .rhdocs abbr\[title\] {
border-bottom: 0.0625rem dotted; } .rhdocs dfn { font-style: italic; }
.rhdocs h1 { margin: 0.67em 0px; } .rhdocs mark { background: rgb(255,
255, 0); color: rgb(0, 0, 0); } .rhdocs small { font-size: 80%; }
.rhdocs sub, .rhdocs sup { font-size: 75%; line-height: 0; position:
relati= ve; vertical-align: baseline; } .rhdocs sup { top: -0.5em; }
.rhdocs sub { bottom: -0.25em; } .rhdocs img { background-color:
light-dark(transparent,var(\--rh-color-surfa= ce-lightest,#fff));
border: 0px; padding: 20px; } .rhdocs .inlinemediaobject img { padding:
2px; } .rhdocs svg:not(:root) { overflow: hidden; } .rhdocs figure {
margin: 1em 2.5rem; } .rhdocs hr { box-sizing: content-box; height: 0px;
} .rhdocs code, .rhdocs kbd, .rhdocs pre, .rhdocs samp { font-family:
monospa= ce, monospace; font-size: 1em; } .rhdocs button, .rhdocs
optgroup, .rhdocs select, .rhdocs textarea, .rhdocs= input { color:
inherit; font: inherit; margin: 0px; } .rhdocs rh-button.copy-link-btn {
border: 2px solid light-dark(var(\--rh-col=
or-white,#fff),var(\--rh-color-surface-darker,#1f1f1f)); cursor:
pointer; di= splay: flex; } .rhdocs rh-button.copy-link-btn:hover {
background-color: light-dark(var(\--=
rh-color-surface-lighter,#f2f2f2),var(\--rh-color-gray-60,#4d4d4d));
border-= radius: var(\--rh-border-radius-default,3px); } .rhdocs
rh-button.copy-link-btn .link-icon { color: light-dark(var(\--rh-col=
or-canvas-black,#151515),var(\--Core-color-palette-Gray-white,#fff)); }
.rhdocs button { overflow: visible; } .rhdocs button, .rhdocs select {
text-transform: none; } .rhdocs button, .rhdocs html
input\[type=3D\"button\"\], .rhdocs input\[type=3D\"= reset\"\], .rhdocs
input\[type=3D\"submit\"\] { appearance: button; cursor: point= er; }
.rhdocs button\[disabled\], .rhdocs html input\[disabled\] { cursor:
default; } .rhdocs input { line-height: normal; } .rhdocs
input\[type=3D\"checkbox\"\], .rhdocs input\[type=3D\"radio\"\] {
box-sizin= g: border-box; padding: 0px; } .rhdocs
input\[type=3D\"number\"\]::-webkit-inner-spin-button, .rhdocs
input\[ty= pe=3D\"number\"\]::-webkit-outer-spin-button { height: auto;
} .rhdocs input\[type=3D\"search\"\] { appearance: textfield;
box-sizing: content= -box; } .rhdocs
input\[type=3D\"search\"\]::-webkit-search-cancel-button, .rhdocs input=
\[type=3D\"search\"\]::-webkit-search-decoration { appearance: none; }
.rhdocs fieldset { border: 0.0625rem solid silver; margin: 0px 0.125rem;
pa= dding: 0.35em 0.625em 0.75em; } .rhdocs legend { border: 0px;
padding: 0px; } .rhdocs textarea { overflow: auto; } .rhdocs optgroup {
font-weight: 700; } .rhdocs table { border-collapse: collapse;
border-spacing: 0px; } .rhdocs td, .rhdocs th { padding: 0px; } .rhdocs
.\_additional-resources\[class\]\[class\], .rhdocs
.\_additional-resource= s\[class\]\[class\]\[id\]:last-child {
background: light-dark(var(\--rh-color-surf=
ace-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f)); border:
0.0625r= em solid rgb(210, 210, 210); border-radius: 0.1875rem; margin:
2em 0px 4em;= padding: 2rem 2rem 1rem; } .rhdocs
.\_additional-resources\[class\]\[class\]\[id\]:last-child { margin-top:
-= 2rem; } .rhdocs .\_additional-resources\[class\]\[class\]:only-child
{ grid-column: 1 / = -1; } .\_additional-resources\[class\]\[class\]
.additional-resources\_\_heading, .\_addi=
tional-resources\[class\]\[class\] .heading,
.\_additional-resources\[class\]\[clas= s\] h1,
.\_additional-resources\[class\]\[class\] h2,
.\_additional-resources\[clas= s\]\[class\] h3,
.\_additional-resources\[class\]\[class\] h4, .\_additional-resourc=
es\[class\]\[class\] h5, .\_additional-resources\[class\]\[class\] h6,
.\_additional-= resources\[class\]\[class\] p.title { display: block;
font-family: RedHatDispla= y, \"Red Hat Display\", \"Helvetica Neue\",
Arial, sans-serif; font-size: 1.125= rem; font-weight: 700; line-height:
1.5rem; margin: 0px 0px 0.5rem; padding= : 0px; text-transform:
uppercase; } .\_additional-resources\[class\]\[class\] ul { border: 0px;
list-style: none; ma= rgin: 0px; padding: 0px; position: relative; }
.related-topic-content\_\_wrapper
.\_additional-resources\[class\]\[class\] ul { d= isplay: block; }
.\_additional-resources\[class\]\[class\] ul::after { background-color:
light-da=
rk(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1=
f1f)); bottom: 0px; content: \"\"; display: block; height: 0.125rem;
position= : absolute; width: 100%; }
.\_additional-resources\[class\]\[class\] li { border-bottom: 0.0625rem
solid rg= b(210, 210, 210); box-sizing: content-box; margin: 0px;
padding: 1rem 1.5re= m 1rem 0px; break-inside: avoid; }
.\_additional-resources\[class\]\[class\] li:only-child { grid-column: 1
/ -1; } .\_additional-resources\[class\]\[class\] li:last-child {
border: 0px; } \@media (min-width: 1100px) {
.\_additional-resources\[class\]\[class\] li:last-child { border-bottom:
0.062= 5rem solid rgb(210, 210, 210); } }
.\_additional-resources\[class\]\[class\] li p:only-child { margin: 0px;
padding= : 0px; } .\_additional-resources\[class\]\[class\] li a {
text-decoration: none; } .\_additional-resources\[class\]\[class\] li
a:focus, .\_additional-resources\[cla= ss\]\[class\] li a:hover {
text-decoration: underline; } .rhdocs table .admonitionblock \>
div:nth-child(2), .rhdocs table .caution \>= div:nth-child(2), .rhdocs
table .important \> div:nth-child(2), .rhdocs tab= le .note \>
div:nth-child(2), .rhdocs table .tip \> div:nth-child(2), .rhdocs= table
.warning \> div:nth-child(2) { margin: 0.5rem 0px; } .rhdocs table
.admonitionblock \> div:nth-child(2) \> :first-child, .rhdocs t= able
.caution \> div:nth-child(2) \> :first-child, .rhdocs table .important
\>= div:nth-child(2) \> :first-child, .rhdocs table .note \>
div:nth-child(2) \> = :first-child, .rhdocs table .tip \>
div:nth-child(2) \> :first-child, .rhdocs= table .warning \>
div:nth-child(2) \> :first-child { margin-top: 0px; } .rhdocs table
.admonitionblock \> div:nth-child(2) \> :last-child, .rhdocs ta= ble
.caution \> div:nth-child(2) \> :last-child, .rhdocs table .important \>
d= iv:nth-child(2) \> :last-child, .rhdocs table .note \>
div:nth-child(2) \> :la= st-child, .rhdocs table .tip \>
div:nth-child(2) \> :last-child, .rhdocs tabl= e .warning \>
div:nth-child(2) \> :last-child { margin-bottom: 0px; } .rhdocs
.codeblock\_\_wrapper + .codeblock\_\_wrapper, .rhdocs pre + pre, .rhdo=
cs pre\[class\] + pre\[class\] { margin-top: 2rem; } .rhdocs
.codeblock\_\_wrapper { background: light-dark(var(\--rh-color-surface=
-lighter,#f2f2f2),var(\--rh-color-gray-80,#292929)); overflow: visible;
posi= tion: relative; transform: translate(0px); z-index: 0; }
.codeblock\_\_wrapper::before { background-repeat: no-repeat;
background-size= : 6.25rem 100%; bottom:
var(\--scrollbar\_\_height,1px); content: \"\"; display:= block; height:
7.125rem; max-height: calc(100% - var(\--scrollbar\_\_height, = 2px));
position: absolute; right: var(\--scrollbar\_\_width,6px); top: 0.0625r=
em; width: 4.0625rem; z-index: 1; } .rhdocs .codeblock\_\_inner-wrapper,
.rhdocs pre { max-height: calc(-6.25rem = + 100vh); } \@media
(min-height: 48em) { .rhdocs .codeblock\_\_inner-wrapper, .rhdocs pre {
max-height: calc(-12.5re= m + 100vh); } } .rhdocs
.codeblock\_\_inner-wrapper { display: grid; grid-template-columns: 1=
fr 4.375rem; } .rhdocs .codeblock\_\_wrapper\--expanded
.codeblock\_\_inner-wrapper { max-heigh= t: max-content; }
.codeblock\_\_copy span { display: block; height: 0px; position:
absolute; vi= sibility: hidden; width: 0px; } .codeblock\_\_copy:focus {
outline: currentcolor dashed 0.0625rem; } .codeblock\_\_copy
svg#icon\--copy { height: 1rem; width: 1rem; } .codeblock\_\_expand {
appearance: none; background: rgb(240, 239, 239); bord= er: 0px; cursor:
pointer; height: 1.75rem; left: calc(100% - 2.75rem - var(=
\--scrollbar\_\_width, 0px)); position: absolute; text-indent: -9999em;
top: 3= .25rem; width: 1.75rem; z-index: 2; }
.codeblock\_\_expand::before { background: rgb(106, 110, 115); content:
\"\"; h= eight: 100%; left: 0px; mask-image:
url(\"data:image/svg+xml;charset=3Dutf-8= ,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' viewBox=3D\'0 0 320 512\'%3E%3C!=
\--! Font Awesome Pro 6.2.0 by \@fontawesome - https://fontawesome.com
Licens= e - https://fontawesome.com/license (Commercial License)
Copyright 2022 Fon= ticons, Inc.\--%3E%3Cpath d=3D\'M182.6
9.4c-12.5-12.5-32.8-12.5-45.3 0l-96 96= c-12.5 12.5-12.5 32.8 0
45.3s32.8 12.5 45.3 0l41.4-41.4v293.4l-41.4-41.3c-1=
2.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l96 96c12.5 12.5 32.8 12.5
45.3 = 0l96-96c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192
402.7V109.3l41.4 4= 1.4c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8
0-45.3l-96-96z\'/%3E%3C/svg%3E\"); m= ask-position: center center;
mask-repeat: no-repeat; mask-size: auto 1rem; = position: absolute; top:
0px; width: 100%; } .codeblock\_\_wrapper\--expanded
.codeblock\_\_expand { background: rgb(43, 154,= 243); }
.codeblock\_\_wrapper\--expanded .codeblock\_\_expand::before {
background: rgb(= 255, 255, 255); } .codeblock\_\_expand:focus::before,
.codeblock\_\_expand:hover::before { backgr= ound: rgb(0, 102, 204); }
.codeblock\_\_wrapper\--expanded .codeblock\_\_expand:focus::before,
.codeblock\_= \_wrapper\--expanded .codeblock\_\_expand:hover::before {
background: rgb(255, = 255, 255); } .codeblock\_\_expand:focus {
outline: currentcolor dashed 0.0625rem; } .rhdocs .callout, .rhdocs
.colist \> ol \> li::before, .rhdocs .conum { backg= round:
light-dark(var(\--rh-color-status-info-on-light,#5e40be) var(\--rh-col=
or-status-info-on-dark,#b6a6e9)); height: 24px; width: 24px; } .rhdocs
.calloutlist \> ol, .rhdocs .colist \> ol { counter-reset: colist 0; =
list-style: none; margin: 1rem 0px 2rem; padding: 0px; } .rhdocs
.calloutlist \> ol \> li, .rhdocs .colist \> ol \> li { counter-increme=
nt: colist 1; font-size: 1rem; margin: 0.5rem 0px; padding-left:
1.75rem; p= osition: relative; } .rhdocs .calloutlist \> ol \> li
.colist-num, .rhdocs .colist \> ol \> li .coli= st-num { display: none;
} .calloutlist \> ol \> li::before, .colist \> ol \> li::before {
content: counte= r(colist); left: 0px; position: absolute; top:
0.1875rem; } .calloutlist dt { clear: left; float: left; margin: 0px;
padding: 0px 0.5re= m 0px 0px; } .included-in-guides\[class\],
.included-in-guides\[class\]\[id\]:last-child { bac= kground: rgb(255,
255, 255); border: 0.0625rem solid rgb(210, 210, 210); bo= rder-radius:
0.1875rem; margin: 2em 0px 4em; padding: 2rem 2rem 1rem; }
.included-in-guides\[class\]\[id\]:last-child { margin-top: -2rem; }
.included-in-guides\[class\]:only-child { grid-column: 1 / -1; }
.included-in-guides\[class\] .additional-resources\_\_heading,
.included-in-gui= des\[class\] .heading, .included-in-guides\[class\]
h1, .included-in-guides\[cla= ss\] h2, .included-in-guides\[class\] h3,
.included-in-guides\[class\] h4, .incl= uded-in-guides\[class\] h5,
.included-in-guides\[class\] h6, .included-in-guide= s\[class\] p.title
{ display: block; font-family: RedHatDisplay, \"Red Hat Dis= play\",
\"Helvetica Neue\", Arial, sans-serif; font-size: 1.125rem; font-weigh=
t: 700; line-height: 1.5rem; margin: 0px 0px 0.5rem; padding: 0px;
text-tra= nsform: uppercase; } .included-in-guides\[class\] ul { border:
0px; list-style: none; margin: 0px;= padding: 0px; position: relative; }
.related-topic-content\_\_wrapper .included-in-guides\[class\] ul {
display: bl= ock; } .included-in-guides\[class\] ul::after {
background-color: rgb(255, 255, 255)= ; bottom: 0px; content: \"\";
display: block; height: 0.125rem; position: abs= olute; width: 100%; }
.included-in-guides\[class\] li { border-bottom: 0.0625rem solid
rgb(210, 210= , 210); box-sizing: content-box; margin: 0px; padding:
1rem 1.5rem 1rem 0px= ; break-inside: avoid; }
.included-in-guides\[class\] li:only-child { grid-column: 1 / -1; }
.included-in-guides\[class\] li:last-child { border: 0px; } \@media
(min-width: 1100px) { .included-in-guides\[class\] li:last-child {
border-bottom: 0.0625rem solid= rgb(210, 210, 210); } }
.included-in-guides\[class\] li p:only-child { margin: 0px; padding:
0px; } .included-in-guides\[class\] li a { text-decoration: none; }
.included-in-guides\[class\] li a:focus, .included-in-guides\[class\] li
a:hove= r { text-decoration: underline; } .menuseq { display:
inline-flex; overflow: hidden; text-indent: -9999em; } .menuseq .menu,
.menuseq .menuitem, .menuseq .submenu { display: block; pos= ition:
relative; text-indent: 0px; } .menuseq .menu + .menu::before, .menuseq
.menu + .menuitem::before, .menuse= q .menu + .submenu::before, .menuseq
.menuitem + .menu::before, .menuseq .m= enuitem + .menuitem::before,
.menuseq .menuitem + .submenu::before, .menuse= q .submenu +
.menu::before, .menuseq .submenu + .menuitem::before, .menuseq=
.submenu + .submenu::before { content: \"\>\"; display: inline-block;
font-we= ight: 700; padding: 0px 0.25em; }
.related-topic-content\_\_wrapper { margin: 2em 0px; }
.related-topic-content\_\_wrapper\--for-guide { margin-bottom: -2.5rem;
paddin= g-bottom: 0.0625rem; position: relative; z-index: 1; }
.related-topic-content\_\_wrapper\--for-guide::before { background:
rgb(240, 2= 40, 240); content: \"\"; display: block; height: 100%; left:
-3rem; position:= absolute; right: -4.5rem; top: 0px; width: auto;
z-index: -1; } \@media (min-width: 1100px) {
.related-topic-content\_\_wrapper\--for-guide::before { left: -2.5rem;
right= : -3.625rem; } } .related-topic-content\_\_wrapper\--for-guide
summary { padding: 1em 2em 1em 2= .1875rem; } \@media (min-width: 950px)
{ .related-topic-content\_\_inner-wrapper { display: grid; gap: 2em;
grid-tem= plate-columns: repeat(2, minmax(0px, 1fr)); } } .local-render
.rhdocs-content { margin: 0px auto; } .rhdocs cp-documentation {
display: block; padding-bottom: 2.5rem; } .rhdocs
cp-documentation.PFElement, .rhdocs cp-documentation\[pfelement\] { p=
adding: 0px; } rh-table { display: block; } ::-webkit-scrollbar, :host
.rhdocs ::-webkit-scrollbar { height: 0.625rem; = width: 0.625rem; }
::-webkit-scrollbar, ::-webkit-scrollbar-track, :host .rhdocs
::-webkit-scr= ollbar, :host .rhdocs ::-webkit-scrollbar-track {
background-color: rgb(214= , 214, 214); } ::-webkit-scrollbar-thumb,
:host .rhdocs ::-webkit-scrollbar-thumb { backgr= ound-color: rgb(142,
142, 142); } \*, :host .rhdocs \* { scrollbar-color: rgb(142, 142, 142)
rgb(214, 214, 214)= ; } .rhdocs p:empty, p:empty { display: none; }
.rhdocs\[class\] h1 code, .rhdocs\[class\] h2 code, .rhdocs\[class\] h3
code, .rh= docs\[class\] h4 code, .rhdocs\[class\] h5 code,
.rhdocs\[class\] h6 code, \[class= \] h1 code, \[class\] h2 code,
\[class\] h3 code, \[class\] h4 code, \[class\] h5 co= de, \[class\] h6
code { background: transparent; border: 0px; color: inherit;= font:
inherit; margin: 0px; padding: 0px; } .pane-page-title h1,
.rhdocs\_\_header\_\_primary-wrapper h1 { font-family: Red= HatDisplay,
\"Red Hat Display\", \"Helvetica Neue\", Arial, sans-serif; font-si= ze:
2.25rem; line-height: 1.333; } .rhdocs details\[class\] { list-style:
none; margin: 1rem 0px 3rem; padding: = 0px; } .rhdocs-toc\[class\] {
background: rgb(242, 242, 242); margin: 1rem 0px 2rem;= padding: 1rem; }
.rhdocs-toc\[class\] \> :last-child { margin-bottom: 0px; }
.rhdocs-toc\[class\] .rhdocs-toctitle { font-size: 1.25rem; font-weight:
400;= line-height: 1.6667; margin-top: 0px; text-transform: none; }
.rhdocs-toc\[class\] li { margin-bottom: 0.25em; padding-left: 0.5em; }
.preamble { margin: 0px 0px 2rem; } .sect1 { margin: 2rem 0px 1rem; }
:host .sect1, cp-documentation .sect1 { margin: 0px 0px 2rem; padding:
0.06= 25rem 0px 0px; } :host(.cp-documentation\--has-external-header)
.sect1:first-child \> h2:first= -child,
:host(.cp-documentation\--has-external-header) .sect1:first-child \> =
h3:first-child { margin-top: 0px; } .listingblock, .literalblock {
margin: 1rem 0px; } .quoteblock, .verseblock { border-left: 0.25rem
solid rgb(210, 210, 210); m= argin: 1rem 0px; padding: 1rem 1rem 1rem
2rem; } .quoteblock.pullleft, .verseblock.pullleft { float: left;
margin-right: 3re= m; width: 25rem; } \@media (min-width: 768px) {
.quoteblock.pullleft, .verseblock.pullleft { margin-left: -1rem; } }
.quoteblock.pullright, .verseblock.pullright { float: right;
margin-left: 3= rem; width: 25rem; } \@media (min-width:768) {
.quoteblock.pullright, .verseblock.pullright { margin-right: -2rem; } }
\@media (min-width: 1100px) { .quoteblock.pullright,
.verseblock.pullright { margin-right: -10rem; } } .quoteblock \>
:first-child, .verseblock \> :first-child { margin-top: 0px; }
.quoteblock .content, .verseblock .content { font-family: RedHatText,
\"Red = Hat Text\", \"Helvetica Neue\", Arial, sans-serif; font-size:
1.25rem; line-he= ight: 1.6667; } .quoteblock .attribution, .verseblock
.attribution { font-size: 0.875rem; f= ont-style: italic; font-weight:
600; line-height: 1.6667; text-transform: u= ppercase; } .quoteblock
.attribution .citetitle, .verseblock .attribution .citetitle { = color:
rgb(88, 88, 88); } .quoteblock .attribution cite, .verseblock
.attribution cite { font-size: 1= em; } .quoteblock blockquote {
font-style: italic; margin: 0px; padding: 0px; } .quoteblock blockquote
.content \> :first-child { margin-top: 0px; } .quoteblock blockquote
.content \> :first-child::before { color: light-dark(=
#e00,var(\--rh-color-text-secondary-on-dark,#c7c7c7)); content:
\"=C3=A2=E2= =82=AC=C5=93\"; display: block; float: left; font-size:
2.75rem; font-style:= normal; line-height: 1.125em; margin-right:
0.5rem; } .quoteblock blockquote .content \> :first-child .content \>
:first-child::bef= ore { content: none; } .imageblock { margin: 1rem
0px; } .imageblock.pullleft { float: left; margin-right: 3rem; width:
25rem; } \@media (min-width: 768px) { .imageblock.pullleft {
margin-left: -1rem; } } .imageblock.pullright { float: right;
margin-left: 3rem; width: 25rem; } \@media (min-width:768) {
.imageblock.pullright { margin-right: -2rem; } } \@media (min-width:
1100px) { .imageblock.pullright { margin-right: -10rem; } }
.imageblock.interrupter { margin: 2rem 0px; } \@media (min-width: 768px)
{ .imageblock.interrupter { margin-left: -1rem; margin-right: -2rem; }
.imageblock.interrupter .caption { margin-left: 1rem; margin-right:
2rem;= } } \@media (min-width: 1100px) { .imageblock.interrupter {
margin-right: -10rem; } .imageblock.interrupter .caption { margin-right:
10rem; } } .imageblock.interrupter img { max-width: 100%; } .imageblock
.caption { color: rgb(88, 88, 88); display: block; font-size: 0=
.875rem; line-height: 1.6667; margin: 0.5rem 0px 0px; }
.rhdocs-footnotes { border-top: 0.0625rem solid rgb(210, 210, 210);
margin:= 3rem 0px 1rem; padding: 1rem 0px 0px; } .rhdocs-footnotes \> ol
{ margin: 0px; padding: 0px 0px 0px 1.5rem; } \@supports
(counter-reset:footnotenum) { .rhdocs-footnotes \> ol { counter-reset:
footnotenum 0; list-style: none; = padding: 0px; } .rhdocs-footnotes \>
ol \> li { counter-increment: footnotenum 1; } .rhdocs-footnotes \> ol
\> li::before { color: rgb(88, 88, 88); content: \"\[= \"
counter(footnotenum) \"\]\"; display: inline-block; margin-right:
0.25rem; } } .rhdocs-footer { background: rgb(237, 237, 237); color:
rgb(21, 21, 21); fo= nt-size: 0.875rem; line-height: 1.6667; margin:
3rem 0px 0px; padding: 1rem= ; } .center { margin-left: auto;
margin-right: auto; } .stretch { width: 100%; } .visually-hidden {
overflow: hidden; position: absolute; clip: rect(0px, 0p= x, 0px, 0px);
border: 0px; height: 0.0625rem; margin: -0.0625rem; padding: = 0px;
width: 0.0625rem; } .rh-docs-legal-notice { margin-top: 4em; } pre,
pre\[class\] { margin: 0px; padding: 1.25em 1em; position: relative; }
code\[class\*=3D\"language-\"\], pre\[class\*=3D\"language-\"\] { color:
rgb(21, 21, = 21); tab-size: 4; } code.language-none,
code.language-text, code.language-txt, pre.language-non= e,
pre.language-text, pre.language-txt { color: rgb(21, 21, 21); }
code\[class\*=3D\"language-\"\] ::selection,
code\[class\*=3D\"language-\"\]::selecti= on,
pre\[class\*=3D\"language-\"\] ::selection,
pre\[class\*=3D\"language-\"\]::selec= tion {
\--\_selected-text-background: light-dark(#b4d7ff,#395676); } :not(pre)
\> code\[class\*=3D\"language-\"\] { border-radius: 0.2em; padding: 0.1=
em; white-space: normal; } .rhdocs.local-render { margin: 0px auto;
max-width: 45.8125rem; padding: 0p= x 1.5rem; } \@media print { .field
code, .field pre, code\[class\*=3D\"language-\"\], pre,
pre\[class\*=3D\"l= anguage-\"\] { white-space: pre-wrap !important;
overflow-wrap: break-word !i= mportant; word-break: break-word
!important; } } .book-nav\_\_list\[class\] { display: flex;
justify-content: space-between; lin= e-height:
var(\--jupiter\_\_lineHeight\--xs,1.3333); list-style: none; margin: =
5rem 0px 0px; padding: 0px; } \@media (min-width: 1200px) {
.book-nav\_\_list\[class\] { display: grid; gap: 2rem;
grid-template-columns:= repeat(2, minmax(0px, 1fr)); } }
.book-nav\_\_item a { display: inline-block; font-size: 0.875rem;
font-weight= : 500; padding-left: 1.25rem; position: relative;
text-transform: uppercase= ; } .book-nav\_\_item a::before { background:
url(\"/sites/dxp-docs/penumbra-dist/=
jupiter/images/arrow-down-solid.svg\") 0% 0% / contain no-repeat;
content: \"= \"; display: block; height: 0.875rem; left: 0px; position:
absolute; top: 0.= 125rem; transform: rotate(90deg); width: 0.875rem; }
.book \> .titlepage:not(:last-child), .rhdocs .chapter, section\[id\] {
paddin= g-bottom: 3.75rem; } .book \> .titlepage .chapter:last-child,
.book \> .titlepage section\[id\]:last= -child, .chapter
.chapter:last-child, .chapter section\[id\]:last-child, sect= ion\[id\]
.chapter:last-child, section\[id\] section\[id\]:last-child { margin-bo=
ttom: -3.75rem; } .rhdocs .codeblock\_\_wrapper + section\[id\], pre +
section\[id\] { padding-top:= 3.75rem; } .rhdocs .cta-link { font-size:
inherit; } .rhdocs a { overflow-wrap: break-word; } .rhdocs .caution,
.rhdocs .important, .rhdocs .note, .rhdocs .tip, .rhdocs = .warning {
padding: 0.888889em; position: relative; } .rhdocs .QSIPopOver { bottom:
18.75rem !important; top: auto !important; } .rhdocs .alert { position:
relative; } .rhdocs button.dismiss-button { background: none; border:
0px; cursor: poin= ter; height: 2.5rem; margin-top: -1.25rem; padding:
0px; position: absolute= ; right: 0.3125rem; text-align: center; top:
50%; width: 2.5rem; z-index: 5= 0; } .rhdocs
button.dismiss-button::after { content: \"=EF=84=89\"; display: inlin=
e-block; font-family: rh-web-iconfont; font-size: 1.3125rem; font-style:
no= rmal; font-variant: normal; font-weight: 400; line-height: 2.5rem;
opacity:= 0.3; text-decoration: inherit; text-rendering:
optimizelegibility; -webkit= -font-smoothing: antialiased;
text-transform: none !important; } .rhdocs .book \> .titlepage, .rhdocs
.chapter, .rhdocs section\[id\] { padding= -bottom:
var(\--rh-space-4xl,64px); } .rhdocs .alert { border: 0px;
border-radius: 0px; } .rhdocs .alert \> h2:first-child, .rhdocs .alert
\> h3:first-child, .rhdocs .= alert \> h4:first-child, .rhdocs .alert \>
h5:first-child, .rhdocs .alert \> h= 6:first-child, .rhdocs .alert \>
p:first-child { margin-top: 0px !important;= } .rhdocs .alert \>
p:last-child { margin-bottom: 0px !important; } .rhdocs
.alert-w-icon\[class\] { padding-left: 2.8125rem; } .rhdocs
.alert-w-icon .alert-icon { float: left; font-size: 1.125rem; margi=
n-left: -1.875rem; margin-right: 0.625rem; } .rhdocs .alert-w-icon
.alert-icon\[class\*=3D\" rh-icon-\"\], .rhdocs .alert-w-i= con
.alert-icon\[class\^=3D\"rh-icon-\"\] { font-size: 2.25rem; line-height:
1em= ; margin-left: -2.5rem; margin-top: -0.375rem; } .rhdocs
.alert-w-icon .alert-icon\[class\*=3D\" icon-innov-prev\"\], .rhdocs
.al= ert-w-icon .alert-icon\[class\^=3D\"icon-innov-prev\"\] {
font-size: 1.3125rem; = margin-top: 0.25rem; } .rhdocs
.alert-w-icon.alert-plain { background: none; color: rgb(21, 21, 21= );
padding-left: 5rem; } .rhdocs .alert-w-icon.alert-plain .alert-icon {
font-size: 3rem; margin-lef= t: -4.375rem; margin-right: 0px; } .rhdocs
.alert-w-icon.alert-plain.alert-success .alert-icon { color: rgb(63= ,
156, 53); } .rhdocs .alert-w-icon.alert-plain.alert-info .alert-icon {
color: rgb(0, 13= 6, 206); } .rhdocs
.alert-w-icon.alert-plain.alert-warning .alert-icon { color: rgb(24= 0,
171, 0); } .rhdocs .alert-w-icon.alert-plain.alert-danger .alert-icon {
color: rgb(238= , 0, 0); } #target_banner .copy-url { float: right;
margin-top: 0px; } #target_banner .dropdown-menu { font-size: inherit; }
.titlepage .svg-img\[data\*=3D\"title_logo.svg\"\] { margin: 1.5rem 0px;
width: = 15rem; } .para { margin: 1.49963rem 0px; } .para\[class\] {
margin-bottom: 1.49963rem; } dd { margin-bottom: 2.5rem; } .rhdocs
.card-light, .rhdocs .card-light-gray, .rhdocs .card-light-grey { b=
ackground: rgb(240, 240, 240); border: 0.0625rem solid rgb(240, 240,
240); = color: rgb(21, 21, 21); } .rhdocs
.card-light-gray.push-bottom:first-child, .rhdocs .card-light-grey.=
push-bottom:first-child, .rhdocs .card-light.push-bottom:first-child {
marg= in-bottom: 3.125rem !important; } .rhdocs .card-light a.card-link,
.rhdocs .card-light h1, .rhdocs .card-ligh= t h2, .rhdocs .card-light
h3, .rhdocs .card-light h4, .rhdocs .card-light h= 5, .rhdocs
.card-light h6, .rhdocs .card-light-gray a.card-link, .rhdocs .c=
ard-light-gray h1, .rhdocs .card-light-gray h2, .rhdocs .card-light-gray
h3= , .rhdocs .card-light-gray h4, .rhdocs .card-light-gray h5, .rhdocs
.card-l= ight-gray h6, .rhdocs .card-light-grey a.card-link, .rhdocs
.card-light-gre= y h1, .rhdocs .card-light-grey h2, .rhdocs
.card-light-grey h3, .rhdocs .ca= rd-light-grey h4, .rhdocs
.card-light-grey h5, .rhdocs .card-light-grey h6 = { color: rgb(21, 21,
21); } .rhdocs .card-light-gray.card-active::after, .rhdocs
.card-light-grey.card-= active::after, .rhdocs
.card-light.card-active::after { border-top-color: r= gb(240, 240, 240);
} .rhdocs .card-md, .rhdocs .card-narrow { display: block; padding:
1.1875rem= ; white-space: normal; overflow-wrap: break-word; } .rhdocs
.card .card-heading.card-heading-sm, .rhdocs .card-sm .card .card-h=
eading { font-size: 1.0625em; font-weight: 500; line-height: 1.5; }
.rhdocs .card .card-heading.card-heading-flush { margin-bottom: 0.25rem;
} .rhdocs .card .card-heading.card-heading-red { color: rgb(209, 0, 0);
} .rhdocs .card \> p { margin-top: 0px; } .rhdocs .card \> p:last-child
{ margin-bottom: 0px; } .rhdocs .new-experience { background-color:
rgb(231, 241, 250); border: 0.0= 625rem solid rgb(190, 225, 244);
font-size: 1rem; margin: 1.5rem; padding: = 1.5rem; position: relative;
z-index: 1; } \@media (min-width: 48rem) { .new-experience { display:
flex; } .new-experience\--contained { left: 50%; position: relative;
transform: tr= anslate(-50%); width: calc(-2.5rem + 100vw); } }
.new-experience\_\_primary-content { flex-grow: 1; } \@media (min-width:
48rem) { .new-experience\_\_primary-content { margin-right: 1.25rem; } }
.new-experience\_\_title { font-size: inherit; font-weight: inherit;
line-hei= ght: 1.6; margin: 0px; padding: 0px; }
.new-experience\_\_title + a, .new-experience\_\_title + pfe-cta {
display: inl= ine-block; margin-top: 1.5em; }
.new-experience\_\_secondary-content { min-width: 12.5rem; } \@media
(min-width: 48rem) { .new-experience\_\_secondary-content { text-align:
right; } } .example { border-left: 0.3125rem solid rgb(204, 204, 204);
margin-bottom: = 2rem; padding: 1rem 0px 1rem 1rem; }
dl.calloutlist\[class\] { display: grid; gap: 1.25em 0.75em;
grid-template-co= lumns: min-content 1fr; } dl.calloutlist\[class\] dt {
float: none; margin: 0px; padding: 0px; } dl.calloutlist\[class\] dd {
margin: 0px; padding: 0px; } dl.calloutlist\[class\] dd \> :first-child
{ margin-top: 0px; } dl.calloutlist\[class\] dd \> :last-child {
margin-bottom: 0px; } .toast { background-color: rgba(0, 0, 0, 0.9);
bottom: 0.9375rem; box-shado= w: rgba(0, 0, 0, 0.26) 0px 0.125rem
0.3125rem; color: rgb(255, 255, 255); l= eft: 0.9375rem; max-width:
32.8125rem; min-width: 6.25rem; padding: 0.9375r= em; position: fixed;
right: 0.9375rem; transform: translate3d(0px, 150%, 0p= x); transition:
transform 0.2s cubic-bezier(0.465, 0.183, 0.153, 0.946); wi= ll-change:
transform; z-index: 999; } .toast.show { transform: translateZ(0px); }
.toast a { color: rgb(255, 255, 255); text-decoration: underline; }
.toast a:focus, .toast a:hover { color: rgb(43, 154, 243); } .toast
a.btn { text-decoration: none; } .toast .btn.btn-link { color: rgb(255,
255, 255); } .toast .close { color: rgb(255, 255, 255); opacity: 0.3;
text-decoration: n= one; } .toast .close:focus, .toast .close:hover {
color: rgb(255, 255, 255); opaci= ty: 0.5; }
.no-csstransforms3d.csstransitions .toast { transition: 0.2s
cubic-bezier(0= .465, 0.183, 0.153, 0.946); } .no-csstransforms3d .toast
{ opacity: 0; visibility: hidden; } .no-csstransforms3d .toast.show {
opacity: 1; visibility: visible; } .annotator-outer\[class\]\[class\] {
display: none; flex-direction: column; fle= x-grow: 1; height: auto;
margin: 0px; position: static; width: auto; } \@media (min-width:
1400px) { .annotator-outer\[class\]\[class\] { display: flex; } }
.annotator-frame\[class\] \* { height: auto; } \@media (min-width:
1400px) { .annotator-frame .h-sidebar-iframe\[class\] { position:
static; width: calc= (100% + 1.5rem); } }
.annotator-toolbar\[class\]\[class\] { position: static; width: auto; }
.annotator-toolbar \> ul, .annotator-toolbar \> ul \> li { display:
block; hei= ght: auto; list-style: none; margin: 0px; padding: 0px;
width: auto; } .annotator-toolbar \> ul \> li { display: flex;
justify-content: flex-end; } .annotator-frame\[class\]
.annotator-frame-button\--sidebar_toggle, .annotator= -outer
.annotator-frame-button\[class\]\[class\], .app-content-wrapper \* {
font= -family: RedHatText, \"Red Hat Text\", \"Helvetica Neue\", Arial,
sans-serif !i= mportant; } .annotator-outer
.annotator-frame-button\[class\]\[class\] { font-size: 0.9375r= em;
font-weight: 500; height: auto; line-height: 1.333; margin-right: 1.875=
rem; padding: 0.75em 1em; position: static; } \@media (min-width:
1400px) { .annotator-outer .annotator-frame-button\[class\]\[class\] {
margin-right: 0p= x; } } .annotator-outer iframe { flex-grow: 1;
margin-bottom: 1.25rem; } \@media (min-width: 1400px) { .annotator-outer
iframe { min-height: 37.5rem; } } .producttitle { color:
light-dark(var(\--rh-color-black,#000),var(\--rh-color= -white,#fff));
font-size: 1.25rem; text-transform: uppercase; } .producttitle
.productnumber { color: light-dark(var(\--jupiter\_\_palette\_\_re=
d\--50,#e00),var(\--rh-color-text-secondary-on-dark,#c7c7c7)); }
.cp-modal-open, .zoom-open { overflow: hidden; } .cp-modal,
.cp-video-modal, .zoom-modal { inset: 0px; display: none; opacit= y: 0;
outline: 0px; overflow: hidden; position: fixed; transition: 0.2s cub=
ic-bezier(0.465, 0.183, 0.153, 0.946); z-index: 1050; } .rhdocs
.in.cp-modal, .rhdocs .in.cp-video-modal, .rhdocs .in.zoom-modal { =
display: block; opacity: 1; overflow: hidden auto; } .rhdocs .cp-modal
.close, .rhdocs .cp-video-modal .close, .rhdocs .zoom-mod= al .close {
background-color: rgb(255, 255, 255); border-radius: 50%; color= :
rgb(26, 26, 26); font-size: 1.75rem; height: 1.75rem; line-height:
1.75re= m; margin-bottom: 0.375rem; margin-top: 0px; opacity: 0.9;
position: absolu= te; right: -0.5rem; text-shadow: none; top: 0px;
width: 1.75rem; } .cp-modal .close::after, .cp-video-modal
.close::after, .zoom-modal .close:= :after { line-height: 1.75rem; }
.cp-modal-wrap, .zoom-wrap { margin: 0.625rem; padding-top: 0.5rem;
positio= n: relative; } \@media (min-width: 48rem) { .rhdocs
.cp-modal-wrap, .rhdocs .zoom-wrap { margin: 2.8125rem auto; widt= h:
38.4375rem; } } \@media (min-width: 62rem) { .rhdocs .cp-modal-wrap,
.rhdocs .zoom-wrap { width: 49.8958rem; } } \@media (min-width: 75rem) {
.rhdocs .cp-modal-wrap, .rhdocs .zoom-wrap { width: 60.3125rem; } }
.rhdocs .cp-modal-body :last-child { margin-bottom: 0px; } .rhdocs
.cp-modal-backdrop, .rhdocs .zoom-backdrop { background-color: rgb(= 0,
0, 0); inset: 0px; display: none; opacity: 0; position: fixed;
transitio= n: opacity 0.2s cubic-bezier(0.465, 0.183, 0.153, 0.946);
z-index: 1040; } .rhdocs .in.cp-modal-backdrop, .rhdocs
.in.zoom-backdrop { display: block; = opacity: 0.8; } .rhdocs
.cp-modal-body { background: rgb(255, 255, 255); padding: 1.875rem;= }
.rhdocs .cp-modal\[data-cp-modal-video=3D\"true\"\] .cp-modal-body,
.rhdocs .cp= -video-modal .cp-modal-body { padding: 0px; } .rhdocs
\[data-action=3D\"zoom\"\] { position: relative; } .rhdocs
\[data-action=3D\"zoom\"\]::after { background: rgba(0, 0, 0, 0.4); bot=
tom: 0px; color: rgb(255, 255, 255); display: inline-block; font-family:
rh= -web-iconfont; font-style: normal; font-variant: normal;
font-weight: 400; = line-height: 1; padding: 0.375rem; position:
absolute; right: 0px; text-ren= dering: optimizelegibility;
-webkit-font-smoothing: antialiased; text-decor= ation: none !important;
text-transform: none !important; } .rhdocs
\[data-action=3D\"zoom\"\]:focus::after, .rhdocs
\[data-action=3D\"zoom\"\]= :hover::after { background: rgba(0, 0, 0,
0.9); } .rhdocs .zoom-wrap .zoom-larger { text-align: center; } .rhdocs
.zoom-wrap .zoom-larger a { color: rgb(255, 255, 255); } .rhdocs
.zoom-wrap .zoom-larger a:focus, .rhdocs .zoom-wrap .zoom-larger a:=
hover { color: rgb(255, 255, 255); text-decoration: underline; } .rhdocs
.zoom-wrap .zoom-larger a::after { content: \"=C3=A2=C2=BF=C2=BB\"; d=
isplay: inline-block; margin-left: 0.25rem; } .rhdocs .zoom-body {
background: rgb(255, 255, 255); border-radius: 0.5rem;= margin: 0px 0px
1rem; padding: 1rem; text-align: center; } .rhdocs .zoom-body
.video-wrapper { height: 0px; overflow: hidden; padding-= bottom:
56.25%; position: relative; } .rhdocs .zoom-body
.video-wrapper\[data-aspect-ratio=3D\"4:3\"\] { padding-bott= om: 75%; }
.rhdocs .zoom-body iframe { height: 100%; left: 0px; position: absolute;
to= p: 0px; width: 100%; } .rhdocs .para \> .title\[class\], .rhdocs
p.title\[class\] { font-size: 1rem; fo= nt-style: normal; font-weight:
700; line-height: 1.6667; margin: 1.25rem 0p= x 0px; text-transform:
none; } .rhdocs .para \> .title\[class\] + .content \> :first-child,
.rhdocs .para \> .t= itle\[class\] + p, .rhdocs p.title\[class\] +
.content \> :first-child, .rhdocs = p.title\[class\] + p { margin-top:
0px; } .rhdocs \[class\] pre .caution, .rhdocs \[class\] pre .important,
.rhdocs \[clas= s\] pre .note, .rhdocs \[class\] pre .tip, .rhdocs
\[class\] pre .warning { back= ground: transparent; border: 0px; color:
inherit; font: inherit; margin: 0p= x; padding: 0px; } .rhdocs \[class\]
pre .caution::after, .rhdocs \[class\] pre .important::after,= .rhdocs
\[class\] pre .note::after, .rhdocs \[class\] pre .tip::after, .rhdocs=
\[class\] pre .warning::after { content: none; } .rhdocs \[class\]
code.email { background-color: transparent; font: inherit; = padding:
0px; } .rhdocs \[class\] .author { margin-bottom: 1.5rem; } .rhdocs
\[class\] .author .author { margin-bottom: 0px; } .rhdocs table {
margin: 2rem 0px; } .rhdocs \[class\] table { width: auto; } .rhdocs
table .table-contents table { max-width: 100%; overflow: auto; } .rhdocs
rh-table table { margin: 0px; max-width: 9999em; overflow: visible;= }
.rhdocs td, .rhdocs th { border-left: 0px; padding: 0.5em 1rem;
transition:= background 0.25s ease-out; } .rhdocs
td.content\--md\[class\]\[class\], .rhdocs
th.content\--md\[class\]\[class\] = { min-width: 13em; } .rhdocs
td.content\--lg\[class\]\[class\], .rhdocs
th.content\--lg\[class\]\[class\] = { min-width: 20em; } .rhdocs thead
th { padding-top: 1.5em; } .rhdocs caption { color:
var(\--pfe-table\_\_caption\--Color,currentColor); fon= t-weight: 700;
margin-bottom: 0.5rem; margin-top: 0.5rem; text-align: cente= r; }
.rhdocs .revhistory table td, .rhdocs .revhistory table th {
border-color: = transparent; } .rhdocs .revhistory table td { padding:
0.625rem 0.875rem; } .rhdocs .revhistory table.simplelist { margin: 0px;
} \@media print { #masthead { display: none !important; } }
.rh-table\--is-full-screen #to-top { display: none; } .rhdocs {
\--rh-table\--maxHeight: calc(100vh - 6.25rem); color: rgb(21, 21, =
21); font-family: var(\--rh-font-family-body-text,RedHatText,\"Red Hat
Text\",= \"Noto Sans Arabic\",\"Noto Sans Hebrew\",\"Noto Sans
JP\",\"Noto Sans KR\",\"Noto S= ans Malayalam\",\"Noto Sans SC\",\"Noto
Sans TC\",\"Noto Sans Thai\",Helvetica,Ari= al,sans-serif); font-size:
var(\--rh-body-copy-lage,1.125rem); line-height: = 1.6667; tab-size: 4;
} .rhdocs rh-codeblock::slotted(#content) { border-radius: 0.25rem; }
.rhdocs rh-codeblock .screen { display: grid; grid-template-columns: 1fr
4.= 375rem; } .rhdocs
rh-codeblock\[class\]\[class\]\[class\]\[class\]\[class\] { max-width:
99999e= m; } .rhdocs .codeblock\_\_copy span { display: block; height:
0px; position: abso= lute; visibility: hidden; width: 0px; } .rhdocs
.codeblock\_\_copy:focus { outline: currentcolor dashed 0.0625rem; }
.rhdocs .codeblock\_\_copy svg#icon\--copy { height: 1rem; width: 1rem;
} .rhdocs pre { border: 0px; max-height: max-content; } .rhdocs pre,
pre\[class\] { margin: 0px; padding: 1.25em 1em; position: relat= ive; }
.rhdocs rh-code-block \> div.codeblock\_\_inner-wrapper \> pre, .rhdocs
rh-code= -block \> div.codeblock\_\_inner-wrapper \> pre\[class\] {
margin: 0px; padding: = 0px; position: relative; } .rhdocs rh-code-block
{ background: light-dark(var(\--rh-color-surface-light=
er,#f2f2f2),oklch(from var(\--rh-color-surface-dark,#383838)
calc(l\*.82) c h= )); } .rhdocs rh-code-block \> pre::after, .rhdocs
rh-code-block \> pre::before, .r= hdocs rh-code-block \> script::after,
.rhdocs rh-code-block \> script::before= { content: \"\"; display:
block; height: 10px; } .rhdocs rh-code-block pre:has(+ rh-badge)::after,
.rhdocs rh-code-block scr= ipt:has(+ rh-badge)::after { display: none; }
.rhdocs rh-code-block rh-badge + pre::before, .rhdocs rh-code-block
rh-badg= e + script::before { display: none; } .rhdocs
code\[class\*=3D\"language-\"\], pre\[class\*=3D\"language-\"\] { color:
rgb(= 21, 21, 21); tab-size: 4; } .rhdocs code.literal { background:
light-dark(#eee,var(\--rh-color-surface-d= ark,#383838)); border-radius:
0.25rem; color: light-dark(var(\--rh-color-bla=
ck,#000),var(\--rh-color-white,#fff)); font-size: 0.875rem; line-height:
1.6= 667; overflow-wrap: break-word; padding: 0.125em 0.5em; word-break:
break-w= ord; } .rhdocs code.literal, .rhdocs kbd, .rhdocs span.keycap {
font-family: RedHa= tMono, \"Red Hat Mono\", Consolas, monospace; }
.rhdocs kbd, .rhdocs span.keycap { background-color: rgb(238, 238, 238);
ba= ckground-image: linear-gradient(rgb(221, 221, 221), rgb(238, 238,
238), rgb= (255, 255, 255)); border-radius: 0.1875rem; box-shadow:
rgb(255, 255, 255) = 0px -0.0625rem, rgb(170, 170, 170) 0px 0.0625rem
0px 0.1875rem; font-size: = 90%; font-weight: 400; margin: 0px 0.25rem;
padding: 0.125rem 0.375rem; } .rhdocs ol, .rhdocs ul { margin: 1rem 0px;
padding: 0px 0px 0px 1.5rem; } .rhdocs
.\_additional-resources\[class\]\[class\] ul { border: 0px; list-style:
= none; margin: 0px; padding: 0px; position: relative; } .rhdocs
.\_additional-resources\[class\]\[class\] li { border-bottom: 0.0625rem
= solid rgb(210, 210, 210); box-sizing: content-box; margin: 0px;
padding: 1r= em 1.5rem 1rem 0px; break-inside: avoid; } .rhdocs
.\_additional-resources\[class\]\[class\] li:last-child { border: 0px; }
.rhdocs section.section#additional_resource
.additional-resources\_\_heading,= .rhdocs
section.section#additional_resource .heading, .rhdocs section.sect=
ion#additional_resource h1, .rhdocs section.section#additional_resource
h2,= .rhdocs section.section#additional_resource h3, .rhdocs
section.section#ad= ditional_resource h4, .rhdocs
section.section#additional_resource h5, .rhdo= cs
section.section#additional_resource h6, .rhdocs
section.section#addition= al_resource p.title { display: block;
font-family: RedHatDisplay, \"Red Hat = Display\", \"Helvetica Neue\",
Arial, sans-serif; font-size: 1.125rem; font-we= ight: 700; line-height:
1.5rem; margin: 0px 0px 0.5rem; padding: 0px; text-= transform:
uppercase; } .rhdocs section.section:first-of-type { margin-top:
var(\--rh-space-4xl,64px= ); } .rhdocs section.section p {
margin-bottom: var(\--rh-space-lg,16px); margin-= top: 0px;
overflow-wrap: break-word; } .rhdocs h1:first-of-type, .rhdocs
h2:first-of-type, .rhdocs h3:first-of-typ= e, .rhdocs h4:first-of-type,
.rhdocs h5:first-of-type, .rhdocs h6:first-of-= type { margin-top: 0px;
} .rhdocs dl { display: block; margin-block: 1em; margin-inline: 0px; }
.rhdocs .para { margin: 1.49963rem 0px; } .rhdocs
dl.calloutlist\[class\] dt { float: none; margin: 0px; padding: 0px; = }
.rhdocs dl.calloutlist\[class\] dd \> :last-child { margin-bottom: 0px;
} .rhdocs dl.calloutlist\[class\] { display: grid; gap: 1.25em 0.75em;
grid-tem= plate-columns: fit-content(40%) 1fr; } .rhdocs .calloutlist dt
{ clear: left; display: flex; flex-wrap: wrap; floa= t: left; margin:
0px; padding: 0px 0.5rem 0px 0px; } .rhdocs .calloutlist dt
a:not(:first-child) { padding-left: 4px; } .rhdocs
dl.calloutlist\[class\] dd { margin: 0px; padding: 0px; } .rhdocs
.callout, .rhdocs .colist \> ol \> li::before, .rhdocs .conum { backg=
round:
light-dark(var(\--rh-color-status-info-on-light,#5e40be),var(\--rh-col=
or-status-info-on-dark,#b6a6e9)); border-radius: 50%; color:
light-dark(var=
(\--rh-color-text-primary-on-dark,#fff),var(\--rh-color-text-primary-on-light=
,#151515)); display: inline-block; font-family:
var(\--rh-font-family-code,R= edHatMono,\"Red Hat Mono\",\"Courier
New\",Courier,monospace); font-size: 0.75r= em; font-style: normal;
font-weight: 600; line-height: 1.5rem; min-height: = 24px; min-width:
24px; padding: 0px; position: relative; text-align: center= ; top:
-0.125em; vertical-align: middle; } .rhdocs img, .rhdocs object, .rhdocs
svg { display: inline-block; max-width= : 100%; vertical-align: middle;
} .rhdocs .titlepage .svg-img\[data\*=3D\"title_logo.svg\"\] { margin:
1.5rem 0px;= width: 15rem; } .rhdocs\[class\] .author { margin-bottom:
1.5rem; } .rhdocs\[class\] .author .author { margin-bottom: 0px; }
.rhdocs .para \> .title\[class\], p.title\[class\] { font-size: 1rem;
font-style= : normal; font-weight: 700; line-height: 1.6667; margin:
1.25rem 0px 0px; } .rhdocs .example { border-left: 0.3125rem solid
rgb(204, 204, 204); margin-= bottom: 2rem; padding: 1rem 0px 1rem 1rem;
} .rhdocs code { background:
light-dark(#eee,var(\--rh-color-surface-dark,#383= 838)); font-family:
RedHatMono, \"Red Hat Mono\", Consolas, monospace; font-s= ize:
0.875rem; line-height: 1.6667; overflow-wrap: break-word; padding: 0.1=
25em 0.5em; word-break: break-word; } .rhdocs .para\[class\] {
margin-bottom: 1.49963rem; } .rhdocs\[class\] code.email {
background-color: transparent; font: inherit; p= adding: 0px; }
rh-alert.admonition #description, rh-alert.admonition p { font-size:
var(\--= rh-font-size-body-text-md,1rem); } rh-alert { width:
fit-content; } .rhdocs .producttitle { color:
light-dark(var(\--rh-color-black,#000),var(\--= rh-color-white,#fff));
font-size: 1.25rem; text-transform: uppercase; } .rhdocs dl { margin:
1rem 0px; } .rhdocs dl dt { font-weight: 600; margin: 0.5rem 0px; }
.rhdocs ol ol { list-style: lower-roman; } .rhdocs
.codeblock\--processed pf-clipboard-copy::part(input), .rhdocs .code=
block\--processed pf-clipboard-copy::part(span) { display: none; }
.calloutlist div.para { margin: 0px; } rh-alert.admonition {
margin-bottom: var(\--rh-space-lg,1rem); } .guibutton, .guimenu,
.guimenuitem { font-weight: 700; } .guibutton { font-size: 90%; padding:
0.1875rem; } .guibutton::before { content: \"\[\"; } .guibutton::after {
content: \"\]\"; } .docs-content-container, .rhdocs {
\--rh-table\--maxHeight: calc(100vh - 6.25= rem); color:
light-dark(var(\--rh-color-gray-95,#151515),var(\--rh-color-whit=
e,#fff)); font-family: RedHatText, \"Red Hat Text\", \"Helvetica Neue\",
Arial,= sans-serif; font-size: 1.125rem; line-height: 1.6667; tab-size:
4; } pre\[hidden\] { display: none; }
.codeblock\[class\]\[class\]\[class\]\[class\]\[class\] { max-width:
99999em; } .codeblock\_\_wrapper { background:
light-dark(var(\--rh-color-surface-lighter=
,#f2f2f2),var(\--rh-color-surface-dark,#383838)); margin: 1rem 0px;
overflow= : visible; position: relative; transform: translate(0px);
z-index: 0; } .codeblock\_\_inner-wrapper::after { content: \"\";
display: block; min-height:= 0.625rem; width: 4.375rem; }
.codeblock\_\_copy { \--pfe-clipboard\--icon\--Color\--hover: #06c;
appearance: n= one; background: rgb(240, 239, 239); height: 1.75rem;
left: calc(100% - 2.7= 5rem - var(\--scrollbar\_\_width, 0px)); padding:
0.3125rem 0.375rem; position= : absolute; top: 1rem; width: 1.75rem;
z-index: 2; } .codeblock\_\_inner-wrapper pre { border: 0px; max-height:
max-content; } .pfe-clipboard:not(\[copied\])
.pfe-clipboard\_\_text\--success, :host(:not(\[cop= ied\]))
.pfe-clipboard\_\_text\--success { display: none !important; }
.codeblock\[class\] { margin: 0px; overflow: visible; padding-right:
0px; } pre { display: inline; font-size: 0.8125rem; line-height:
1.42857; margin: = 0px 0px 0.625rem; word-break: break-all;
overflow-wrap: break-word; backgro= und-color:
light-dark(var(\--rh-color-surface-lighter,#f2f2f2),var(\--rh-colo=
r-surface-dark,#383838)); border: 0.0625rem solid rgb(204, 204, 204);
borde= r-radius: 0.25rem; } .docs-content-container pre, .rhdocs pre,
pre { color: light-dark(var(\--rh-=
color-gray-95,#151515),var(\--rh-color-white,#fff)); }
.docs-content-container pre, .rhdocs pre { background:
light-dark(var(\--rh-=
color-surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,#383838));
font-= family: RedHatMono, \"Red Hat Mono\", Consolas, monospace;
font-size: 0.875re= m; line-height: 1.6667; overflow-wrap: normal;
white-space: pre; word-break= : normal; } .rhdocs pre\[class\] {
line-height: 27px; overflow-x: auto; } rh-codeblock
pre\[class\]\[class\] { overflow-x: auto; }
.pfe-clipboard\_\_text\--success { background-color: rgb(221, 221, 221);
borde= r: 1px solid rgb(0, 0, 0); border-radius: 2px; }
.content-code-block-container { position: relative; }
.content-code-block-container .content-code-block-container-actions {
displ= ay: flex; flex-direction: column; height: auto; justify-content:
flex-start= ; position: absolute; right: 0px; top: 0px; width: 57px;
z-index: 2; } .content-code-block-container
.content-code-block-container-actions rh-tool= tip .shadow-fab {
align-items: center; background: rgba(0, 0, 0, 0); border= : none;
border-radius: var(\--rh-border-radius-default,3px); display: flex; =
height: var(\--rh-length-3xl,48px); justify-content: center; padding:
var(\--= rh-space-md,8px); width: var(\--rh-length-3xl,48px); }
.content-code-block-container .content-code-block-container-actions
rh-tool= tip .shadow-fab svg { color: var(\--rh-color-text-primary);
height: var(\--rh= -size-icon-02,24px); width:
var(\--rh-size-icon-02,24px); }
.content-code-block-container\[data-text-wrapped=3D\"true\"\]
rh-code-block pre= code { overflow-wrap: break-word; white-space:
pre-wrap; word-break: break= -word; }
.content-code-block-container\[data-text-wrapped=3D\"false\"\]
rh-code-block pr= e code { overflow-wrap: normal; white-space: pre;
word-break: normal; } \@media (max-width: 768px) { .rhdocs h1 {
font-size: 29px; line-height: 37.7px; } .rhdocs h2 { font-size: 24px;
line-height: 31.2px; } .rhdocs h3 { font-size: 20px; line-height: 26px;
} .rhdocs h4, .rhdocs h5 { font-size: 18px; line-height: 23.4px; } } \*,
::after, ::before { box-sizing: border-box; } :root { \--rh-space-xs:
4px; \--rh-space-sm: 6px; \--rh-space-md: 8px; \--rh-sp= ace-lg: 16px;
\--rh-space-xl: 24px; \--rh-space-2xl: 32px; \--rh-space-3xl: 48= px;
\--rh-space-4xl: 64px; \--rh-space-5xl: 80px; \--rh-space-6xl: 96px;
\--rh-= space-7xl: 128px; \--rh-font-size-body-text-xs: .75rem;
\--rh-font-size-body-= text-sm: .875rem; \--rh-font-size-body-text-md:
1rem; \--rh-font-size-body-te= xt-lg: 1.125rem;
\--rh-font-size-body-text-xl: 1.25rem; \--rh-font-size-body-= text-2xl:
1.5rem; \--rh-font-size-heading-xs: 1.25rem; \--rh-font-size-headin=
g-sm: 1.5rem; \--rh-font-size-heading-md: 1.75rem;
\--rh-font-size-heading-lg= : 2.25rem; \--rh-font-size-heading-xl:
2.5rem; \--rh-font-size-heading-2xl: 3= rem;
\--pfe-navigation\--logo\--maxWidth: 200px;
\--pfe-navigation\_\_logo\--heigh= t: 40px;
\--pfe-navigation\--fade-transition-delay: .5s; \--pfe-navigation\_\_na=
v-bar\--highlight-color: var( \--rh-color-brand-red-on-dark,#e00 );
\--pf-glob= al\--icon\--FontSize\--sm: .75rem; color-scheme: light dark;
} body, html { color:
light-dark(var(\--rh-color-text-primary-on-light,#151515=
),var(\--rh-color-text-primary-on-dark,#fff)); font-family: \"Red Hat
Text\", = sans-serif; font-size: var(\--rh-font-size-body-text-md,1rem);
line-height: = var(\--rh-line-height-body-text,1.5); margin: 0px; }
html.theme-light { color-scheme: light; \--header-select:
url(\"data:image/sv= g+xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'= 10\' height=3D\'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%2315= 1515\'
d=3D\'M.678 0h8.644c.596 0 .895.797.497 1.195l-4.372 4.58c-.298.3-.695=
.3-.993 0L.18 1.196C-.216.797.081 0 .678 0\'/%3E%3C/svg%3E\");
\--ai-foundatio= n-container: var(\--rh-color-surface-lighter,#f2f2f2);
\--ai-foundation-image= -wrapper:
url(/\_nuxt/ai-training-hero-blocks-light.DgHphzNg.webp); \--certif=
icate-container: var(\--rh-color-surface-lighter,#f2f2f2);
\--certificate-ima= ge-wrapper:
url(/\_nuxt/ai-training-hero-blocks-light.DgHphzNg.webp); \--sele=
ct-dropdown-image: url(\"data:image/svg+xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'= http://www.w3.org/2000/svg\' width=3D\'10\' height=3D\'6\'
fill=3D\'none\' viewBox= =3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%23151515\'
d=3D\'M.678 0h8.644c.596 0 .895.7= 97.497 1.195l-4.372
4.58c-.298.3-.695.3-.993 0L.18 1.196C-.216.797.081 0 .6= 78
0\'/%3E%3C/svg%3E\"); \--expert-hub-footer:
linear-gradient(327.3deg,#fff 5= 8.63%,#f2f2f2 80.42%);
\--expert-hub-footer-wrapper: url(/\_nuxt/bg-cta-band-=
desktop.B1GFcRCk.webp); \--expert-hub-footer-mobile-wrapper:
url(/\_nuxt/bg-c= ta-band-mobile.Ch8SmKy6.webp);
\--home-welcome-section: linear-gradient(0deg=
,var(\--rh-color-gray-10,#f2f2f2) 0%,var(\--rh-color-white,#fff) 50%);
\--home= -dark-dots-bg:
url(/\_nuxt/docs-new-hero-desktop-light.BvTdfw7R.webp); }
html.theme-dark { color-scheme: dark; \--header-select:
url(\"data:image/svg+= xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'10= \' height=3D\'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%23fff\'=
d=3D\'M.678 0h8.644c.596 0 .895.797.497 1.195l-4.372
4.58c-.298.3-.695.3-.9= 93 0L.18 1.196C-.216.797.081 0 .678
0\'/%3E%3C/svg%3E\"); \--ai-foundation-con= tainer:
linear-gradient(309deg,var(\--rh-color-purple-70,#21134d) 21.34%,var=
(\--rh-color-black,#000) 92.49%); \--ai-foundation-image-wrapper:
url(/\_nuxt/= ai-training-hero-blocks-dark.C-W6u3Az.webp);
\--certificate-container: linea=
r-gradient(309deg,var(\--rh-color-purple-70,#21134d)
21.34%,var(\--rh-color-b= lack,#000) 92.49%);
\--certificate-image-wrapper: url(/\_nuxt/ai-training-her=
o-blocks-dark.C-W6u3Az.webp); \--select-dropdown-image:
url(\"data:image/svg+= xml;charset=3Dutf-8,%3Csvg
xmlns=3D\'http://www.w3.org/2000/svg\' width=3D\'10= \' height=3D\'6\'
fill=3D\'none\' viewBox=3D\'0 0 10 6\'%3E%3Cpath fill=3D\'%23fff\'=
d=3D\'M.678 0h8.644c.596 0 .895.797.497 1.195l-4.372
4.58c-.298.3-.695.3-.9= 93 0L.18 1.196C-.216.797.081 0 .678
0\'/%3E%3C/svg%3E\"); \--expert-hub-footer= :
linear-gradient(90deg,#151515,#21134d); \--expert-hub-footer-wrapper:
url(= /\_nuxt/bg-cta-band-desktop.B1GFcRCk.webp);
\--expert-hub-footer-mobile-wrapp= er:
url(/\_nuxt/bg-cta-band-mobile-dark.tRg-muK0.webp);
\--home-welcome-secti= on:
linear-gradient(270deg,var(\--rh-color-black,#000)
0%,var(\--rh-color-pur= ple-80,#1b0d33) 100%); \--home-dark-dots-bg:
url(/\_nuxt/docs-new-hero-deskto= p-dark.Df7w36hb.webp); } h1 {
font-weight: var(\--rh-font-weight-heading-regular,400); } h1, h2, h3,
h4, h5, h6 { font-family: \"Red Hat Display\", sans-serif; } h2, h3, h4,
h5, h6 { font-weight: var(\--rh-font-weight-heading-medium,500);= } h1 {
font-size: var(\--rh-font-size-heading-xl,2.5rem); line-height: 52px; }
h2 { font-size: var(\--rh-font-size-heading-md,1.75rem); line-height:
36.4px= ; } h3 { font-size: var(\--rh-font-size-heading-sm,1.5rem);
line-height: 31.2px;= } h4 { font-size:
var(\--rh-font-size-heading-xs,1.25rem); line-height: 26px; = } h5 {
font-size: 18px; line-height: 23.4px; } main { line-height: 30px; }
main#main-content { background-color:
light-dark(var(\--rh-color-surface-lig=
htest,#fff),var(\--rh-color-surface-darkest,#151515)); } section {
padding-bottom: 3rem; padding-top: 3rem; } img { height: auto;
max-width: 100%; } a { color:
light-dark(var(\--rh-color-interactive-blue-darker,#06c),var(\--rh=
-color-interactive-primary-default-on-dark,#92c5f9)); text-decoration:
none= ; } a:hover { color:
light-dark(var(\--rh-color-interactive-blue-darkest,#004080=
),var(\--rh-color-interactive-primary-hover-on-dark,#b9dafc)); }
rh-alert.html-container a { text-decoration: underline; } .container {
padding-left: 12px; padding-right: 12px; } .container, .container-fluid
{ margin-left: auto; margin-right: auto; width= : 100%; }
.container-fluid { padding: 12px; } \@media (min-width: 576px) {
.container { max-width: 540px; } } \@media (min-width: 768px) {
.container { max-width: 720px; } } \@media (min-width: 992px) {
.container { max-width: 960px; } } \@media (min-width: 1200px) {
.container { min-width: 1140px; } } \@media (min-width: 1400px) {
.container { min-width: 1320px; } } .grid { display: grid; gap:
var(\--rh-space-xl,24px); } .grid-center { margin: auto; }
.grid.grid-col-2 { grid-template-columns: repeat(2, 1fr); }
.grid.grid-col-3 { grid-template-columns: repeat(3, 1fr); }
.grid.grid-col-4 { grid-template-columns: repeat(4, 1fr); }
.grid.grid-col-5 { grid-template-columns: repeat(5, 1fr); }
.grid.grid-col-6 { grid-template-columns: repeat(6, 1fr); }
.grid.grid-col-7 { grid-template-columns: repeat(7, 1fr); }
.grid.grid-col-8 { grid-template-columns: repeat(8, 1fr); }
.grid.grid-col-9 { grid-template-columns: repeat(9, 1fr); }
.grid.grid-col-10 { grid-template-columns: repeat(10, 1fr); }
.grid.grid-col-11 { grid-template-columns: repeat(11, 1fr); }
.grid.grid-col-12 { grid-template-columns: repeat(12, 1fr); } \@media
(min-width: 576px) { .grid.grid-col-sm-2 { grid-template-columns:
repeat(2, 1fr); } .grid.grid-col-sm-3 { grid-template-columns: repeat(3,
1fr); } .grid.grid-col-sm-4 { grid-template-columns: repeat(4, 1fr); }
.grid.grid-col-sm-5 { grid-template-columns: repeat(5, 1fr); }
.grid.grid-col-sm-6 { grid-template-columns: repeat(6, 1fr); }
.grid.grid-col-sm-7 { grid-template-columns: repeat(7, 1fr); }
.grid.grid-col-sm-8 { grid-template-columns: repeat(8, 1fr); }
.grid.grid-col-sm-9 { grid-template-columns: repeat(9, 1fr); }
.grid.grid-col-sm-10 { grid-template-columns: repeat(10, 1fr); }
.grid.grid-col-sm-11 { grid-template-columns: repeat(11, 1fr); }
.grid.grid-col-sm-12 { grid-template-columns: repeat(12, 1fr); } }
\@media (min-width: 768px) { .grid.grid-col-md-2 {
grid-template-columns: repeat(2, 1fr); } .grid.grid-col-md-3 {
grid-template-columns: repeat(3, 1fr); } .grid.grid-col-md-4 {
grid-template-columns: repeat(4, 1fr); } .grid.grid-col-md-5 {
grid-template-columns: repeat(5, 1fr); } .grid.grid-col-md-6 {
grid-template-columns: repeat(6, 1fr); } .grid.grid-col-md-7 {
grid-template-columns: repeat(7, 1fr); } .grid.grid-col-md-8 {
grid-template-columns: repeat(8, 1fr); } .grid.grid-col-md-9 {
grid-template-columns: repeat(9, 1fr); } .grid.grid-col-md-10 {
grid-template-columns: repeat(10, 1fr); } .grid.grid-col-md-11 {
grid-template-columns: repeat(11, 1fr); } .grid.grid-col-md-12 {
grid-template-columns: repeat(12, 1fr); } } \@media (min-width: 992px) {
.grid.grid-col-lg-2 { grid-template-columns: repeat(2, 1fr); }
.grid.grid-col-lg-3 { grid-template-columns: repeat(3, 1fr); }
.grid.grid-col-lg-4 { grid-template-columns: repeat(4, 1fr); }
.grid.grid-col-lg-5 { grid-template-columns: repeat(5, 1fr); }
.grid.grid-col-lg-6 { grid-template-columns: repeat(6, 1fr); }
.grid.grid-col-lg-7 { grid-template-columns: repeat(7, 1fr); }
.grid.grid-col-lg-8 { grid-template-columns: repeat(8, 1fr); }
.grid.grid-col-lg-9 { grid-template-columns: repeat(9, 1fr); }
.grid.grid-col-lg-10 { grid-template-columns: repeat(10, 1fr); }
.grid.grid-col-lg-11 { grid-template-columns: repeat(11, 1fr); }
.grid.grid-col-lg-12 { grid-template-columns: repeat(12, 1fr); } }
.span-1 { grid-column: span 1; } .span-2 { grid-column: span 2; }
.span-3 { grid-column: span 3; } .span-4 { grid-column: span 4; }
.span-5 { grid-column: span 5; } .span-6 { grid-column: span 6; }
.span-7 { grid-column: span 7; } .span-8 { grid-column: span 8; }
.span-9 { grid-column: span 9; } .span-10 { grid-column: span 10; }
.span-11 { grid-column: span 11; } .span-12 { grid-column: span 12; }
\@media (min-width: 399px) { .span-xs-1 { grid-column: span 1; }
.span-xs-2 { grid-column: span 2; } .span-xs-3 { grid-column: span 3; }
.span-xs-4 { grid-column: span 4; } .span-xs-5 { grid-column: span 5; }
.span-xs-6 { grid-column: span 6; } .span-xs-7 { grid-column: span 7; }
.span-xs-8 { grid-column: span 8; } .span-xs-9 { grid-column: span 9; }
.span-xs-10 { grid-column: span 10; } .span-xs-11 { grid-column: span
11; } .span-xs-12 { grid-column: span 12; } } \@media (min-width: 768px)
{ .span-md-1 { grid-column: span 1; } .span-md-2 { grid-column: span 2;
} .span-md-3 { grid-column: span 3; } .span-md-4 { grid-column: span 4;
} .span-md-5 { grid-column: span 5; } .span-md-6 { grid-column: span 6;
} .span-md-7 { grid-column: span 7; } .span-md-8 { grid-column: span 8;
} .span-md-9 { grid-column: span 9; } .span-md-10 { grid-column: span
10; } .span-md-11 { grid-column: span 11; } .span-md-12 { grid-column:
span 12; } } \@media (min-width: 992px) { .span-lg-1 { grid-column: span
1; } .span-lg-2 { grid-column: span 2; } .span-lg-3 { grid-column: span
3; } .span-lg-4 { grid-column: span 4; } .span-lg-5 { grid-column: span
5; } .span-lg-6 { grid-column: span 6; } .span-lg-7 { grid-column: span
7; } .span-lg-8 { grid-column: span 8; } .span-lg-9 { grid-column: span
9; } .span-lg-10 { grid-column: span 10; } .span-lg-11 { grid-column:
span 11; } .span-lg-12 { grid-column: span 12; } } \@media (min-width:
1025px) { .span-xl-1 { grid-column: span 1; } .span-xl-2 { grid-column:
span 2; } .span-xl-3 { grid-column: span 3; } .span-xl-4 { grid-column:
span 4; } .span-xl-5 { grid-column: span 5; } .span-xl-6 { grid-column:
span 6; } .span-xl-7 { grid-column: span 7; } .span-xl-8 { grid-column:
span 8; } .span-xl-9 { grid-column: span 9; } .span-xl-10 { grid-column:
span 10; } .span-xl-11 { grid-column: span 11; } .span-xl-12 {
grid-column: span 12; } } \@media (min-width: 1200px) { .span-2xl-1 {
grid-column: span 1; } .span-2xl-2 { grid-column: span 2; } .span-2xl-3
{ grid-column: span 3; } .span-2xl-4 { grid-column: span 4; }
.span-2xl-5 { grid-column: span 5; } .span-2xl-6 { grid-column: span 6;
} .span-2xl-7 { grid-column: span 7; } .span-2xl-8 { grid-column: span
8; } .span-2xl-9 { grid-column: span 9; } .span-2xl-10 { grid-column:
span 10; } .span-2xl-11 { grid-column: span 11; } .span-2xl-12 {
grid-column: span 12; } } \@media (min-width: 1440px) { .span-3xl-1 {
grid-column: span 1; } .span-3xl-2 { grid-column: span 2; } .span-3xl-3
{ grid-column: span 3; } .span-3xl-4 { grid-column: span 4; }
.span-3xl-5 { grid-column: span 5; } .span-3xl-6 { grid-column: span 6;
} .span-3xl-7 { grid-column: span 7; } .span-3xl-8 { grid-column: span
8; } .span-3xl-9 { grid-column: span 9; } .span-3xl-10 { grid-column:
span 10; } .span-3xl-11 { grid-column: span 11; } .span-3xl-12 {
grid-column: span 12; } } .flex { display: flex; flex-direction: column;
gap: var(\--rh-space-lg,16px)= ; } .flex-row { flex-direction: row; }
.flex-column { flex-direction: column; } \@media (min-width: 768px) {
.flex-md-row { flex-direction: row; } .flex-md-column { flex-direction:
column; } } .typography-h1 { font-size:
var(\--rh-font-size-heading-2xl,3rem); } .typography-h2 { font-size:
var(\--rh-font-size-heading-xl,2.5rem); } .typography-h3 { font-size:
var(\--rh-font-size-heading-lg,2.25rem); } .typography-h4 { font-size:
var(\--rh-font-size-heading-md,1.75rem); } .typography-h5 { font-size:
var(\--rh-font-size-heading-sm,1.5rem); } .typography-h6 { font-size:
var(\--rh-font-size-heading-xs,1.25rem); } .content section { padding:
0px; } .content h1, .content h2, .content h3, .content h4, .content h5,
.content h= 6 { margin: var(\--rh-space-lg,16px) 0; } .sr-only { height:
1px; margin: -1px; overflow: hidden; padding: 0px; posit= ion: absolute;
width: 1px; clip: rect(0px, 0px, 0px, 0px); border: 0px; }
.list-unstyled { list-style: none; padding-left: 0px; } .tooltip-content
{ align-items: center; display: flex; font-family: \"Red Ha= t Text\";
justify-content: center; text-transform: none; } .tooltip-content
.check-icon { margin-left: var(\--rh-space-md,8px); } .doc-image-link {
display: inline-block; text-decoration: none; } .modal-img { display:
block; width: 100%; } .modal-helper-text { margin-top: 0.5rem;
text-align: center; } .modal-helper-text a { color: rgb(0, 0, 0);
cursor: pointer; } .modal-helper-text a:hover { text-decoration:
underline; } .modal-helper-text a::after { content: \"=E2=BF=BB\";
margin-left: 0.25rem; } pf-modal.pf-img-modal {
\--pf-c-modal-box\--MaxHeight: 90vh; overflow-y: scro= ll; }
pf-modal.pf-img-modal::part(close-button) { background-color: rgb(255,
255,= 255); border-radius: 50%; color: rgb(0, 0, 0); margin-right:
-2rem; margin= -top: -2rem; }
pf-modal.pf-img-modal::part(close-button):hover { opacity: 0.7; }
rh-card { height: 100%; } h2.truste-title { line-height: normal;
margin-top: 0px; } rh-alert p\[slot=3D\"header\"\] { color: rgb(0, 41,
82); } section.rhdocs aside:target, section.rhdocs div:target,
section.rhdocs sect= ion:target { scroll-margin-top: 110px; } \@media
(max-width: 1439px) { html:has(div.content-wrapper) section.rhdocs
aside:target, html:has(div.c= ontent-wrapper) section.rhdocs div:target,
html:has(div.content-wrapper) se= ction.rhdocs section:target {
scroll-margin-top: 90px; } html:has(div.content-wrapper
rh-disclosure.tablet-jump-links-container) s= ection.rhdocs
aside:target, html:has(div.content-wrapper rh-disclosure.tabl=
et-jump-links-container) section.rhdocs div:target,
html:has(div.content-wr= apper
rh-disclosure.tablet-jump-links-container) section.rhdocs section:tar=
get { scroll-margin-top: 180px; } } \@media (max-width: 991px) {
html:has(nav.content-page-mobile-nav) section.rhdocs aside:target,
html:h= as(nav.content-page-mobile-nav) section.rhdocs div:target,
html:has(nav.con= tent-page-mobile-nav) section.rhdocs section:target {
scroll-margin-top: 60= px; }
html:has(nav.content-page-mobile-nav.hide-content-page-mobile-nav
rh-disc= losure.jump-links-container) section.rhdocs aside:target,
html:has(nav.cont= ent-page-mobile-nav.hide-content-page-mobile-nav
rh-disclosure.jump-links-c= ontainer) section.rhdocs div:target,
html:has(nav.content-page-mobile-nav.h= ide-content-page-mobile-nav
rh-disclosure.jump-links-container) section.rhd= ocs section:target {
scroll-margin-top: 20px; } html:has(nav.content-page-mobile-nav
rh-disclosure.jump-links-container) = section.rhdocs aside:target,
html:has(nav.content-page-mobile-nav rh-disclo=
sure.jump-links-container) section.rhdocs div:target,
html:has(nav.content-= page-mobile-nav
rh-disclosure.jump-links-container) section.rhdocs section:= target {
scroll-margin-top: 160px; } } .highlight { background: rgb(255, 244,
204); color: rgb(0, 0, 0); } \@media (max-width: 768px) { h1 {
font-size: 29px; line-height: 37.7px; } h2 { font-size: 24px;
line-height: 31.2px; } h3 { font-size: 20px; line-height: 26px; } h4, h5
{ font-size: 18px; line-height: 23.4px; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-09b61e25-6c79-497e-9866-181aad83e018@mhtml.blink \@charset
\"utf-8\"; .feedback-container\[data-v-9de855e7\] { align-items: center;
background-colo= r:
light-dark(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-=
darker,#1f1f1f)); display: flex; justify-content: flex-end; min-height:
48p= x; padding: var(\--rh-space-lg,16px) var(\--rh-space-2xl,32px); }
.toggle-theme-btn\[data-v-9de855e7\] { padding-left:
var(\--rh-space-xl,24px);= } \@media (max-width: 767px) {
.feedback-container\[data-v-9de855e7\] { padding:
var(\--rh-space-lg,16px); = } } \@media (max-width: 1024px) {
.toggle-theme-btn\[data-v-9de855e7\] { display: none; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-32b15471-2023-4932-a8e9-6b9210592f61@mhtml.blink \@charset
\"utf-8\"; section\[data-v-babbacad\] { padding: 0px; }
h1\[data-v-babbacad\], h2\[data-v-babbacad\] { margin: 0px; }
.main-error-container\[data-v-babbacad\] { background-color:
light-dark(var(-=
-rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
p= adding-bottom: var(\--rh-space-7xl,128px); padding-top:
var(\--rh-space-5xl,8= 0px); } .main-error\[data-v-babbacad\] {
background-color: light-dark(var(\--rh-color-=
surface-lighter,#f2f2f2),var(\--rh-color-surface-dark,#383838)); margin:
0px= auto; max-width: 44rem; padding: var(\--rh-space-3xl,48px); }
.cloud-IT-image\[data-v-babbacad\] { width: 9rem; }
.error-text-container p\[data-v-babbacad\] { color:
light-dark(#6a6e73,var(\--= rh-color-white,#fff)); font-size:
var(\--rh-font-size-body-text-lg,1.125rem)= ; }
.help-container\[data-v-babbacad\] { margin-top:
var(\--rh-space-4xl,64px); } .form-box-container\[data-v-babbacad\] {
justify-content: center; margin-top:= var(\--rh-space-xl,24px); }
.error-search-box\[data-v-babbacad\],
.form-box-container\[data-v-babbacad\] { = align-items: center; display:
flex; width: 100%; } .error-search-box\[data-v-babbacad\] {
justify-content: space-between; positi= on: relative; }
.search-icon-form\[data-v-babbacad\] { color:
light-dark(var(\--rh-color-gray-=
50,#707070),var(\--rh-color-status-neutral-on-dark,#c7c7c7)); left:
12px; po= sition: absolute; } .arrow-right-button\[data-v-babbacad\] {
color: light-dark(var(\--rh-color-gra=
y-95,#151515),var(\--rh-color-icon-secondary-on-dark,#fff)); }
.input-box\[data-v-babbacad\] { appearance: none; background-color:
light-dar=
k(var(\--rh-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f=
1f)); border-top-color: ; border-top-style: ; border-top-width: ;
border-bo= ttom-color: ; border-bottom-style: ; border-bottom-width: ;
border-left-col= or: ; border-left-style: ; border-left-width: ;
border-image-source: ; bord= er-image-slice: ; border-image-width: ;
border-image-outset: ; border-image= -repeat: ; border-right: none;
font-family: var(\--rh-font-family-body-text,= \"Red Hat
Text\",\"RedHatText\",Arial,sans-serif); font-size: var(\--rh-font-siz=
e-body-text-md,1rem); height: 36px; padding: 0px 40px; text-overflow:
ellip= sis; white-space: nowrap; width: 100%; }
.input-box\[data-v-babbacad\]::placeholder { color:
light-dark(var(\--rh-color=
-text-secondary-on-light,#4d4d4d),var(\--rh-color-text-secondary-on-dark,#c7=
c7c7)); font-family: var(\--rh-font-family-body-text,\"Red Hat
Text\",\"RedHatT= ext\",Arial,sans-serif); font-size:
var(\--rh-font-size-body-text-md,1rem); f= ont-weight:
var(\--rh-font-weight-code-regular,400); line-height: 24px; }
.form-box-container rh-button\[data-v-babbacad\]::part(button) {
align-items:= center; background-color:
light-dark(var(\--rh-color-gray-20,#e0e0e0),var(-=
-rh-color-status-neutral-on-light,#4d4d4d)); border-radius: 0px;
display: f= lex; height: 36px; justify-content: center;
\--\_default-border-color: light-=
dark(var(\--rh-color-gray-20,#e0e0e0),var(\--rh-color-status-neutral-on-light=
,#4d4d4d)); } .input-clear-btn\[data-v-babbacad\] { align-items: center;
background-color: = transparent; border: none; display: flex; height:
36px; justify-content: ce= nter; margin-right: -30px; outline: none;
transform: translate(-30px); } .input-clear-btn\[data-v-babbacad\]:focus
{ border: 1px solid var(\--rh-color-= accent-base-on-light,#06c); }
.input-clear-btn:focus .input-clear-icon\[data-v-babbacad\] { color:
var(\--rh= -color-gray-95,#151515); }
.input-clear-icon\[data-v-babbacad\] { color: rgb(107, 110, 114);
cursor: poi= nter; } .input-clear-icon\[data-v-babbacad\]:hover { color:
var(\--rh-color-gray-95,#1= 51515); } .help-links\[data-v-babbacad\] {
margin-top: var(\--rh-space-xl,24px); padding= : 0
var(\--rh-space-md,8px); } .help-links li\[data-v-babbacad\] { display:
inline-block; list-style: none; = margin-right:
var(\--rh-space-xl,24px); padding: var(\--rh-space-xs,4px) 0; }
.help-links li a\[data-v-babbacad\] { color:
light-dark(var(\--rh-context-ligh=
t-color-text-link,#06c),var(\--rh-color-blue-30,#92c5f9)); cursor:
pointer; = text-decoration: none; } \@media (max-width: 992px) {
.main-error\[data-v-babbacad\] { padding: var(\--rh-space-lg,16px); }
.cloud-IT-image\[data-v-babbacad\] { width: 6rem; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-a9d1a383-2631-4fae-be4d-2039ff10b1a3@mhtml.blink \@charset
\"utf-8\"; .theme-container\[data-v-9af16c28\] { height: 36px; position:
relative; } rh-button\[data-v-9af16c28\],
rh-button\[data-v-9af16c28\]::part(button) { heig= ht: 36px; }
rh-button\[variant=3D\"tertiary\"\]\[data-v-9af16c28\] {
\--rh-color-icon-secondar= y-on-dark:
var(\--rh-color-surface-darkest,#151515); \--rh-color-icon-seconda=
ry-on-light: var(\--rh-color-surface-lightest,#fff); }
rh-button\[variant=3D\"tertiary\"\].footer\[data-v-9af16c28\] {
\--rh-color-border= -strong: transparent; }
rh-button\[variant=3D\"tertiary\"\]\[data-v-9af16c28\]::part(button) {
padding: 1= 0px var(\--rh-space-lg,16px); }
rh-button\[variant=3D\"tertiary\"\].footer\[data-v-9af16c28\]::part(button)
{ pad= ding: 10px 0px; } .popover-container\[data-v-9af16c28\] {
background-color: light-dark(var(\--rh=
-color-surface-lightest,#fff),var(\--rh-color-surface-darker,#1f1f1f));
bord= er-radius: 6px; box-shadow: var( \--rh-box-shadow-md,0 4px 6px 1px
light-dar= k(hsla(0,0%,8%,.25),rgba(0,0,0,.5)) ); position: absolute;
right: 0px; top:= 42px; width: 168px; z-index: 1; }
.footer-popover-container\[data-v-9af16c28\] { left: 0px; top: 54px; }
.theme-list-container\[data-v-9af16c28\] { align-items: flex-start;
display: = flex; flex-direction: column; list-style: none; margin: 0px;
padding: var(-= -rh-space-md,8px) 0; } .theme-list\[data-v-9af16c28\] {
margin: 0px; padding: 0px; width: 100%; } .theme-list
button.theme-btn\[data-v-9af16c28\] { align-items: center; backgr=
ound-color: transparent; border: none; color:
light-dark(var(\--rh-color-gra=
y-95,#151515),var(\--rh-color-white,#fff)); cursor: pointer; display:
flex; = justify-content: flex-start; padding: var(\--rh-space-md,8px)
var(\--rh-space= -xl,24px); width: 100%; } button.theme-btn
span.theme-btn-text\[data-v-9af16c28\] { font-family: \"Red H= at
Text\"; font-size: var(\--rh-font-size-body-text-sm,.875rem);
font-weight:= var(\--rh-font-weight-body-text-regular,400);
padding-left: var(\--rh-space-= md,8px); }
button.theme-btn\[data-v-9af16c28\]:hover { background-color:
light-dark(var(=
\--rh-color-gray-20,#e0e0e0),var(\--rh-color-gray-70,#383838)); }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-b8fa2522-2ca6-4b54-a9ee-60fe1a5a5f61@mhtml.blink \@charset
\"utf-8\"; :root { \--pfe-navigation\_\_dropdown\--Color:
light-dark(var(\--rh-color-text-p=
rimary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff));
\--pfe-= navigation\_\_dropdown\--Background:
light-dark(var(\--rh-color-surface-lightes=
t,#fff),var(\--rh-color-surface-darker,#1f1f1f));
\--pfe-navigation\_\_nav-bar-= -toggle\--BackgroundColor\--active:
light-dark(var(\--rh-color-surface-lightes=
t,#fff),var(\--rh-color-surface-darker,#1f1f1f));
\--pfe-navigation\_\_nav-bar-= -Color\--active:
light-dark(var(\--rh-color-text-primary-on-light,#151515),va=
r(\--rh-color-text-primary-on-dark,#fff));
\--pfe-navigation\_\_dropdown\--separ= ator\--Border: 1px solid
light-dark(#d2d2d2,var(\--rh-color-border-subtle-on-= dark,#707070)); }
.section .titlepage { gap: 0.75rem; } .section .titlepage, div.edit {
align-items: center; display: flex; } div.edit { font-size: 0.9rem;
margin-bottom: 8px; } div.edit \> a { align-items: center; display:
flex; } .edit pf-icon { margin-right: 4px; }
rh-tile\[color-palette=3D\"darkest\"\] a { color:
var(\--rh-color-interactive-pr= imary-default-on-dark,#92c5f9); }
rh-tile\[color-palette=3D\"darkest\"\]:not(:defined) { background-color:
var(\--= rh-color-surface-darkest,#151515); border-color:
var(\--rh-color-border-subt= le-on-dark,#707070); color:
var(\--rh-color-text-primary-on-dark,#fff); }
rh-tile\[color-palette=3D\"darkest\"\]:not(:defined) img { aspect-ratio:
1 / 1;= width: 48px; }
rh-tile\[color-palette=3D\"darkest\"\]:not(:defined) img + h3 {
margin-block-st= art: var(\--rh-space-2xl,32px); } rh-tile a { color:
var(\--rh-color-interactive-primary-default,light-dark(va=
r(\--rh-color-interactive-primary-default-on-light,#06c),var(\--rh-color-inte=
ractive-primary-default-on-dark,#92c5f9))); } rh-tile:not(:defined) {
background-color: light-dark(var(\--rh-color-surface=
-lightest,#fff),var(\--rh-color-surface-darkest,#151515)); border:
var(\--rh-= border-width-sm,1px) solid
var(\--rh-color-border-subtle,light-dark(var(\--rh=
-color-border-subtle-on-light,#c7c7c7),var(\--rh-color-border-subtle-on-dark=
,#707070))); color:
var(\--rh-color-text-primary,light-dark(var(\--rh-color-t=
ext-primary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff)));
= padding: var(\--rh-space-2xl,32px) var(\--rh-space-2xl,32px)
var(\--rh-space-3= xl,48px) var(\--rh-space-2xl,32px); }
rh-tile:not(:defined) img { aspect-ratio: 1 / 1; width: 48px; }
rh-tile:not(:defined) img + h3 { margin-block-start:
var(\--rh-space-2xl,32p= x); } rh-card.explore-products { color:
var(\--rh-color-text-primary,light-dark(va=
r(\--rh-color-text-primary-on-light,#151515),var(\--rh-color-text-primary-on-=
dark,#fff))); } rh-card.explore-products:not(:defined) { align-items:
center; display: flex= ; flex-direction: column; justify-content:
center; } rh-card.explore-products:not(:defined) h4 { font-size:
var(\--rh-font-size-h= eading-sm,1.5rem); padding-bottom:
var(\--rh-space-lg,16px); } rh-card.explore-products:not(:defined)
rh-cta\[variant=3D\"secondary\"\]:not(:d= efined) { border:
var(\--rh-border-width-sm,1px) solid var(\--rh-color-border=
-strong,light-dark(var(\--rh-color-border-strong-on-light,#151515),var(\--rh-=
color-border-strong-on-dark,#fff))); border-radius:
var(\--rh-border-radius-= default,3px); max-width: fit-content;
padding-block: var(\--rh-space-lg,16px= ); padding-inline:
var(\--rh-space-2xl,32px); } rh-card.explore-products:not(:defined)
rh-cta\[variant=3D\"secondary\"\]:not(:d= efined) a { color:
var(\--rh-color-text-primary,light-dark(var(\--rh-color-te=
xt-primary-on-light,#151515),var(\--rh-color-text-primary-on-dark,#fff)));
}
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-0eb8be96-e78d-4b5f-8827-0691bc6a8dc1@mhtml.blink \@charset
\"utf-8\"; .ta-display-none { display: none; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-df1c3ef7-2a44-4c27-8279-9666a4eb0507@mhtml.blink \@charset
\"utf-8\"; \@font-face { font-family: \"Source Sans Pro\"; src:
url(\"https://consent.trus=
tarc.com/get?name=3DSourceSansPro-Regular.ttf\") format(\"truetype\"),
url(\"ht=
tps://consent.trustarc.com/get?name=3DSourceSansPro-Regular.woff\")
format(\"= woff\"),
url(\"https://consent.trustarc.com/get?name=3DSourceSansPro-Regular.=
otf\") format(\"opentype\"); } .truste_cursor_pointer { cursor: pointer;
} .truste_border_none { border: none; } .truste_accessible_link {
font-family: \"Source Sans Pro\", sans-serif; color= : rgb(29, 78, 216);
font-size: 14px; font-weight: 600; text-decoration: und= erline; }
.truste_accessible_link:hover { color: rgb(29, 78, 216);
text-decoration: n= one !important; }
.truste_accessible_link:focus-visible { outline: none; border-radius:
4px; = box-shadow: rgb(255, 255, 255) 0px 0px 0px 1px, rgb(54, 153, 241)
0px 0px 0= px 4px; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-32ce7430-cab1-47e3-b92c-edeb825d1b6c@mhtml.blink \@charset
\"utf-8\"; .truste_caIcon_display { display: block !important; }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-f5bbd928-d9bd-422a-a795-064a8b9afb02@mhtml.blink \@charset
\"utf-8\"; .rh-target-pzn1827950 { & .dx-bg-white { background-color:
rgb(255, 255, 255) !important; } & .dx-relative { position: relative
!important; } & .dx-pl-2 { padding-left: 16px !important; } \@media
(min-width: 992px) { & .lg\\:dx-pl-0 { padding-left: 0px !important; } }
& .dx-py-2 { padding-top: 16px !important; padding-bottom: 16px
!importan= t; } & .dx-flex { display: flex !important; } & .dx-flex-row
{ flex-direction: row !important; } & .dx-justify-start {
justify-content: flex-start !important; } \@media (min-width: 992px) { &
.lg\\:dx-justify-center { justify-content: center !important; } }
\@media (min-width: 992px) { & .lg\\:dx-items-center { align-items:
center !important; } } & \[class\*=3D\"dx-border\"\] { border-style:
solid; border-width: 0px; } & .dx-border { border-width: 1px !important;
} & .dx-border-gray-30 { border-color: rgb(199, 199, 199) !important; }
& .dx-items-start { align-items: flex-start !important; } & .dx-mr-2 {
margin-right: 16px !important; } \@media (min-width: 1200px) { &
.xl\\:dx-mr-4 { margin-right: 32px !important; } } & .dx-flex-col {
flex-direction: column !important; } \@media (min-width: 992px) { &
.lg\\:dx-flex-row { flex-direction: row !important; } } & .dx-text-16 {
font-size: 1rem !important; } \@media (min-width: 992px) { &
.lg\\:dx-text-18 { font-size: 1.125rem !important; } } & .dx-mb-0 {
margin-bottom: 0px !important; } & .dx-mt-0 { margin-top: 0px
!important; } & .dx-pb-0 { padding-bottom: 0px !important; } & .dx-pr-7
{ padding-right: 56px !important; } \@media (min-width: 992px) { &
.lg\\:dx-pr-2 { padding-right: 16px !important; } } \@media (min-width:
1200px) { & .xl\\:dx-pr-4 { padding-right: 32px !important; } } &
.dx-items-center { align-items: center !important; } & .dx-absolute {
position: absolute !important; } & .dx-p-0 { padding: 0px !important; }
& .dx-justify-center { justify-content: center !important; } & .dx-block
{ display: block !important; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/css Content-Transfer-Encoding: quoted-printable
Content-Location:
cid:css-77db7b0d-f205-4e58-bd96-ac0f0f75cd9b@mhtml.blink \@charset
\"utf-8\"; .rh-target-pzn1827950 { & .pzn1827950-banner-close { right:
10px; top: 10px; border: none; cursor= : pointer; background: 0px 0px; }
& rh-cta { bottom: 2px; } & .rh-target-pzn1827950-logo { max-width:
48px; max-height: 48px; } }
\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/html Content-ID: Content-Transfer-Encoding:
quoted-printable Content-Location:
https://consent.trustarc.com/get?name=crossdomain.html&domain=redhat.com

\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/html Content-ID: Content-Transfer-Encoding:
quoted-printable

\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/html Content-ID: Content-Transfer-Encoding:
quoted-printable Content-Location:
https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/login-status-iframe.html

=20 =20

\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\--
Content-Type: text/html Content-ID: Content-Transfer-Encoding:
quoted-printable

\-\-\-\-\--MultipartBoundary\--zxfy1cY7F2RZ8FgrghABtDUhChKg401sMHoPQ0vDEL\-\-\-\-\--
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
:::
