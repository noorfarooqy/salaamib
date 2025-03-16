<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <element-breadcrumb :title="title" />
      <div class="row">
        <!-- Ribbon -->
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <ul class="timeline">
                <li>
                  <div class="timeline-badge success">
                    <i class="fas fa-user"></i>
                  </div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">{{ head1 }}</h4>
                    </div>
                    <div class="timeline-body">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero
                        laboriosam dolor perspiciatis omnis exercitationem. Beatae,
                        officia pariatur? Est cum veniam excepturi. Maiores praesentium,
                        porro voluptas suscipit facere rem dicta, debitis.
                      </p>
                    </div>
                  </div>
                </li>
                <li class="timeline-inverted">
                  <div class="timeline-badge warning">
                    <i class="fas fa-users"></i>
                  </div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">{{ head1 }}</h4>
                    </div>
                    <div class="timeline-body">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                        Laudantium maiores odit qui est tempora eos, nostrum provident
                        explicabo dignissimos debitis vel! Adipisci eius voluptates, ad
                        aut recusandae minus eaque facere.
                      </p>
                    </div>
                  </div>
                </li>
                <li>
                  <div class="timeline-badge danger">
                    <i class="fas fa-gift"></i>
                  </div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">{{ head }}</h4>
                    </div>
                    <div class="timeline-body">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                        Repellendus numquam facilis enim eaque, tenetur nam id qui vel
                        velit similique nihil iure molestias aliquam, voluptatem totam
                        quaerat, magni commodi quisquam.
                      </p>
                    </div>
                  </div>
                </li>
                <li class="timeline-inverted">
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">{{ head }}</h4>
                    </div>
                    <div class="timeline-body">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                        Voluptates est quaerat asperiores sapiente, eligendi, nihil.
                        Itaque quos, alias sapiente rerum quas odit! Aperiam officiis
                        quidem delectus libero, omnis ut debitis!
                      </p>
                    </div>
                  </div>
                </li>
                <li>
                  <div class="timeline-badge info">
                    <i class="fa fa-save"></i>
                  </div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">{{ head }}</h4>
                    </div>
                    <div class="timeline-body">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nobis
                        minus modi quam ipsum alias at est molestiae excepturi delectus
                        nesciunt, quibusdam
                      </p>
                    </div>
                  </div>
                </li>
                <li class="timeline-inverted">
                  <div class="timeline-badge success">
                    <i class="fa fa-graduation-cap"></i>
                  </div>
                  <div class="timeline-panel">
                    <div class="timeline-heading">
                      <h4 class="timeline-title">{{ head }}</h4>
                    </div>
                    <div class="timeline-body">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                        Deserunt obcaecati, quaerat tempore officia voluptas debitis
                        consectetur culpa amet, accusamus dolorum fugiat, animi dicta
                        aperiam, enim incidunt quisquam maxime neque eaque.
                      </p>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <!-- /Ribbon -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      head1: "Title",
      head: "Lorem ipsum dolor",
      title: "Timeline",
    };
  },
};
</script>
