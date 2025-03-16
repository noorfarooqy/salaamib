<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <pageheader :title="title" :text="text" />
      <div class="row">
        <div class="col-md-12">
          <div class="card-table">
            <div class="card-body">
              <div class="table-responsive">
                <a-table class="stripped table-hover" :columns="columns" :data-source="data">
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'Status'">
                      <div class="status-toggle">
                        <input :id="record.Id" class="check" type="checkbox" checked />
                        <label :for="record.For" class="checktoggle checkbox-bg">{{
                          record.Status
                        }}</label>
                      </div>
                    </template>
                    <template v-else-if="column.key === 'action'">
                      <div class="d-flex align-items-center">
                        <a href="javascript:;" class="btn-action-icon me-2" data-bs-toggle="modal"
                          data-bs-target="#pages_edit"><span><i class="feaher feather-edit"></i></span></a>
                        <a href="javascript:;" class="btn-action-icon" data-bs-toggle="modal"
                          data-bs-target="#page_delete"><span><i class="feaher feather-trash-2"></i></span></a>
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

  <pagemodel></pagemodel>
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
    title: "Pages",
    dataIndex: "Pages",
    sorter: {
      compare: (a, b) => {
        a = a.Pages.toLowerCase();
        b = b.Pages.toLowerCase();
        return a > b ? -1 : b > a ? 1 : 0;
      },
    },
  },
  {
    title: "Pages Slug",
    dataIndex: "PagesSlug",
    sorter: {
      compare: (a, b) => {
        a = a.PagesSlug.toLowerCase();
        b = b.PagesSlug.toLowerCase();
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
    key: "action",
    sorter: true,
  },
];
const data = [
  {
    NUM: "1",
    Pages: "About Us",
    PagesSlug: "about-us",
    Status: "checkbox",
    Id: "rating_1",
    For: "rating_1",
  },
  {
    NUM: "2",
    Pages: "Cookie Policy",
    PagesSlug: "cookie-policy",
    Status: "checkbox",
    Id: "rating_2",
    For: "rating_2",
  },
  {
    NUM: "3",
    Pages: "FAQ",
    PagesSlug: "faq",
    Status: "checkbox",
    Id: "rating_3",
    For: "rating_3",
  },
  {
    NUM: "4",
    Pages: "Helps",
    PagesSlug: "helps",
    Status: "checkbox",
    Id: "rating_4",
    For: "rating_4",
  },
  {
    NUM: "5",
    Pages: "Home",
    PagesSlug: "home",
    Status: "checkbox",
    Id: "rating_5",
    For: "rating_5",
  },
  {
    NUM: "6",
    Pages: "Privacy Policy",
    PagesSlug: "privacy-policy",
    Status: "checkbox",
    Id: "rating_6",
    For: "rating_6",
  },
];
export default {
  setup() {
    return {
      title: "Pages list",
      text: "Add Page",
      data,
      columns,
    };
  },
};
</script>
