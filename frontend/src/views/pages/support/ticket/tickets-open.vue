<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <ticketlistheader :title="title" :name="name" :text="text" />
      <searchfilter />
      <card />
      <tickettab />
      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'TicketID'">
                      <router-link to="/invoices/invoice-details" class="invoice-link">{{
                        record.TicketID
                      }}</router-link></template>
                    <template v-else-if="column.key === 'Assigned'">
                      <h2 class="table-avatar d-flex">
                        <span class="avatar avatar-sm me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.img}`)" alt="User Image" /></span>
                        <span>{{ record.Assigned }}</span>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Assignee'">
                      <h2 class="table-avatar d-flex">
                        <a class="avatar avatar-sm me-2"><img class="avatar-img rounded-circle"
                            :src="require(`@/assets/img/profiles/${record.img1}`)" alt="User Image" /></a>
                        <a>{{ record.Assignee }}<span>{{ record.num }}</span></a>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Priority'">
                      <span v-if="record.Priority === 'Medium'" class="badge bg-warning-light text-warning-light">{{
                        record.Priority }}</span>
                      <span v-if="record.Priority === 'High'" class="badge bg-danger-light">{{ record.Priority }}</span>
                      <span v-if="record.Priority === 'Low'" class="badge bg-primary-light">{{ record.Priority
                      }}</span></template>
                    <template v-else-if="column.key === 'Status'">
                      <span class="badge bg-danger-light">{{ record.Status }}</span>
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <div class="dropdown dropdown-action">
                          <a href="javascript:;" class="btn-action-icon" data-bs-toggle="dropdown"
                            aria-expanded="false"><i class="fas fa-ellipsis-v"></i></a>
                          <div class="dropdown-menu dropdown-menu-right">
                            <ul>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);"><i
                                    class="far fa-edit me-2"></i>Edit</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);"><i
                                    class="far fa-trash-alt me-2"></i>Delete</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);"><i
                                    class="far fa-eye me-2"></i>View</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);"><i
                                    class="far fa-bell me-2"></i>Active</a>
                              </li>
                              <li>
                                <a class="dropdown-item" href="javascript:void(0);"><i
                                    class="far fa-bell-slash me-2"></i>Deactivate</a>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Table -->
    </div>
  </div>
  <!-- /Page Wrapper -->
  <ticketmodal />
</template>
<script>
const columns = [
  {
    title: "Ticket ID",
    key: "TicketID",
    dataIndex: "TicketID",
    sorter: {
      compare: (a, b) => {
        a = a.TicketID.toLowerCase();
        b = b.TicketID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Subject",
    dataIndex: "Subject",
    sorter: {
      compare: (a, b) => {
        a = a.Subject.toLowerCase();
        b = b.Subject.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Assigned",
    dataIndex: "Assigned",
    key: "Assigned",
    sorter: {
      compare: (a, b) => {
        a = a.Assigned.toLowerCase();
        b = b.Assigned.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Assigned Date",
    dataIndex: "AssignedDate",
    sorter: {
      compare: (a, b) => {
        a = a.AssignedDate.toLowerCase();
        b = b.AssignedDate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created On",
    dataIndex: "CreatedOn",
    sorter: {
      compare: (a, b) => {
        a = a.CreatedOn.toLowerCase();
        b = b.CreatedOn.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Due Date",
    dataIndex: "DueDate",
    sorter: {
      compare: (a, b) => {
        a = a.DueDate.toLowerCase();
        b = b.DueDate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Assignee",
    dataIndex: "Assignee",
    key: "Assignee",
    sorter: {
      compare: (a, b) => {
        a = a.Assignee.toLowerCase();
        b = b.Assignee.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Last Reply",
    dataIndex: "LastReply",
    sorter: {
      compare: (a, b) => {
        a = a.LastReply.toLowerCase();
        b = b.LastReply.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Priority",
    dataIndex: "Priority",
    key: "Priority",
    sorter: {
      compare: (a, b) => {
        a = a.Priority.toLowerCase();
        b = b.Priority.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Status",
    dataIndex: "Status",
    key: "Status",
    sorter: {
      compare: (a, b) => {
        a = a.Assignee.toLowerCase();
        b = b.Assignee.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "Action",
  },
];
const data = [
  {
    TicketID: "#4987",
    img: "avatar-07.jpg",
    img1: "avatar-14.jpg",
    Subject: "Support for theme",
    Assigned: "Charles Hafner",
    AssignedDate: "17 Dec 2023",
    CreatedOn: "19 Dec 2023, 6:12PM",
    DueDate: "16 Jan 2023",
    Assignee: "John Smith",
    num: "+1 843-443-3282",
    LastReply: "18 Jan 2023",
    Priority: "Medium",
    Status: "Open",
  },
  {
    TicketID: "#4988",
    img: "avatar-04.jpg",
    img1: "avatar-15.jpg",
    Subject: "verify your email",
    Assigned: "Michel",
    AssignedDate: "21 Dec 2023",
    CreatedOn: "23 Dec 2023, 6:12PM",
    DueDate: "28 Feb 2023",
    Assignee: "Johnny",
    num: "+1 843-443-4298",
    LastReply: "21 Jan 2023",
    Priority: "Low",
    Status: "Open",
  },
];
export default {
  setup() {
    return {
      title: "Tickets Open",
      name: "New Tickets",
      text: "#add_ticket",
      data,
      columns,
    };
  },
};
</script>
