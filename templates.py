def base_template():
    return """<h2>{month-count} Month Warning</h2>
<p><a href="{path-to-file}">click to see Properties</a></p>
<p>This is a {email-type} alert for the following property:</p>
<h3>{property-name}</h3>
<p>
	{address-lines} <br>
	{town} <br>
	{county} <br>
	{post-code}
</p>

<p>
	Landlord: {landlord} <br>
	Tenant: {tenant}
</p>

<p>
	{extra-content}
	Property Purchase Value: {purchase-value} <br>
	Property Size: {property-size}
</p>
"""