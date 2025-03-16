<template>
  <div class="row">
    <div class="col-md-6">
      <div class="card bg-white">
        <div class="card-header">
          <h5 class="card-title">Basic tabs</h5>
        </div>
        <div class="card-body">
          <b-tabs content->
            <b-tab title="Home" active><span>Tab content 1</span></b-tab>
            <b-tab title="Profile"><span>Tab content 2</span></b-tab>
            <b-tab title="Messages"><span>Tab content 3</span></b-tab>
          </b-tabs>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card bg-white">
        <div class="card-header">
          <h5 class="card-title">Basic justified tabs</h5>
        </div>
        <div class="card-body">
          <ul class="nav nav-tabs nav-justified">
            <li class="nav-item">
              <a class="nav-link active" href="#basic-justified-tab1" data-bs-toggle="tab"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#basic-justified-tab2" data-bs-toggle="tab"
                >Profile</a
              >
            </li>
            <li class="nav-item dropdown">
              <a
                href="javascript:;"
                class="dropdown-toggle nav-link"
                data-bs-toggle="dropdown"
                >Dropdown</a
              >
              <div class="dropdown-menu dropdown-menu-right">
                <a class="dropdown-item" href="#basic-justified-tab3" data-bs-toggle="tab"
                  >Dropdown 1</a
                >
                <a class="dropdown-item" href="#basic-justified-tab4" data-bs-toggle="tab"
                  >Dropdown 2</a
                >
              </div>
            </li>
          </ul>
          <div class="tab-content">
            <div class="tab-pane show active" id="basic-justified-tab1">
              Tab content 1
            </div>
            <div class="tab-pane" id="basic-justified-tab2">Tab content 2</div>
            <div class="tab-pane" id="basic-justified-tab3">Tab content 3</div>
            <div class="tab-pane" id="basic-justified-tab4">Tab content 4</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
