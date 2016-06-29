# Integration-of-IoTronic-in-OpenStack-the-Web-Horizon-dashboard-approach
The goal of the proposed project is to integrate, through the dashboard OpenStack Horizon, a new service developed within the university of Messina. The service in question is Iotronic and to achieve this, you need to integrate it, following standards and rules imposed by the structure of the dashboard. This is why the Dashboard is working with a particular high-level Python Web framework that is Django.


Assuming you've OpenStack and the Iotronic service installed on your host:

You have to copy the "iotronic.py" file and the "__init__.py" file here: /usr/share/openstack -dashboard/openstack_dashboard/api/
You have to copy the "_50_mydashboard.py" here:/usr/share/openstack -dashboard/openstack_dashboard/enabled
You have to copy the "mydashboard" directory here: /usr/share/openstack-dashboard/openstack_dashboard/dashboards

The Iotronic service allows you to use its functionality in Horizon, like adding a node, deleting a node, showing the list of the created nodes and showing the datails of single node, by the complex actions in the table.
