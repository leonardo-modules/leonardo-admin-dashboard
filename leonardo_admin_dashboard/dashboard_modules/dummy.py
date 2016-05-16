
from django.core.urlresolvers import reverse
from django.forms import Widget
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html


class DummyChartWidget(Widget):
    module = None
    title = 'Dummy visitors chart'

    def render(self, name, value, attrs=None):
        return format_html("""
<div class="dashboard-item-content contrast" style="height: 188px; overflow-x: auto;">
    <div class="padding center">
        <canvas id="chart_8" style="width: 330px; height: 165px;" width="330" height="165">
            <div class="chart-fillColor"></div>
            <div class="chart-strokeColor"></div>
            <div class="chart-pointColor"></div>
            <div class="chart-pointHighlightFill"></div>
            <div class="chart-scaleGridLineColor"></div>
            <div class="chart-scaleLineColor"></div>
            <div class="chart-scaleFontColor"></div>
            <div class="chart-data">
                
                    <div class="chart-data-item" data-date="10/05" data-value="19"></div>
                
                    <div class="chart-data-item" data-date="11/05" data-value="18"></div>
                
                    <div class="chart-data-item" data-date="12/05" data-value="15"></div>
                
                    <div class="chart-data-item" data-date="13/05" data-value="12"></div>
                
                    <div class="chart-data-item" data-date="14/05" data-value="2"></div>
                
                    <div class="chart-data-item" data-date="15/05" data-value="6"></div>
                
                    <div class="chart-data-item" data-date="16/05" data-value="0"></div>
                
            </div>
        </canvas>
        <script>jet.jQuery('#chart_8').googleAnalyticsChart();</script>
    </div>

</div>
""")

class DummyVisitorsWidget(Widget):
    module = None
    title = 'Dummy Analytics visitors'

    def render(self, name, value, attrs=None):
        return format_html("""
<div class="dashboard-item-content" style="height: 255px;">



    <table class="table">
        <thead>
            <tr>
                <th>Date</th>
                <th>Users</th>
                <th>Sessions</th>
                <th>Views</th>
            </tr>
        </thead>
        <tbody>
            
                <tr>
                    <th>May 16, 2016</th>
                    <td width="1" align="center">0</td>
                    <td width="1" align="center">0</td>
                    <td width="1" align="center">0</td>
                </tr>
            
                <tr>
                    <th>May 15, 2016</th>
                    <td width="1" align="center">6</td>
                    <td width="1" align="center">6</td>
                    <td width="1" align="center">22</td>
                </tr>
            
                <tr>
                    <th>May 14, 2016</th>
                    <td width="1" align="center">2</td>
                    <td width="1" align="center">2</td>
                    <td width="1" align="center">6</td>
                </tr>
            
                <tr>
                    <th>May 13, 2016</th>
                    <td width="1" align="center">12</td>
                    <td width="1" align="center">13</td>
                    <td width="1" align="center">117</td>
                </tr>
            
                <tr>
                    <th>May 12, 2016</th>
                    <td width="1" align="center">15</td>
                    <td width="1" align="center">21</td>
                    <td width="1" align="center">159</td>
                </tr>
            
                <tr>
                    <th>May 11, 2016</th>
                    <td width="1" align="center">18</td>
                    <td width="1" align="center">20</td>
                    <td width="1" align="center">201</td>
                </tr>
            
                <tr>
                    <th>May 10, 2016</th>
                    <td width="1" align="center">19</td>
                    <td width="1" align="center">19</td>
                    <td width="1" align="center">214</td>
                </tr>
            
        </tbody>
    </table>


</div>
""")


class DummyOnlineWidget(Widget):
    module = None
    title = 'Dummy Analytics Online'

    def render(self, name, value, attrs=None):
        return format_html("""
<div class="dashboard-item-content contrast" style="height: 59px;">


    <div class="padding center">
        <ul class="inline bordered">
                <li>
                    <div class="big">145</div>
                    <div class="dim">users</div>
                </li>
                <li>
                    <div class="big">213</div>
                    <div class="dim">sessions</div>
                </li>
                <li>
                    <div class="big">1536</div>
                    <div class="dim">views</div>
                </li>
        </ul>
    </div>
</div>
""")
