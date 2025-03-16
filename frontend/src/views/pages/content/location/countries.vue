<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <countriesheader :title="title" :text="text" />

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

      <!-- Table -->
      <div class="row">
        <div class="col-sm-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'id'">
                      <div class="d-flex align-items-center">
                        <h2>
                          <img class="avatar-img rounded me-2" width="30" height="30"
                            :src="require(`@/assets/img/flags/${record.img}`)" alt="User Image" />
                        </h2>

                        {{ record.CountryName }}
                      </div>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <a class="btn-action-icon me-2" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#edit_country"><i class="feather feather-edit"></i></a>
                        <a class="btn-action-icon" href="javascript:void(0);" data-bs-toggle="modal"
                          data-bs-target="#delete_modal"><i class="feather feather-trash-2"></i></a>
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

  <countriesmodel></countriesmodel>
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
    title: "Country Code",
    dataIndex: "CountryCode",
    sorter: {
      compare: (a, b) => {
        a = a.CountryCode.toLowerCase();
        b = b.CountryCode.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Country ID",
    dataIndex: "CountryID",
    sorter: {
      compare: (a, b) => {
        a = a.CountryID.toLowerCase();
        b = b.CountryID.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Country Name",
    dataIndex: "CountryName",
    key: "id",
    sorter: {
      compare: (a, b) => {
        a = a.CountryName.toLowerCase();
        b = b.CountryName.toLowerCase();
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
    img: "as.png",
    CountryCode: "AS",
    CountryID: "684",
    CountryName: "American Samoa(+684)",
  },
  {
    NUM: "2",
    img: "ad.png",
    CountryCode: "AD",
    CountryID: "376",
    CountryName: "Andorra (+376)",
  },
  {
    NUM: "3",
    img: "ao.png",
    CountryCode: "AO",
    CountryID: "244",
    CountryName: "Angola (+244)",
  },
  {
    NUM: "4",
    img: "ai.png",
    CountryCode: "AI",
    CountryID: "1264",
    CountryName: "Anguilla (+1264)",
  },
  {
    NUM: "5",
    img: "ag.png",
    CountryCode: "AQ",
    CountryID: "672",
    CountryName: "Antigua & Barbuda (+1268)",
  },
  {
    NUM: "6",
    img: "au.png",
    CountryCode: "AQ",
    CountryID: "1268",
    CountryName: "Australia",
  },
  {
    NUM: "7",
    img: "as.png",
    CountryCode: "AS",
    CountryID: "684",
    CountryName: "American Samoa(+684)",
  },
  {
    NUM: "8",
    img: "ad.png",
    CountryCode: "AD",
    CountryID: "376",
    CountryName: "Andorra (+376)",
  },
  {
    NUM: "9",
    img: "ao.png",
    CountryCode: "AO",
    CountryID: "244",
    CountryName: "Angola (+244)",
  },
];
export default {
  data() {
    return {
      title: "Countries",
      title1: "Delete Countries",
      text: "Add Countries",
      Delete: "Delete Countries",
      data,
      columns,
    };
  },
};
</script>
