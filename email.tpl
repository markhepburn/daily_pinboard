<%!
import datetime
today = datetime.date.today()
%>

<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta charset="utf-8">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings xmlns:o="urn:schemas-microsoft-com:office:office">
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <style>
    td,th,div,p,a,h1,h2,h3,h4,h5,h6 {font-family: "Segoe UI", sans-serif; mso-line-height-rule: exactly;}
  </style>
  <![endif]-->
    <title>Daily Pinboard</title>
    <style>
.hover-bg-gray-300:hover {
  background-color: #d1d5db !important;
}
.hover-underline:hover {
  text-decoration: underline !important;
}
@media (max-width: 600px) {
  .sm-w-full {
    width: 100% !important;
  }
  .sm-px-24 {
    padding-left: 24px !important;
    padding-right: 24px !important;
  }
  .sm-leading-32 {
    line-height: 32px !important;
  }
}
</style>
</head>
<body style="margin: 0; width: 100%; padding: 0; word-break: break-word; -webkit-font-smoothing: antialiased; background-color: #f3f4f6;">
  <div role="article" aria-roledescription="email" aria-label="Daily Pinboard" lang="en">
    <table style="width: 100%; padding-top: 48px; padding-bottom: 48px; font-family: ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif;" cellpadding="0" cellspacing="0" role="presentation">
      <tr>
        <td align="center" style="background-color: #f3f4f6;">
          <table class="sm-w-full" style="width: 600px;" cellpadding="0" cellspacing="0" role="presentation">
            <tr>
              <td align="center" class="sm-px-24">
                <table style="width: 100%;" cellpadding="0" cellspacing="0" role="presentation">
                  <tr>
                    <td class="sm-px-24" style="border-radius: 4px; background-color: #ffffff; padding-left: 48px; padding-right: 48px; text-align: left; font-size: 16px; line-height: 24px; color: #1f2937;">
                      <p class="sm-leading-32" style="margin: 0; margin-top: 24px; margin-bottom: 12px; font-size: 24px; font-weight: 600; color: #000000;">Your daily links for ${today.strftime('%d %b, %Y')}</p>
                    </td>
                  </tr>
                  % for bookmark in bookmarks:
                  <tr>
                    <td class="sm-px-24" style="border-radius: 4px; background-color: #ffffff; padding-left: 48px; padding-right: 48px; padding-top: 12px; padding-bottom: 12px; text-align: left; font-size: 16px; color: #1f2937;">
                      <table style="width: 100%;" cellpadding="0" cellspacing="0" role="presentation">
                        <tr>
                          <td style="padding-top: 12px; padding-bottom: 12px;">
                            <div style="height: 1px; background-color: #e5e7eb; line-height: 1px;">&zwnj;</div>
                          </td>
                        </tr>
                      </table>
                      <p>
                        <a class="hover-underline" href="${bookmark['href']}" style="color: #1d4ed8; text-decoration: none;">${bookmark['description']}</a><br>
                        <span style="font-size: 12px; color: #9ca3af;">Saved on ${bookmark['date_formatted']}.</span>
                      </p>
                      % if bookmark['extended']:
                      <p style="font-style: italic;">${bookmark['extended']}</p>
                      % endif
                      % if bookmark['tags']:
                      <div style="margin-top: 3px; margin-bottom: 3px; display: flex; flex-wrap: wrap;">
                        % for tag in bookmark['tags']:
                        <span class="hover-bg-gray-300" style="margin: 2px; display: inline-flex; align-items: center; border-radius: 9999px; background-color: #e5e7eb; padding-top: 2px; padding-bottom: 2px; padding-left: 8px; padding-right: 8px; font-size: 14px;">${tag}</span>
                        % endfor
                      </div>
                      % endif
                    </td>
                  </tr>
                  % endfor
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </div>
</body>
</html>
