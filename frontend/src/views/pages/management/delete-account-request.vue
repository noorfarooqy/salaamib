<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <div class="page-header">
          <div class="content-page-header">
            <h5>Delete Account Request</h5>
            <div class="list-btn">
              <ul class="filter-list">
                <li>
                  <a
                    class="btn btn-filters w-auto popup-toggle"
                    data-bs-toggle="tooltip"
                    data-bs-placement="bottom"
                    title="Filter"
                    ><span class="me-2"
                      ><img src="@/assets/img/icons/filter-icon.svg" alt="filter" /></span
                    >Filter
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <searchfilter />
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
                            >{{ record.UserName
                            }}<span>{{ record.mail }}</span></router-link
                          >
                        </h2>
                      </template>
                      <template v-else-if="column.key === 'Action'">
                        <div class="d-flex align-items-center">
                          <div class="dropdown dropdown-action">
                            <a
                              href="javascript:;"
                              class="btn-action-icon"
                              data-bs-toggle="dropdown"
                              aria-expanded="false"
                              ><i class="fas fa-ellipsis-v"></i
                            ></a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <ul>
                                <li>
                                  <a
                                    class="dropdown-item"
                                    href="javascript:void(0);"
                                    data-bs-toggle="modal"
                                    data-bs-target="#delete_modal"
                                    ><i class="far fa-trash-alt me-2"></i>Delete</a
                                  >
                                </li>
                              </ul>
                            </div>
                          </div>
                          <a href="javascript:;" class="btn btn-greys ms-2">Confirm</a>
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

  <deleteaccountrequestmodel></deleteaccountrequestmodel>
  <!-- /Main Wrapper -->
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
    title: "User Name",
    dataIndex: "UserName",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.UserName.toLowerCase();
        b = b.UserName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Requisition Date",
    dataIndex: "RequisitionDate",
    sorter: {
      compare: (a, b) => {
        a = a.RequisitionDate.toLowerCase();
        b = b.RequisitionDate.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Delete Request Date",
    dataIndex: "DeleteRequestDate",
    sorter: {
      compare: (a, b) => {
        a = a.DeleteRequestDate.toLowerCase();
        b = b.DeleteRequestDate.toLowerCase();
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
    NUM: "1",
    UserName: "John Smith",
    img: "avatar-14.jpg",
    mail: "john@example.com",
    RequisitionDate: "28 Sep 2023 16:43PM",
    DeleteRequestDate: "19 Dec 2023, 06:12 PM",
  },
  {
    NUM: "2",
    UserName: "Johnny",
    img: "avatar-15.jpg",
    mail: "johnny@example.com",
    RequisitionDate: "12 Dec 2023, 06:12 PM",
    DeleteRequestDate: "15 Dec 2023, 06:12 PM",
  },
  {
    NUM: "3",
    UserName: "Robert",
    img: "avatar-16.jpg",
    mail: "robert@example.com",
    RequisitionDate: "04 Dec 2023, 12:38 PM",
    DeleteRequestDate: "08 Dec 2023, 12:38 PM",
  },
  {
    NUM: "4",
    UserName: "Sharonda",
    img: "avatar-17.jpg",
    mail: "sharon@example.com",
    RequisitionDate: "14 Dec 2023, 12:38 PM",
    DeleteRequestDate: "24 Dec 2023, 12:38 PM",
  },
  {
    NUM: "5",
    UserName: "Pricilla",
    img: "avatar-18.jpg",
    mail: "pricilla@example.com",
    RequisitionDate: "12 Dec 2023, 12:38 PM",
    DeleteRequestDate: "13 Dec 2023, 12:38 PM",
  },
  {
    NUM: "6",
    UserName: "Randall",
    img: "avatar-19.jpg",
    mail: "randall@example.com",
    RequisitionDate: "04 Dec 2023, 12:38 PM",
    DeleteRequestDate: "09 Dec 2023, 12:38 PM",
  },
];
export default {
  setup() {
    return {
      data,
      columns,
    };
  },
};
</script>
