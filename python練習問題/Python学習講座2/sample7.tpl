<ul> 
    {% for item in items -%}
    <li>{{ item | escape}}</li>
    {% endfor %}
</ul>