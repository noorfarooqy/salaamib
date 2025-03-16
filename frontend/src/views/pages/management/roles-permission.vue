<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <permissionheader :title="title" :text="text" />

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
                    <template #bodyCell="{ column }">
                      <template v-if="column.key === 'Action'">
                        <div class="d-flex align-items-center">
                          <a
                            href="javascript:;"
                            class="btn btn-greys me-2"
                            data-bs-toggle="modal"
                            data-bs-target="#edit_role"
                            ><i class="fa fa-edit me-1"></i> Edit Role</a
                          >
                          <router-link to="permission" class="btn btn-greys me-2"
                            ><i class="fa fa-shield me-1"></i> Permissions</router-link
                          >
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
    <ticketmodal></ticketmodal>
</template>
<script>
const columns = [
  {
    title: "ID",
    dataIndex: "ID",
    sorter: {
      compare: (a, b) => {
        a = a.ID.toLowerCase();
        b = b.ID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Role Name",
    dataIndex: "RoleName",
    sorter: {
      compare: (a, b) => {
        a = a.RoleName.toLowerCase();
        b = b.RoleName.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Created at",
    dataIndex: "Createdat",
    sorter: {
      compare: (a, b) => {
        a = a.Createdat.toLowerCase();
        b = b.Createdat.toLowerCase();
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
    ID: "1",
    RoleName: "Admin",
    Createdat: "19 Dec 2023, 06:12 PM",
  },
  {
    ID: "2",
    RoleName: "Customer",
    Createdat: "28 Nov 2023, 03:25 PM",
  },
  {
    ID: "3",
    RoleName: "Shop Owner",
    Createdat: "19 Dec 2023, 06:12 PM",
  },
  {
    ID: "4",
    RoleName: "Receptionist",
    Createdat: "9 Dec 2023, 06:12 PM",
  },
];
export default {
  setup() {
    return {
      title: "Roles & Permission",
      text: "Add Roles",
      data,
      columns,
    };
  },
};
</script>
