<%!
import datetime
today = datetime.date.today()
%>

<h1>Bookmark history for ${today.strftime('%d %b, %Y')}</h1>

<ul>
  % for bookmark in bookmarks:
  <li><a href="${bookmark['href']}">${bookmark['description']}</a> on <span class="date">${bookmark['date_formatted']}</span>
    % if bookmark['description']:
    <span class="description">${bookmark['description']}</span>
    % endif
    % for tag in bookmark['tags']:
    <span class="tag">${tag}</span>
    % endfor
  </li>
  % endfor
</ul>
