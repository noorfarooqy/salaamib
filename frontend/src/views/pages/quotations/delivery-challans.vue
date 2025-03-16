<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <quotationsheader :title="title" :text="text" />

        <!-- Search Filter -->
        <div id="filter_inputs" class="card filter-card">
          <div class="card-body pb-0">
            <div class="row">
              <div class="col-sm-6 col-md-3">
                <div class="form-group">
                  <label>Name</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
              <div class="col-sm-6 col-md-3">
                <div class="form-group">
                  <label>Email</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
              <div class="col-sm-6 col-md-3">
                <div class="form-group">
                  <label>Phone</label>
                  <input type="text" class="form-control" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /Search Filter -->

        <div class="row">
          <div class="col-sm-12">
            <div class="card-table">
              <div class="card-body">
                <div class="table-responsive">
                  <a-table
                    class="stripped table-hover"
                    :columns="columns"
                    :data-source="data"
                  >
                    <template #bodyCell="{ column, record }">
                      <template v-if="column.key === 'id'">
                        <h2 class="table-avatar d-flex">
                          <router-link to="/profile" class="avatar avatar-sm me-2"
                            ><img
                              class="avatar-img rounded-circle"
                              :src="require(`@/assets/img/profiles/${record.img}`)"
                              alt="User Image"
                          /></router-link>
                          <router-link to="/profile"
                            >{{ record.Customer }}
                            <span>{{ record.number }}</span></router-link
                          >
                        </h2>
                      </template>
                      <template v-else-if="column.key === 'action'">
                        <div class="text-start">
                          <div class="dropdown dropdown-action">
                            <a
                              href="#"
                              class="btn-action-icon"
                              data-bs-toggle="dropdown"
                              aria-expanded="false"
                              ><i class="fas fa-ellipsis-v"></i
                            ></a>
                            <div
                              class="dropdown-menu dropdown-menu-right quatation-dropdown"
                            >
                              <ul>
                                <li>
                                  <router-link
                                    class="dropdown-item"
                                    to="/quotations/edit-delivery-challans"
                                    ><i class="far fa-edit me-2"></i>Edit</router-link
                                  >
                                </li>
                                <li>
                                  <a
                                    class="dropdown-item"
                                    href="javascript:void(0);"
                                    data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"
                                    ><i class="far fa-trash-alt me-2"></i>Delete</a
                                  >
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-eye me-2"></i>View</a
                                  >
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-file-text me-2"></i>Convert
                                    to Invoice</a
                                  >
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-send me-2"></i>Send</a
                                  >
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-copy me-2"></i>Clone</a
                                  >
                                </li>
                                <li>
                                  <a class="dropdown-item" href="javascript:void(0);"
                                    ><i class="feather feather-download me-2"></i
                                    >Download</a
                                  >
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
      </div>
    </div>
    <!-- /Page Wrapper -->
    <locationmodal :Delete="Delete" />
</template>
<script>
const columns = [
  {
    title: "#",
    dataIndex: "NUM",
    sorter: {
      compare: (a, b) => {
        a = a.NUM.toLowerCase();
        b = b.NUM.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Challan ID",
    dataIndex: "ChallanID",
    sorter: {
      compare: (a, b) => {
        a = a.ChallanID.toLowerCase();
        b = b.ChallanID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Customer",
    dataIndex: "Customer",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.Customer.toLowerCase();
        b = b.Customer.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Amount",
    dataIndex: "Amount",
    sorter: {
      compare: (a, b) => {
        a = a.Amount.toLowerCase();
        b = b.Amount.toLowerCase();
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
    title: "Action",
    key: "action",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    ChallanID: "#4905681",
    img: "avatar-14.jpg",
    Customer: "John Smith",
    number: "+1 843-443-3282",
    Amount: "$1,54,220",
    CreatedOn: "19 Dec 2023, 06:12 PM",
  },
  {
    NUM: "2",
    ChallanID: "#4905682",
    img: "avatar-15.jpg",
    Customer: "Johnny",
    number: "+1 917-409-0861",
    Amount: "$2,54,220",
    CreatedOn: "15 Dec 2023, 04:35 PM",
  },
  {
    NUM: "3",
    ChallanID: "#4905683",
    img: "avatar-16.jpg",
    Customer: "Robert",
    number: "+1 956-623-2880",
    Amount: "$3,54,220",
    CreatedOn: "04 Dec 2023, 12:38 PM",
  },
  {
    NUM: "4",
    ChallanID: "#4905684",
    img: "avatar-17.jpg",
    Customer: "Sharonda",
    number: "+1 707-439-1732",
    Amount: "$4,54,220",
    CreatedOn: "28 Nov 2023, 03:25 PM",
  },
  {
    NUM: "5",
    ChallanID: "#4905685",
    img: "avatar-18.jpg",
    Customer: "Randall",
    number: "+1 559-741-9672",
    Amount: "$5,54,220",
    CreatedOn: "20 Nov 2022, 02:47 PM",
  },
  {
    NUM: "6",
    ChallanID: "#4905686",
    img: "avatar-19.jpg",
    Customer: "Pricilla",
    number: "+1 989-438-3131",
    Amount: "$4,54,220",
    CreatedOn: "15 Nov 2022, 10:42 AM",
  },
];
export default {
  data() {
    return {
      title: "Delivery Challans",
      Delete: "Delete Delivery Challans",
      text: "Create Delivery Challan",
      data,
      columns,
    };
  },
};
</script>
