<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <domain-header></domain-header>
      <!-- /Page Header -->

      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="input-block mb-3">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table
                  class="table table-stripped table-hover datatable"
                  :columns="columns"
                  :data-source="data"
                >
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Name'">
                      <h2 class="table-avatar">
                        <router-link
                          to="/profile"
                          class="company-avatar avatar-md me-2 companies company-icon"
                        >
                          <img
                            class="avatar-img rounded-circle company"
                            :src="require(`@/assets/img/companies/${record.Image}`)"
                            alt="Company Image"
                        /></router-link>
                        <a href="#">{{ record.Name }}</a>
                      </h2>
                    </template>
                    <template v-else-if="column.key === 'Plan'">
                      <div>
                        {{ record.Plan }}
                        <span class="plane-type">{{ record.Type }}</span>
                      </div>
                    </template>
                    <template v-else-if="column.key === 'Status'">
                      <span :class="record.Class"
                        ><i :class="record.Class1"></i>{{ record.Status }}</span
                      >
                    </template>
                    <template v-else-if="column.key === 'Action'">
                      <div class="d-flex align-items-center">
                        <div class="dropdown dropdown-action">
                          <a
                            href="#"
                            class="btn-action-icon"
                            data-bs-toggle="dropdown"
                            aria-expanded="false"
                            ><i class="fas fa-ellipsis-v"></i
                          ></a>
                          <div class="dropdown-menu dropdown-menu-end">
                            <ul class="dropdown-ul">
                              <li>
                                <a
                                  class="dropdown-item"
                                  href="javascript:void(0);"
                                  data-bs-toggle="modal"
                                  data-bs-target="#view_doamin"
                                  ><i class="feather feather-eye me-2"></i>Domain
                                  Detail</a
                                >
                              </li>
                              <li class="delete-alt">
                                <div>
                                  <a
                                    class="dropdown-item"
                                    href="javascript:void(0);"
                                    data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"
                                    ><i class="feather feather-trash-2 me-2"></i>Delete</a
                                  >
                                </div>
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
  <domain-modal></domain-modal>
</template>

<script>
const columns = [
  {
    title: "#",
    dataIndex: "id",
    sorter: {
      compare: (a, b) => {
        a = a.id.toLowerCase();
        b = b.id.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Name",
    dataIndex: "Name",
    key: "Name",
    sorter: {
      compare: (a, b) => {
        a = a.Name.toLowerCase();
        b = b.Name.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Domain URL",
    dataIndex: "DomainURL",
    sorter: {
      compare: (a, b) => {
        a = a.DomainURL.toLowerCase();
        b = b.DomainURL.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Plan",
    dataIndex: "Plan",
    key: "Plan",
    sorter: {
      compare: (a, b) => {
        a = a.Plan.toLowerCase();
        b = b.Plan.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Registered On",
    dataIndex: "RegisteredOn",
    sorter: {
      compare: (a, b) => {
        a = a.RegisteredOn.toLowerCase();
        b = b.RegisteredOn.toLowerCase();
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
        a = a.Status.toLowerCase();
        b = b.Status.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Action",
    key: "Action",
    sorter: true,
  },
];

const data = [
  {
    id: "1",
    Name: "Hermann Groups",
    DomainURL: "hru.example.com",
    Plan: "Advanced",
    Type: "(Monthly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-01.svg",
    Status: "Approved",
    Class1: "feather feather-check me-1",
    Class: "badge bg-success-light d-inline-flex align-items-center",
  },
  {
    id: "2",
    Name: "Skiles LLC",
    DomainURL: "sk.example.com",
    Plan: "Basic",
    Type: "(Yearly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-02.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "3",
    Name: "Kerluke Group",
    DomainURL: "kerluke.example.com",
    Plan: "Basic",
    Type: "(Yearly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-03.svg",
    Status: "Rejected",
    Class1: "feather feather-x me-1",
    Class: "badge bg-danger-light d-inline-flex align-items-center",
  },
  {
    id: "4",
    Name: "Schowalter Group",
    DomainURL: "schowalter.example.com",
    Plan: "Advanced",
    Type: "(Monthly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-04.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "5",
    Name: "Accentric Global",
    DomainURL: "accentric.example.com",
    Plan: "Basic",
    Type: "(Yearly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-05.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "6",
    Name: "Dexter Matrix",
    DomainURL: "dexter.example.com",
    Plan: "Advanced",
    Type: "(Monthly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-06.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "7",
    Name: "Emporis Technologies",
    DomainURL: "emporis.example.com",
    Plan: "Basic",
    Type: "(Yearly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-07.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "8",
    Name: "Beacon Softwares",
    DomainURL: "beacon.example.com",
    Plan: "Advanced",
    Type: "(Monthly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-08.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "9",
    Name: "Global tech",
    DomainURL: "global.example.com",
    Plan: "Basic",
    Type: "(Yearly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-09.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
  {
    id: "10",
    Name: "High Tech Lead",
    DomainURL: "high.example.com",
    Plan: "Basic",
    Type: "(Yearly)",
    RegisteredOn: "19 Jan 2024",
    Image: "company-10.svg",
    Status: "Pending",
    Class1: "feather feather-clock me-1",
    Class: "badge bg-orange-light d-inline-flex align-items-center",
  },
];

export default {
  data() {
    return {
      title: "Domain",
      DeleteTitle: "Delete Domain",
      columns,
      data,
    };
  },
};
</script>
